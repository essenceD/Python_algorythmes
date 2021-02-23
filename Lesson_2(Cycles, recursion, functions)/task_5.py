# 5.
# Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

start, limit, string, size = 32, 128, 0, 10
print('+----------------' * size + '+', sep='')
for i in range(size):
    print(f'|{(i + 1): 8}', end='')
    print(' ' * 8, end='')
print('|')
while start < limit:
    if string == 0:
        print('+----------------' * size + '+', sep='')
    if string != size:
        print(f'| symbol({start:03}): {chr(start)} ', end='')
        start += 1
        string += 1
    else:
        print('|\n' + '+----------------' * size + '+', sep='')
        print(f'| symbol({start:03}): {chr(start)} ', end='')
        string = 1
print('|\n' + '+----------------' * string + '+', sep='')
