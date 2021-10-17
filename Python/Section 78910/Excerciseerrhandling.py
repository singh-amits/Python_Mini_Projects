while True:
    try:
        age = int(input('what is your age ?'))
        10/age
    except ValueError:
        print('enter a number')
        continue
    except ZeroDivisionError:
        print('please enetr a value higher then 0')
        break
    else:
        print('thank u')
        break
    finally:
        print('ok, i am done')
    print('can u hear me ?')
