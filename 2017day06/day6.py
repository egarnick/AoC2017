from sys import argv
from typing import List


def find_max_redistributions(memory_blocks: List[int]) -> int:
    seen_distributions = {}
    distribution = redistribute_blocks(memory_blocks)
    distribution_count = 1
    distribution_string = '-'.join([str(block) for block in distribution])
    while distribution_string not in seen_distributions:
        seen_distributions[distribution_string] = distribution_count
        distribution_count += 1
        distribution = redistribute_blocks(memory_blocks)
        distribution_string = '-'.join([str(block) for block in distribution])

    return distribution_count - seen_distributions[distribution_string]


def redistribute_blocks(memory_blocks: List[int]) -> List[int]:
    num_blocks = len(memory_blocks)
    target_value = max(memory_blocks)
    target_idx = memory_blocks.index(target_value)
    memory_blocks[target_idx] = 0
    i = (target_idx + 1) % num_blocks
    while target_value:
        memory_blocks[i] += 1
        target_value -= 1
        i = (i + 1) % num_blocks
    return memory_blocks


if __name__ == "__main__":
    input_file = argv[1]
    data = [int(block) for block in open(input_file, 'r').read().strip().split()]
    print(data)
    num_redistributions = find_max_redistributions(data)
    print("Looped after {} redistributions".format(num_redistributions))


