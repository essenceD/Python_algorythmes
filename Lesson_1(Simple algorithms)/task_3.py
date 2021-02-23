# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import randint as rd


choose = input('Choose what do you want to generate:\n'
               'Enter 1 to generate random INTEGER\n'
               'Enter 2 to generate random FLOAT\n'
               'Enter 3 to generate random SYMBOL\n'
               'Your choice: ')

if choose == '1':
    start = int(input('Input start value for INTEGER: '))
    fin = int(input('Input final value for INTEGER: '))
    if start >= fin:
        print('Incorrect interval!')
    else:
        ans = rd(start, fin)
        print(f'Random INT from [{start};{fin}] is {ans}')
else:
    if choose == '2':
        start = float(input('Input start value for FLOAT: '))
        fin = float(input('Input final value for FLOAT: '))
        if start >= fin:
            print('Incorrect interval!')
        else:
            ans = rd(int(start), int(fin)) + rd(int((start - int(start)) * 100), int((fin - int(fin)) * 100)) / 100
            print(f'Random FLOAT from [{start};{fin}] is {round(ans, 2)}')
    else:
        start = input('Input start value for STRING (enter char): ')
        fin = input('Input final value for STRING (enter char): ')
        if ord(start) >= ord(fin):
            print('Incorrect interval!')
        else:
            ans = chr(rd(ord(start), ord(fin)))
            print(f'Random SYMBOL from [{start};{fin}] is {ans}')
