number = int(input('Enter a number = '))


def flag(number):
    return True if number % 2 else False


def generate_seriese(number):
    if number != 0:
        i = 1
        last = int(not flag(number))
        while number > last:
            print(i, end=',')
            number -= 1
            i += 2
    else:
        print('invalid number')


generate_seriese(number)
