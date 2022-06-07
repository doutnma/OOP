class Person:
    """
    Třída, která reprezentuje člověka
    """
    def __init__(self, _name, _surname, _country):
        self.name = _name
        self.surname = _surname
        self.country = _country

class Player(Person):
    """
    Třída, která reprezentuje hráče, který dědí parametry osoby
    """
    def __init__(self, _name, _surname, _country, _position, _jersey_number, _salary, _contract_lenght):
        super().__init__(_name, _surname, _country)
        self.position = _position
        self.jersey_number = _jersey_number
        self.__salary = _salary
        self.__contract_lenght = _contract_lenght

class Coach(Person):
    """
    Třída, která reprezentuje trenéra, který dědí parametry osoby
    """
    def __init__(self, _name, _surname, _country, _salary, _contract_lenght):
        super().__init__(_name, _surname, _country)
        self.__salary = _salary
        self.__contract_lenght = _contract_lenght

class Team:
    """
    Třída, která reprezentuje tým
    """
    def __init__(self, _name, _country, _city):
        self.name = _name
        self.country = _country
        self.city = _city
        self.stadion = None
        self.trener = None
        self.hrac = []

    def prirad_stadion(self, stadion):
        self.stadion = stadion

    def prirad_trenera(self, trener):
        self.trener = trener

    def prirad_hrace(self, hrac):
        self.hrac.append(hrac)

    def get_trener(self):
        print("V týmu " + self.name + " trénuje: " + self.trener.name + " " + self.trener.surname)

    def get_stadion(self):
        print("Tým " + self.name + " hraje na stadionu: " + self.stadion.name + ", který má kapacitu " + str(self.stadion.capacity) + " míst")

    def get_hrac(self):
        for x in self.hrac:
            print("V týmu " + self.name + " hraje: " + x.name + " " + x.surname + ", s číslem dresu: " + str(x.jersey_number))

class Stadium:
    """
    Třída, která reprezentuje stadion
    """
    def __init__(self, _name, _capacity):
        self.name = _name
        self.capacity = _capacity

class Competition:
    """
    Třída, která reprezentuje soutěž
    """
    def __init__(self, _name, _country):
        self.name = _name
        self.continent = _country
        self.tym = []

    def prirad_tymy(self, tym):
        self.tym.append(tym)

"""
class Match:
    
    #Třída, která reprezentuje zápas
    
    def __init__(self, _home_team, _away_team, _home_team_goals, _away_team_goals):
        self.home_team = _home_team
        self.away_team = _away_team
        self.home_team_goals = _home_team_goals
        self.away_team_goals = _away_team_goals
"""

hrac1 = Player("Harry", "Maguire", "England", "Center Back", 3, 10000000, 3)
hrac2 = Player("Bruno", "Fernandes", "Portugal", "Offensive Midfielder", 10, 25000000, 5)
hrac3 = Player("Cristiano", "Ronaldo", "Portugal", "Center Forward", 7, 30000000, 2)
hrac4 = Player("Kevin", "De Bruyne", "Belgium", "Offensive Midfielder", 10, 11000000, 2)
hrac5 = Player("Gabriel", "Jesus", "Brazil", "Center Forward", 7, 20000000, 3)
hrac6 = Player("Ruben", "Dias", "Portugal", "Center Back", 2, 31000000, 6)
hrac7 = Player("Alexandre", "Lacazette", "France", "Center Forward", 9, 10000000, 3)
hrac8 = Player("Emile", "Smith Rowe", "England", "Ofensive Midfielder", 10, 15000000, 4)
hrac9 = Player("Benjamin", "White", "England", "Center Back", 5, 10000000, 5)
hrac10 = Player("Mohamed", "Salah", "Egypt", "Right Winger", 8, 100000000, 2)
hrac11 = Player("Diogo", "Jota", "Portugal", "Ofensive Midfielder", 10, 10000000, 3)
hrac12 = Player("Virgil", "Van Dijk", "Netherlands", "Center Back", 3, 40000000, 1)
hrac13 = Player("Harry", "Kane", "England", "Center Forward", 7, 110000000, 2)
hrac14 = Player("Steven", "Bergwijn", "Netherlands", "Left Winger", 12, 26000000, 4)
hrac15 = Player("Davinson", "Sanchez", "Colombia", "Center Back", 2, 43000000, 3)
hrac16 = Player("Romelu", "Lukaku", "Belgium", "Center Forward", 7, 130000000, 1)
hrac17 = Player("Mason", "Mount", "England", "Ofensive Midfielder", 10, 89000000, 4)
hrac18 = Player("Andreas", "Christensen", "Denmark", "Center Back", 2, 56000000, 3)
hrac19 = Player("Bruno", "Guimaraes", "Portugal", "Center Midfielder", 13, 17000000, 5)
hrac20 = Player("Kieran", "Trippier", "England", "Right Back", 6, 10000000, 2)
hrac21 = Player("Chris", "Wood", "New Zealand", "Center Forward", 9, 70000000, 3)
hrac22 = Player("Lucas", "Digne", "France", "Left Back", 5, 80000000, 3)
hrac23 = Player("Phillipe", "Coutinho", "Brazil", "Ofensive Midfielder", 10, 95000000, 4)
hrac24 = Player("Leon", "Bailey", "Jamaica", "Left Winger", 15, 60000000, 5)
hrac25 = Player("Ruben", "Neves", "Portugal", "Center Midfielder", 8, 80000000, 2)
hrac26 = Player("Willy", "Boly", "France", "Center Back", 3, 40000000, 1)
hrac27 = Player("Francisco", "Trincao", "Portugal", "Right Winger", 18, 50000000, 5)

