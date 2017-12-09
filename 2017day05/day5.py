from sys import argv


class Jumper:
    def __init__(self, input_file_name: str):
        self.input_file_name = input_file_name
        self.instructions = []
        self.steps = 0

    def fill_instructions(self):
        for line in open(self.input_file_name, 'r'):
            self.instructions.append(int(line.strip()))

    def follow_instructions(self):
        instr_idx = 0
        while 0 <= instr_idx < len(self.instructions):
            instruction = self.instructions[instr_idx]
            if instruction >= 3:
                self.instructions[instr_idx] -= 1
            else:
                self.instructions[instr_idx] += 1
            instr_idx += instruction
            self.steps += 1


if __name__ == "__main__":
    instr_file = argv[1]
    j = Jumper(instr_file)
    j.fill_instructions()
    j.follow_instructions()
    print("Number of steps:", j.steps)

