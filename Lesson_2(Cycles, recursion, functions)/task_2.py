# 2.
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Enter number to check its digits on parity: ')
even = ''
n_even = 0
odd = ''
n_odd = 0

for i in num:
    if int(i) % 2 == 0:
        even += f'{i};'
        n_even += 1
    else:
        odd += f'{i};'
        n_odd += 1
print(f'In number {num}:\n'
      f'{n_even} evens: {even[:-1]}\n'
      f'{n_odd} odds: {odd[:-1]}')
