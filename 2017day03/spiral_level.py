from sys import argv
from typing import Optional, List


class SpiralLevel:
    def __init__(self, level_sides: Optional[List[List[int]]]=None,
                 inner_level=None):
        self.level_height = 1
        self.inner_level = inner_level  # type: SpiralLevel
        self.level_sides = level_sides or [[], [], [], []]

    def __str__(self):
        return str(self.level_sides)

    def build_level(self):
        self.level_height = self.inner_level.level_height + 1
        for side_index in range(len(self.level_sides)):
            side = self.level_sides[side_index]
            inner_side = [self.inner_level.level_sides[side_index - 1][-1]] + \
                self.inner_level.level_sides[side_index]
            if side_index == len(self.level_sides) - 1:
                # Last side ends with first element of first side
                inner_side.append(self.level_sides[0][0])
            for node_index in range(self.level_height * 2):
                side.append(0)
                if node_index == 0:
                    if side_index != 0:
                        # Sides after the first get the last 2 values from the
                        # previous side
                        side[0] += self.level_sides[side_index - 1][-1]
                        side[0] += self.level_sides[side_index - 1][-2]
                else:
                    # Nodes after the first on a side get the prior node value
                    side[node_index] += side[node_index - 1]
                for adjust in [-1, 0, 1]:
                    adjusted_index = node_index + adjust
                    if 0 <= adjusted_index < len(inner_side):
                        side[node_index] += inner_side[adjusted_index]
            self.level_sides[side_index] = side


if __name__ == '__main__':
    if len(argv) != 2:
        print("Must enter target value as first command line argument")
    else:
        target = int(argv[1])
        last_level = SpiralLevel(level_sides=[[1, 2], [4, 5],
                                              [10, 11], [23, 25]])
        done = False
        while not done:
            for spiral_side in last_level.level_sides:
                if done:
                    break
                for node in spiral_side:
                    if done:
                        break
                    if node > target:
                        print("Next greater value:", node)
                        done = True
            next_level = SpiralLevel(inner_level=last_level)
            next_level.build_level()
            last_level = next_level