trener1 = Coach("Erik", "Ten Hag", "Netherlands", 3000000, 5)
trener2 = Coach("Pep", "Guardiola", "Spain", 4000000, 3)
trener3 = Coach("Mikel", "Arteta", "Spain", 2000000, 4)
trener4 = Coach("Jurgen", "Klopp", "Germany", 2000000, 2)
trener5 = Coach("Antonio", "Conte", "Italy", 3000000, 3)
trener6 = Coach("Thomas", "Tuchel", "Germany", 6000000, 2)
trener7 = Coach("Eddie", "Howe", "Scotland", 8000000, 3)
trener8 = Coach("Steven", "Gerrard", "England", 3500000, 2)
trener9 = Coach("Bruno", "Lage", "Portugal", 1000000, 3)


tym1 = Team("Manchester United", "England", "Manchester")
tym2 = Team("Manchester City", "England", "Manchester")
tym3 = Team("Arsenal", "England", "London")
tym4 = Team("Liverpool FC", "England", "Liverpool")
tym5 = Team("Tottenham", "England", "London")
tym6 = Team("Chelsea", "England", "London")
tym7 = Team("Newcastle United", "England", "Newcastle")
tym8 = Team("Aston Villa", "England", "Birmingham")
tym9 = Team("Wolves", "England", "Wolverhampton")

stadion1 = Stadium("Old Trafford", 82000)
stadion2 = Stadium("Etihad Stadium", 70000)
stadion3 = Stadium("Emirates Stadium", 80000)
stadion4 = Stadium("Anfield", 60000)
stadion5 = Stadium("Tottenham Hotspur Stadium", 50000)
stadion6 = Stadium("Stamford Bridge", 65000)
stadion7 = Stadium("St James Park", 48000)
stadion8 = Stadium("Villa Park", 55000)
stadion9 = Stadium("Molineux Stadium", 30000)

soutez1 = Competition("Premier League", "England")

tym1.prirad_stadion(stadion1)
tym2.prirad_stadion(stadion2)
tym3.prirad_stadion(stadion3)
tym4.prirad_stadion(stadion4)
tym5.prirad_stadion(stadion5)
tym6.prirad_stadion(stadion6)
tym7.prirad_stadion(stadion7)
tym8.prirad_stadion(stadion8)
tym9.prirad_stadion(stadion9)

tym1.prirad_trenera(trener1)
tym2.prirad_trenera(trener2)
tym3.prirad_trenera(trener3)
tym4.prirad_trenera(trener4)
tym5.prirad_trenera(trener5)
tym6.prirad_trenera(trener6)
tym7.prirad_trenera(trener7)
tym8.prirad_trenera(trener8)
tym9.prirad_trenera(trener9)

tym1.prirad_hrace(hrac1)
tym1.prirad_hrace(hrac2)
tym1.prirad_hrace(hrac3)
tym2.prirad_hrace(hrac4)
tym2.prirad_hrace(hrac5)
tym2.prirad_hrace(hrac6)
tym3.prirad_hrace(hrac7)
tym3.prirad_hrace(hrac8)
tym3.prirad_hrace(hrac9)
tym4.prirad_hrace(hrac10)
tym4.prirad_hrace(hrac11)
tym4.prirad_hrace(hrac12)
tym5.prirad_hrace(hrac13)
tym5.prirad_hrace(hrac14)
tym5.prirad_hrace(hrac15)
tym6.prirad_hrace(hrac16)
tym6.prirad_hrace(hrac17)
tym6.prirad_hrace(hrac18)
tym7.prirad_hrace(hrac19)
tym7.prirad_hrace(hrac20)
tym7.prirad_hrace(hrac21)
tym8.prirad_hrace(hrac22)
tym8.prirad_hrace(hrac23)
tym8.prirad_hrace(hrac24)
tym9.prirad_hrace(hrac25)
tym9.prirad_hrace(hrac26)
tym9.prirad_hrace(hrac27)


soutez1.prirad_tymy(tym1)
soutez1.prirad_tymy(tym2)
soutez1.prirad_tymy(tym3)
soutez1.prirad_tymy(tym4)
soutez1.prirad_tymy(tym5)
soutez1.prirad_tymy(tym6)
soutez1.prirad_tymy(tym7)
soutez1.prirad_tymy(tym8)
soutez1.prirad_tymy(tym9)

print("\n")
tym1.get_trener()
tym1.get_stadion()
tym1.get_hrac()
print("\n")
tym2.get_trener()
tym2.get_stadion()
tym2.get_hrac()
print("\n")
tym3.get_trener()
tym3.get_stadion()
tym3.get_hrac()
print("\n")
tym4.get_trener()
tym4.get_stadion()
tym4.get_hrac()
print("\n")
tym5.get_trener()
tym5.get_stadion()
tym5.get_hrac()
print("\n")
tym6.get_trener()
tym6.get_stadion()
tym6.get_hrac()
print("\n")
tym7.get_trener()
tym7.get_stadion()
tym7.get_hrac()
print("\n")
tym8.get_trener()
tym8.get_stadion()
tym8.get_hrac()
print("\n")
tym9.get_trener()
tym9.get_stadion()
tym9.get_hrac()
