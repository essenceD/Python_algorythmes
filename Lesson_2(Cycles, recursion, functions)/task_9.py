# 9.
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_num, max_sum, num, num_to_check, sum_to_check = '', 0, '', '', 0
print('This program calculates digits sum in entered numbers and returns maximum one.')
while True:
    to_add = input('Enter number or "stop" to stop entering: ')
    if to_add.lower() == 'stop':
        if len(num) > 0:
            break
        else:
            print('You have to enter at least 1 number!')
    else:
        num += f'{to_add};'
for i in num:
    if i == ';':
        for j in num_to_check:
            sum_to_check += int(j)
        if sum_to_check > max_sum:
            max_sum = sum_to_check
            max_num = num_to_check
        num_to_check = ''
        sum_to_check = 0
    else:
        num_to_check += i

print(f'Biggest sum is {max_sum} in number "{max_num}".')
