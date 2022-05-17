class Karta:
    def __init__(self, _hodnota, _barva):
        self.hodnota = _hodnota
        self.barva = _barva

class Balicek:
    def __init__(self):
        self.__karty = []
        barvy = ["S", "K", "P", "L"]
        hodnoty = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

        for barva in barvy:
            for hodnota in hodnoty:
                self.__karty.append(Karta(hodnota, barva))

class Hrac:
    pass

class Krupier:
    pass