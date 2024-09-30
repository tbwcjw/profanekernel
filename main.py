import os
import git
import read
import asyncio
import compile_results
import argparse
from tqdm import tqdm 

repo_url="https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git"
tree_url="https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/"

clone_dir="kernel/"

run_log = "runlog.csv"

csv_output = "matches.csv"
keywords_file = "keywords.txt"
count_file = "count.csv"

ignore_file = "ignore.txt"

concurrent = 10                         #number of files to read at the same time. too many will error out.

class Progress(git.RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()

def pull_or_clone():                                
    if not os.path.exists(clone_dir):               
        print(f"making directory.")
        os.makedirs(clone_dir)
    try:
        repo = git.Repo(clone_dir)
        print("Found repo. pulling.")
        origin = repo.remotes.origin
        origin.pull(progress=Progress())
    except git.exc.InvalidGitRepositoryError:
        print("No repo. cloning.")
        git.Repo.clone_from(repo_url, clone_dir, progress=Progress())

async def compile(result=None):
    print("compiling results")
    compile_results.write_to_readme(csv_output, "results/PROFANITY.md")
    compile_results.write_to_readme(count_file, "results/COUNT.md")
    compile_results.keyword_count_pie("count.csv", "results/COUNT.png")
    if result is not None:
        compile_results.write_to_runlog(result, "runlog.csv")
    

async def main():
    pull_or_clone()
    result = await read.search_recurse(keywords_file, ignore_file, clone_dir, tree_url, csv_output, count_file, concurrent)
    await compile(result)
    
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', nargs='?', default=None, help="command to execute")
    args = parser.parse_args()

    if args.command == "compile":           #compiles results
        asyncio.run(compile())
    else:
        asyncio.run(main())                 #default runs whole app

if __name__ == "__main__":
    parse_args()
