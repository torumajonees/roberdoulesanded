# henripaul
class User():  # selle abil saame luua uldse enda panga konto
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):  # siin kuvatakse isiku personaalsed andmed
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):  # selle abil saame kontosse lisada raha
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : €", self.balance)

    def withdraw(self, amount):  # selle abil saame raha valja vonta kontost
        self.amount = amount
        if self.amount > self.balance:  # kui kontol pole piisavalt raha mida valja votta, tuleb veateade
            print("Insufficient Funds | Balance Available : €", self.balance)
        else:  # kui kontol on piisavalt raha, siis super
            self.balance = self.balance - self.amount
            print("Account balance has been updated : €", self.balance)

    def view_balance(self):  # naitab kontrojaaki
        self.show_details()
        print("Account balance: €", self.balance)
