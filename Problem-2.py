number = int(input('Enter a number = '))


def generate_seriese(number):
    if number != 0:
        i = 1
        while number > 0:
            print(i, end=',')
            number -= 1
            i += 2
    else:
        print('invalid number')


generate_seriese(number)
