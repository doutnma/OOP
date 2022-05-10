class Person:

    """
    Třída, která reprezentuje člověka(osobu)
    """

    def __init__(self, _name, _birth, _email):
        self.name = _name
        self.__birth = _birth
        self.email = _email
        self.__address = None

    def __str__(self):
        return "Čest práci, mé jméno je:" + self.name

    def purchase_parking_pass(self):
        """
        Metoda, která vezme parkovací kartu
        :return:
        """
        print("Parking purchased!!!")

    def get_age(self):
        return 100 + self.__birth

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
        self.salary = _salary
        self.staff_num = _num

    def teach(self):
        print("V mých hodinách panuje tvrdá diktatura!!!")

class Student(Person):
    """
    Třída, která reprezentuje žáka
    """

    def __init__(self, _name, _birth, _email, _student_number, _mark):
        super().__init__(_name, _birth, _email)
        self.student_number = _student_number
        self.mark = _mark

class Address():
    """
    Třída, která reprezentuje adresu
    """

    def __init__(self, _street, _city, _postal_code):
        self.street = _street
        self.city = _city
        self.postal_code = _postal_code

    def __str__(self):
        return self.street + "," + self.city

    def __validate(self):
        return True

osoba = Person("Človíček", 1990, "clovek@sps-prosek.cz")
osoba.purchase_parking_pass()

skola = Address("U Dvou Řeznických psů ", "Vídeň za Rakouska-Uherska", 58000)
ucitel = Professor("Láďa Řehák nejstarší ", 1945, "ladarehaku@sps-prosek.cz", 16000, 1)

osoba.set_address(skola)
print(osoba.get_adress())