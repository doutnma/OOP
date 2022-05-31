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
        self.teams = []

class Match:
    """
    Třída, která reprezentuje zápas
    """
    def __init__(self, _home_team, _away_team, _home_team_goals, _away_team_goals):
        self.home_team = _home_team
        self.away_team = _away_team
        self.home_team_goals = _home_team_goals
        self.away_team_goals = _away_team_goals

hrac1 = Player("Harry", "Maguire", "England", "Center Back", 3, 10000000, 3)
hrac2 = Player("Bruno", "Fernandes", "Portugal", "Ofensive Midfielder", 10, 25000000, 5)
hrac3 = Player("Cristiano", "Ronaldo", "Portugal", "Center Forward", 7, 30000000, 2)

trener1 = Coach("Erik", "Ten Hag", "Netherlands", 3000000, 5)
trener2 = Coach("Pep", "Guardiola", "Spain", 4000000, 3)
trener3 = Coach("Jurgen", "Klopp", "Germany", 2000000, 2)

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