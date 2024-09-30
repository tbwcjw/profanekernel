from datetime import datetime
import os
import csv
import re
import asyncio
import aiofiles
import sys
import time
from collections import defaultdict

import compile_results

class Progress:
    def __init__(self):
        self.lock = asyncio.Lock()
        self.total_files = 0
        self.processed_files = 0
        self.start_time = time.time()

    def set_total_files(self, total):
        self.total_files = total

    async def update_processed_files(self):
        async with self.lock:
            self.processed_files += 1
            self.print_progress()

    def get_elapsed_time(self):
        elapsed_time = time.time() - self.start_time
        hours, remainder = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        elapsed_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        return elapsed_str


    def print_progress(self):
        sys.stdout.write(f'\rProcessed files: {self.processed_files}/{self.total_files} - Elapsed time: {self.get_elapsed_time()}')
        sys.stdout.flush()

async def kw(kf):
    async with aiofiles.open(kf, 'r', encoding='utf-8') as f:
        keywords = [line.strip().lower() for line in await f.readlines() if line.strip()]
    return keywords

async def ig(ig):
    async with aiofiles.open(ig, 'r', encoding='utf-8') as f:
        ignore_dirs = [line.strip() for line in await f.readlines() if line.strip()]
    return ignore_dirs

def combine_file_tree_paths(file_path, tree_path):
    w = file_path.split('/')
    file_path = '/'.join(w[1:]).replace("\\", "/")

    return f"{tree_path}{file_path}"

async def search_in_file(file_path, tree_path, line_number, line, pattern, csv_writer_lock, csv_writer, keyword_count):
    match = re.search(pattern, line, re.IGNORECASE)
    if match:
        keyword = match.group(0).strip().lower()
        async with csv_writer_lock:
            await csv_writer.writerow([combine_file_tree_paths(file_path, tree_path), line_number, keyword, line.strip()])
        
        keyword_count[keyword] += 1

async def process_file(file_path, tree_path, patterns, csv_writer_lock, csv_writer, progress, semaphore, keyword_count):
    async with semaphore:
        try:
            async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = await f.readlines()
                for line_number, line in enumerate(lines, start=1):
                    for pattern in patterns:
                        await search_in_file(file_path, tree_path, line_number, line, pattern, csv_writer_lock, csv_writer, keyword_count)
            await progress.update_processed_files()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

async def search_recurse(keywords, ignore, directory, tree_url, output_file, count_output_file, max_concurrent_files):
    keywords = await kw(keywords)
    ignore = await ig(ignore)

    patterns = []
    for keyword in keywords:
        if keyword.startswith('"') and keyword.endswith('"'):
            phrase = keyword[1:-1]
            patterns.append(r'\b' + re.escape(phrase) + r'\b')
        else:
            patterns.append(r'\b' + re.escape(keyword) + r'\b')

    print(keywords)

    csv_writer_lock = asyncio.Lock()
    progress = Progress()
    semaphore = asyncio.Semaphore(max_concurrent_files)
    keyword_count = defaultdict(int)

    total_files = sum(len(files) for _, dirs, files in os.walk(directory) if not any(ignored in _ for ignored in ignore))
    progress.set_total_files(total_files)

    async with aiofiles.open(output_file, 'w', newline='', encoding='utf-8') as csvf:
        csv_writer = csv.writer(csvf)
        await csv_writer.writerow(['file', 'line', 'keyword', 'match'])
        tasks = []
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in ignore]

            for file in files:
                file_path = os.path.join(root, file)
                tasks.append(process_file(file_path, tree_url, patterns, csv_writer_lock, csv_writer, progress, semaphore, keyword_count))
        await asyncio.gather(*tasks)

    async with aiofiles.open(count_output_file, 'w', newline='', encoding='utf-8') as count_csvf:
        count_csv_writer = csv.writer(count_csvf)
        await count_csv_writer.writerow(['keyword', 'count'])
        for keyword, count in keyword_count.items():
            await count_csv_writer.writerow([keyword.lower(), count])

    complete_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elapsed_time = progress.get_elapsed_time()
    total_matches = sum(keyword_count.values())

    return [complete_time, total_files, len(keywords), elapsed_time, total_matches]