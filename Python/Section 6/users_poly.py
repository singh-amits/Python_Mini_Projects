class user():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class wizard(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        user.attack(self)
        print(f'attacking with the power of {self.power}')


class archer(user):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left -{self.num_arrows}')


wizard1 = wizard('amit', 24)
archer1 = archer('shabu', 100)
print(wizard1.attack())
