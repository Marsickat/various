class Alphabet:
    def __init__(self, language):
        self.language = language
        self.alphabets = {"en": [chr(c) for c in range(97, 123)],
                          "ru": [chr(c) for c in range(1072, 1104)]}
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.alphabets[self.language]):
            self.index = 0
        return self.alphabets[self.language][self.index]


test = Alphabet("ru")
print(next(test))