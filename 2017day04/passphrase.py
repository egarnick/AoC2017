from sys import argv


class Passphrase:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def is_valid(self):
        unique_words = set()
        for word in self.phrase.split():
            word = ''.join(sorted(list(word)))
            if word in unique_words:
                return False
            else:
                unique_words.add(word)
        return True


if __name__ == '__main__':
    if len(argv) != 2:
        print("Must enter input file name as first command line argument")
    else:
        total_valid = 0
        for line in open(argv[1], 'r'):
            passphrase = Passphrase(line.strip())
            if passphrase.is_valid():
                total_valid += 1
        print("Total valid: {}".format(total_valid))

