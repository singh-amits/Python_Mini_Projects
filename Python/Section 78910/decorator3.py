def my_decorator(func):
    # def wrap_func(x, y):
    def wrap_func(*args, **kwargs):
        print('good')
        #func(x, y)
        func(*args, **kwargs)
        print('peace')
    return wrap_func


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


#a = my_decorator(hello)
hello('hii')
