# 1
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    operator = input('Enter operator [+] [-] [/] [*] or [0] to exit\nOperator: ')
    if operator in '/*-+0':
        if operator == '0':
            break
        else:
            a = float(input('Enter first number: '))
            if operator == '/':
                while True:
                    b = float(input('Enter second number: '))
                    if b != 0:
                        break
                    else:
                        print('Divider should be NOT ZERO!')
            else:
                b = float(input('Enter second number: '))
        print(eval(f'{a} {operator} {b}'))
    else:
        print('You\'ve entered incorrect symbol!')
