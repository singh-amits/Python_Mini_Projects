def my_decorator(func):
    def wrap_func():
        print('good')
        func()
        print('peace')
    return wrap_func


# @my_decorator
def hello():
    print('hello')


# @my_decorator
def bye():
    print('bye')


hello2 = my_decorator(hello)
print(hello2())
