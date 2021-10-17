while True:
    try:
        age = int(input('what is your age ?'))
        10/age
    except ValueError:
        print('enter a number')
    except ZeroDivisionError:
        print('please enetr a value higher then 0')
    else:
        print('thank u')
        break
