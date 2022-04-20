from pathlib import Path
from sys import argv
from collections import Counter
from time import perf_counter


def dir_files():
    res = {}

    for item in Path(argv[1]).glob("*.txt"):
        with open(item) as f:
            my_dict = Counter(f.read().split())

            for key in my_dict:
                if key not in res:
                    res[key] = my_dict[key]
                elif key in res:
                    res[key] += my_dict[key]

    return res


if __name__ == "__main__":
    start = perf_counter()
    dir_files()
    end = perf_counter()
    print(dir_files())
    print("Time elapsed:", end-start)
