# get SHA256 from all .pmx, .pmd and .vmd files in the directory and subdirectories
import os
import sys
import hashlib
from tqdm import tqdm

def get_SHA256(path):
    # get SHA256 from all .pmx, .pmd and .vmd files in the directory and subdirectories
    for root, dirs, files in tqdm(os.walk(path)):
        for file in files:
            if file.endswith('.pmd') or file.endswith('.pmx') or file.endswith('.vmd'):
                with open(os.path.join(root, file), 'rb') as f1:
                    # write to Dataset_SHA256.txt
                    with open('Dataset_SHA256.txt', 'a') as f2:
                        f2.write(hashlib.sha256(f1.read()).hexdigest() + '\n')

# delete repeat lines in Dataset_SHA256.txt
def delete_repeat_lines():
    with open('Dataset_SHA256.txt', 'r') as f1:
        lines = f1.readlines()
        lines_set = set(lines)
        with open('Dataset_SHA256.txt', 'w') as f2:
            for line in lines_set:
                f2.write(line)

# sort lines in Dataset_SHA256.txt
def sort_lines():
    with open('Dataset_SHA256.txt', 'r') as f1:
        lines = f1.readlines()
        lines.sort()
        with open('Dataset_SHA256.txt', 'w') as f2:
            for line in lines:
                f2.write(line)

if __name__ == '__main__':
    path = "."
    get_SHA256(path)
    delete_repeat_lines()
    sort_lines()