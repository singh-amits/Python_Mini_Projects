class user(object):

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class wizard(user):
    def __init__(self, name, power, email):
        user.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')


# class archer(user):

    # def __init__(self, name, num_arrows):
        #self.name = name
        #self.num_arrows = num_arrows

   # def attack(self):
     #   print(f'attacking with arrows: arrows left -{self.num_arrows}')


wizard1 = wizard('amit', 24, 'amit@gmail.com')
#archer1 = archer('shabu', 100)
print(wizard1.email)
