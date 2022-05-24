class Person:

    """
    Třída, která reprezentuje člověka(osobu)
    """

    def __init__(self, _name, _birth, _email):
        self.name = _name
        self.birth = _birth
        self.email = _email
        self.__address = None

    def __str__(self):
        return "Čest práci, mé jméno je:" + self.name

    def purchase_parking_pass(self):
        """
        Metoda, která vezme parkovací kartu
        :return:
        """

        print("Parkování informace: Parkování pro Láďu zadarmo, kvůli jeho pokročilejšímu věku!!!")

    def get_age(self):
        return 2022 - self.birth

    def set_address(self, _address):
        self.__address = _address

    def get_adress(self):
        return self.__address

class Professor(Person):
    """
    Třída, která reprezentuje učitele
    """

    def __init__(self, _name, _birth, _email, _salary, _num):
        super().__init__(_name, _birth, _email)
        self.__salary = _salary
        self.staff_num = _num

    def teach(self):
        print("V mých hodinách panuje tvrdá diktatura!!!")

class Student(Person):
    """
    Třída, která reprezentuje žáka
    """

    def __init__(self, _name, _birth, _email, _student_number, _mark):
        super().__init__(_name, _birth, _email)
        self.__student_number = _student_number
        self.mark = _mark

class Address():
    """
    Třída, která reprezentuje adresu
    """

    def __init__(self, _street, _city, _postal_code):
        self.__street = _street
        self.__city = _city
        self.__postal_code = _postal_code

    def __str__(self):
        return self.__street + "," + self.__city

    def __validate(self):
        return True

osoba = Person("Človíček", 1990, "clovek@sps-prosek.cz")
osoba.purchase_parking_pass()

skola = Address("U Dvou Řeznických Psů ", "Vídeň za Rakouska-Uherska", 58000)

osoba.set_address(skola)
print(osoba.get_adress())

ucitel = Professor("Láďa Řehák nejstarší ", 1875, "ladarehaku@sps-prosek.cz", 100000, 4)
zak = Student("Jan Brousek Official", 2005, "brouskos@email.cz", 3, 5)