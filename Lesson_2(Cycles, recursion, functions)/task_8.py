# 8.
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

match, line = 0, ''
print('This program will count the digit you\'ll enter in numbers yo\'ll enter.')
tries = int(input('Enter number of numbers to count digits: '))
dig = int(input('Enter digit which need to find: '))
for i in range(tries):
    num = int(input(f'Enter number where needed to find digit "{dig}": '))
    line += f'{num}\n'
    while num != 0:
        if num % 10 == dig:
            match += 1
        num //= 10
print(f'There are {match} digits "{dig}" in following numbers:\n{line}')
