class Cesko:
    def hlavni_mesto(self):
        print("Praha")
    def pocet_obyvatel(self):
        print("10,700,000")
    def jazyk(self):
        print("Čeština")
    def nabozenstvi(self):
        print("Převážně Ateismus")

class Mexiko:
    def hlavni_mesto(self):
        print("Ciudad de Mexico")
    def pocet_obyvatel(self):
        print("128,400,000")
    def jazyk(self):
        print("Španělština")
    def nabozenstvi(self):
        print("Křesťanství")

class Thajsko:
    def hlavni_mesto(self):
        print("Bangkok")
    def pocet_obyvatel(self):
        print("68,414,000")
    def jazyk(self):
        print("Thajština")
    def nabozenstvi(self):
        print("Budhismus")

def zakladni_info(instance):
    instance.hlavni_mesto()
    instance.pocet_obyvatel()
    instance.jazyk()

staty = []

staty.append(Cesko)
staty.append(Thajsko)
staty.append(Mexiko)