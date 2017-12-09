from sys import argv


class SpiralDistance:
    def __init__(self, target: int):
        self.target = target
        self.higher_square = 1
        self.corner_distance = 0
        self.corners = [0, 0, 0, 0]
        self.midway = 0
        self.midway_distance = 0
        self.target_distance = 0

    def set_higher_square(self):
        root = 1
        while root ** 2 < self.target:
            root += 2
        self.corner_distance = root - 1
        self.higher_square = root ** 2

    def set_corners(self):
        for i in range(len(self.corners)):
            self.corners[i] = self.higher_square - \
                              self.corner_distance * i
        self.corners = [val for val in self.corners[::-1]]
            
    def set_midway(self):
        for corner in self.corners:
            if corner - self.target < self.corner_distance:
                self.midway = corner - self.corner_distance // 2
                self.midway_distance = self.corner_distance // 2

    def set_target_distance(self):
        self.target_distance = self.midway_distance + abs(self.midway -
                                                          self.target)


if __name__ == '__main__':
    if len(argv) != 2:
        print("Must enter target number as command line argument")
    else:
        sd = SpiralDistance(int(argv[1]))
        sd.set_higher_square()
        print("Higher square: {}".format(sd.higher_square))
        print("Higher square distance: {}".format(sd.corner_distance))
        sd.set_corners()
        print("Corners for target level: {}".format(sd.corners))
        sd.set_midway()
        print("Midway value: {}".format(sd.midway))
        print("Midway distance: {}".format(sd.midway_distance))
        sd.set_target_distance()
        print("Target distance: {}".format(sd.target_distance))
