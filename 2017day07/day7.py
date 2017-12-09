from sys import argv
from typing import List, Dict


def calc_weight(tower_base: str,
                program_weights: Dict[str, int],
                programs_to_supported: Dict) -> int:
    try:
        supported_weights = [calc_weight(supported,
                                         program_weights,
                                         programs_to_supported)
                             for supported in programs_to_supported[tower_base]]
        if len(set(supported_weights)) > 1:
            print("_+_+_+_+_+ {}".format([(sup, program_weights[sup]) for sup in programs_to_supported[tower_base]]))
            print("+++++++UNEVEN WEIGHTS: {}".format(supported_weights))
        return program_weights[tower_base] + sum(supported_weights)
    except KeyError:
        return program_weights[tower_base]


def bottom_program(program_specifications: List[str]):
    programs_to_supported = {}
    supported_programs_set = set()

    program_weights = {}

    base_program = ''

    for program_specification in program_specifications:
        spec_split = [spec.strip() for spec in
                      program_specification.split('->')]
        program_name, program_weight = [spec.strip('()') for spec in
                                        spec_split[0].split()]
        program_weights[program_name] = int(program_weight)

        if len(spec_split) > 1:
            supported_programs = [program.strip() for program in
                                  spec_split[1].split(',')]
            for supported in supported_programs:
                supported_programs_set.add(supported)
            programs_to_supported[program_name] = supported_programs
    for program in programs_to_supported:
        if program not in supported_programs_set:
            base_program = program
            print("Base program: {}".format(program))
            break

    tower_weights = {}
    for tower_base in programs_to_supported[base_program]:
        tower_weights[tower_base] = calc_weight(tower_base, program_weights, programs_to_supported)
    print("TOWER WEIGHTS:", tower_weights)
    all_weights = list(tower_weights.values())
    print("ALL WEIGHTS:", all_weights)
    off_weight = [weight for weight in all_weights if
                  all_weights.count(weight) == 1][0]
    std_weight = list({weight for weight in all_weights if
                       all_weights.count(weight) > 1})[0]
    off_tower = [tower for tower in tower_weights.keys() if
                 tower_weights[tower] == off_weight][0]
    individual_weight = program_weights[off_tower]
    print("Individual weight: {}".format(individual_weight))
    print("Standard weight: {}".format(std_weight))
    print("Off weight: {}".format(off_weight))
    print("Necessary weight: {}".format(individual_weight +
                                        (std_weight - off_weight)))


if __name__ == "__main__":
    test = argv[1]
    if test == 'true':
        input_data = [thing.strip() for thing in
                      open('2017input07_test.txt', 'r')]
    else:
        input_data = [thing.strip() for thing in open('2017input07.txt', 'r')]
    bottom_program(input_data)
