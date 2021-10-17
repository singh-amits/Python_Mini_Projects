class user():
    def sign_in(self):
        print('logged in')


class wizard(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')


class archer(user):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left -{self.num_arrows}')


wizard1 = wizard('amit', 24)
archer1 = archer('shabu', 100)


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)
