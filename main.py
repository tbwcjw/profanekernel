import os
import git
import read
import asyncio
import compile_results

from tqdm import tqdm 

repo_url="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git"
clone_dir="kernel/"

csv_output = "matches.csv"
keywords_file = "keywords.txt"
count_file = "count.csv"

ignore_file = "ignore.txt"

concurrent = 10

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
    
if __name__ == "__main__":
    #pull_or_clone()
    #asyncio.run(read.search_recurse(keywords_file, ignore_file, clone_dir, csv_output, count_file, concurrent))
    compile_results.write_to_readme(csv_output)