class Person:

    def __init__(self):
        self.__money = 0

    def set_money(self, amount):
        self.__money += amount

    def get_money(self):
        return self.__money

p1 = Person()
p1.set_money(100)
p1.get_money()

class Person:

    def __init__(self):
        self.__money = 0
        self.birth = 2004

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, amount):
        if amount > 0:
            self.__money += amount
        else:
            print("error")

    @property
    def name(self):
        return self.__money

    @name.setter
    def name(self, amount):
        if amount > 0:
            self.__money += amount
        else:
            print("too short")

    def add_money_to_account(self, amount, eur, date):
        self.money += amount
        self.eur = eur
        self.date = date

    @property
    def age(self):
        return 2022 - self.birth

p2 = Person()
p2.money = 100
p2.money = -10
print(p2.money)
print(p2.age)