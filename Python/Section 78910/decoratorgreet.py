# def hello():
#   print('hellooo')

#greet = hello

#del hello
# hello()
# print(greet())

def hello(func):
    func()


def greet():
    print('still here')


a = hello(greet)

print(a)
