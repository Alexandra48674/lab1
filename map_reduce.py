from functools import reduce
from pathlib import Path
from sys import argv
from collections import Counter
from time import perf_counter


def counter(path):
    with open(path) as f:
        return Counter(f.read().split())


def add(dict1):
    dict2 = {**dict1}
    return dict2


def dir_files():
    return reduce(add, map(counter, Path(argv[1]).glob("*.txt")))


if __name__ == "__main__":
    start = perf_counter()
    dir_files()
    end = perf_counter()
    print(dir_files())
    print("Time elapsed:", end - start)
