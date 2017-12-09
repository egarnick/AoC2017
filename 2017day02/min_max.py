from sys import argv
from typing import List, Callable


def total_differences_by_function(number_rows: List[str],
                                  aggregation_function: Callable) -> int:
    total = 0
    for row in number_rows:
        number_row = [int(number) for number in row.split()]
        total += aggregation_function(number_row)
    return total


def min_max_diff_for_row(number_row: List[int]) -> int:
    minimum = maximum = int(number_row[0])
    for num in number_row:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return maximum - minimum


def divisible_for_row(number_row: List[int]) -> int:
    for i in range(len(number_row) - 1):
        num_i = number_row[i]
        for j in range(i + 1, len(number_row)):
            num_j = number_row[j]
            if num_i % num_j == 0:
                return num_i // num_j
            elif num_j % num_i == 0:
                return num_j // num_i


if __name__ == '__main__':
    if len(argv) != 3:
        print("Must enter file name and aggregation function "
              "as command line args")
    else:
        data_file, aggregation_function_name = argv[1:]
        aggregation_function_mapping = {"min_max": min_max_diff_for_row,
                                        "divisible": divisible_for_row}
        string_number_rows = []
        for line in open(data_file, 'r'):
            string_number_rows.append(line.strip())
        print("Total is {}".format(total_differences_by_function(
            string_number_rows,
            aggregation_function_mapping[aggregation_function_name])))

