def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def calculate():
    a = float(input('enter a = '))
    b = float(input('enter b = '))
    operator = str(input('enter operator like +, -, *, /  = '))
    if operator in ['+', '-', '*', '/']:
        if operator == '+':
            print(f'a+b = {add(a, b)}')
        elif operator == '-':
            print(f'a-b = {sub(a, b)}')
        elif operator == '*':
            print(f'a*b = {mul(a, b)}')
        elif operator == '/':
            if a == 0:
                print("divident cannot be zero")
            else:
                print(f'a-b = {div(a, b)}')
    else:
        print("Invalid Operations")


calculate()


exit()
