from collections import defaultdict
from sys import argv
from typing import List


COMPARISONS = {'==': int.__eq__, '!=': int.__ne__, '>': int.__gt__,
               '<': int.__lt__, '>=': int.__ge__, '<=': int.__le__}
OPERATIONS = {'inc': int.__add__, 'dec': int.__sub__}


def parse_instructions(instructions: str,
                       register_values: defaultdict[str, int]) -> int:
    operation, amount, if_word, condition = instructions.split(maxsplit=3)
    condition_key, comparison, condition_value = condition.split()
    if COMPARISONS[comparison](register_values[condition_key],
                               int(condition_value)):
        return OPERATIONS[operation](0, int(amount))
    else:
        return 0


def update_registers(input_data: List[str]):
    register_values = defaultdict(lambda: 0)
    max_seen = 0
    for datum in input_data:
        register_name, instructions = datum.split(maxsplit=1)
        value_update = parse_instructions(instructions, register_values)
        try:
            register_values[register_name] += value_update
        except KeyError:
            register_values[register_name] = value_update
        updated_value = register_values[register_name]
        if updated_value > max_seen:
            max_seen = updated_value
    print("Largest value: {}".format(max_seen))


if __name__ == "__main__":
    if len(argv) > 1 and argv[1] == "test":
        input_file = "2017input08_test.txt"
    else:
        input_file = "2017input08.txt"
    puzzle_input = [line.strip() for line in open(input_file, 'r')]
    update_registers(puzzle_input)


