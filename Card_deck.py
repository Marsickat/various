class CardDeck:
    def __init__(self):
        self.denominations = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
        self.suits = ["пик", "треф", "бубен", "червей"]
        self.denomination_index = -1
        self.suit_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        for _ in self.suits:
            for _ in self.denominations:
                self.denomination_index += 1
                if self.denomination_index == 13:
                    self.denomination_index = 0
                    self.suit_index += 1
                    if self.suit_index == 4:
                        raise StopIteration
                return f"{self.denominations[self.denomination_index]} {self.suits[self.suit_index]}"


test = CardDeck()
print(*test)
