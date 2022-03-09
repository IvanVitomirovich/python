from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_cosumption(self, list_suits):
        a = 0
        for suit in list_suits:
            a += suit.consumption
        return a


coat = Coat(50)
costume = Suit(1.80)
costume_1 = Suit(1.75)
costume_2 = Suit(1.83)
costume_3 = Suit(1.90)
list_costumes = [costume_3, costume_2, costume_1, costume]
print(coat.consumption)
print(costume.consumption)
print(costume.sum_cosumption(list_costumes))
