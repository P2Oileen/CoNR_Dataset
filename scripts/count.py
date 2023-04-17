# count how many *.pmd and *.pmx files in the directory
# and subdirectories
import os
import sys

def count_pmxorpmd(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pmd') or file.endswith('.pmx'):
                count += 1
    return count

def count_vmd(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.vmd'):
                count += 1
    return count

if __name__ == '__main__':
    path = "."
    print("model count:", count_pmxorpmd(path + '/model/'))
    print("motion count:", count_vmd(path + '/motion/'))