# henripaul
class Kalkulaator:
    def __init__(self):
        pass

    def liitmine(self, a, b):  # liitmine
        return a + b

    def lahutamine(self, a, b):  # lahutamine
        return a - b

    def korrutamine(self, a, b):  # korrutamine
        return a * b

    def jagamine(self, a, b):  # jagamine
        if b != 0:
            return a / b
        else:
            print("nulliga ei saa jagada!")
            return None

    def kasutaja_sisend(self):  # kusib kasutajalt, mis tehet teha
        tehe = input("Valige tehe (liitmine, lahutamine, korrutamine, jagamine): ")
        ooga = float(input("Sisestage esimene number: "))
        booga = float(input("Sisestage teine number: "))

        if tehe == "liitmine":  # peamine susteem, et koik toimiks
            tulemus = self.liitmine(ooga, booga)
            print("Vastus: ", tulemus)
        elif tehe == "lahutamine":
            tulemus = self.lahutamine(ooga, booga)
            print("Vastus: ", tulemus)
        elif tehe == "korrutamine":
            tulemus = self.korrutamine(ooga, booga)
            print("Vastus: ", tulemus)
        elif tehe == "jagamine":
            tulemus = self.jagamine(ooga, booga)
            if tulemus is not None:
                print("Vastus: ", tulemus)
        else:
            print("Midagi läks näru, palun valige sobiv tehe.")


# kalkulaatori kasutamine
kalkulaator = Kalkulaator()
kalkulaator.kasutaja_sisend()
