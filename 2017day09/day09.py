from sys import argv
from typing import List, Tuple


def find_garbage(input_data: str) -> List[Tuple[int, int]]:
    garbage_ranges = []  # type: List[Tuple[int, int]]
    garbage_start = None
    garbage_end = None
    garbage_count = 0
    i = 0
    while i < len(input_data):
        if garbage_start is None and input_data[i] == '<':
            garbage_start = i
        while garbage_start is not None and garbage_end is None:
            i += 1
            if input_data[i] == '>':
                garbage_end = i
                garbage_count += garbage_end - garbage_start - 1
            elif input_data[i] == '!':
                i += 1
                garbage_count -= 2
        if garbage_start is not None and garbage_end is not None:
            garbage_ranges.append((garbage_start, garbage_end))
            garbage_start = garbage_end = None
        i += 1
    print("Total garbage: {}".format(garbage_count))
    return garbage_ranges


def clean_garbage(input_data: str) -> str:
    garbage_ranges = find_garbage(input_data)

    clean_data_spans = []
    clean_start = 0
    for garbage_range in garbage_ranges:
        clean_data_spans.append(input_data[clean_start:garbage_range[0]])
        clean_start = garbage_range[1] + 1
    if clean_start < len(input_data):
        clean_data_spans.append(input_data[clean_start:])
    return ''.join(clean_data_spans)


def score_data(input_data: str) -> int:
    score = 0
    depth = 0
    i = 0
    while i < len(input_data):
        if input_data[i] == '{':
            depth += 1
            score += depth
        while depth:
            i += 1
            if input_data[i] == '{':
                depth += 1
                score += depth
            elif input_data[i] == '}':
                depth -= 1
            elif input_data[i] == '!':
                i += 1
        i += 1
    return score


def score_groups(input_data: str):
    clean_data = clean_garbage(input_data)
    score = score_data(clean_data)
    print("Score: {}".format(score))


if __name__ == '__main__':
    if len(argv) > 1 and argv[1] == "test":
        input_file = "2017input09_test.txt"
    else:
        input_file = "2017input09.txt"
    puzzle_input = open(input_file, 'r').read().strip()
    score_groups(puzzle_input)
