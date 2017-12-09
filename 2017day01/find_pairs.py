from sys import argv


def find_pairs(sequence: str):
    total = 0
    for i in range(len(sequence)):
        half_len = len(sequence) // 2
        if i < half_len:
            other_index = i + half_len
        else:
            other_index = i - half_len
        if sequence[i] == sequence[other_index]:
            total += int(sequence[i])
    print("Total for dupicates is:", total)


if __name__ == '__main__':
    if len(argv) != 2:
        print("Must enter input file name as command line argument")
    else:
        input_file = argv[1]
        input_data = open(input_file, 'r').read().strip()
        find_pairs(input_data)
