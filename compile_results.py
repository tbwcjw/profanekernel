import csv
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
import os

def month_year_key(folder):                     #folders MUST be formatted like "MonthYear" ("%B%Y")
    fmonth = folder[:-4]
    year = int(folder[-4:])
    month = datetime.strptime(fmonth, "%B").month
    return (year, month)

def keyword_over_time(path, output):
    data_dict = {}

    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        data_dict[folder] = []

        with open(f"{folder_path}/count.csv", mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                keyword = row['keyword']
                count = int(row['count'])

                data_dict[folder].append({
                    "keyword": keyword,
                    "count": count
                })

    keyword_counts = {}
    for folder, keywords in data_dict.items():
        for entry in keywords:
            keyword = entry['keyword']
            count = entry['count']

            if keyword not in keyword_counts:
                keyword_counts[keyword] = {}
            
            keyword_counts[keyword][folder] = count

    sorted_folders = sorted(
        os.listdir(path),
        key=month_year_key
    )

    plt.figure(figsize=(10, 6))

    for keyword, counts in keyword_counts.items():
        counts_values = [counts.get(folder, 0) for folder in sorted_folders]
        
        plt.plot(sorted_folders, counts_values, marker='o', label=keyword)

    plt.text(0.5, 0.5, 'profanekernel.xyz', fontsize=50, color='gray', 
         ha='center', va='center', alpha=0.2, rotation=45, transform=plt.gca().transAxes)
    plt.title('Keyword Count Over Time')
    plt.xlabel('Month/Year')
    plt.ylabel('Keyword Count')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(output)
                    

def keyword_count_pie(csvf, output):
    keyword_counts = defaultdict(int)

    with open(csvf, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            keyword = row['keyword']
            count = int(row['count'])
            keyword_counts[keyword] += count

        keywords = []
        counts = []
        total_count = sum(keyword_counts.values())

        for keyword, count in keyword_counts.items():
            percentage = (count / total_count) * 100
            if percentage >= 1:
                keywords.append(keyword)
                counts.append(count)

        
        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=keywords, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 16})
        plt.axis('equal')
        plt.text(0.5, -0.075, 'profanekernel.xyz', fontsize=50, color='gray', 
         ha='center', va='center', alpha=0.5, transform=plt.gca().transAxes)
        plt.savefig(output)

def csv_to_md_table(csvf):
    with open(csvf, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        headers = rows[0]
        markdown = "| " + " | ".join(headers) + "|\n"                   #header
        markdown += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'  #separator

        for row in rows[1:]:
            markdown += "| " + " | ".join(row) + ' |\n'                 #row
    
    markdown += f"\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    return markdown

def write_to_readme(csvf, output):
    md = csv_to_md_table(csvf)
    with open(output, 'w') as f:
        f.write(md)
        f.close()

def append_to_readme(str, output):
    with open(output, 'a') as f:
        f.write(f"\n{str}")
        f.close()

def write_to_runlog(input, file):
    with open(file, 'a', newline='', encoding='utf-8') as csvf:
        csv_writer = csv.writer(csvf)
        csv_writer.writerow(input)