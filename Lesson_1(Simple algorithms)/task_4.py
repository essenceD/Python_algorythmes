# 4. Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят, и сколько между ними находится букв.

a = input('Enter first letter: ')
b = input('Enter second letter: ')
print(f'Position of letter "{a.lower()}" is {ord(a.lower()) - ord("a") + 1}')
print(f'Position of letter "{b.lower()}" is {ord(b.lower()) - ord("a") + 1}')
between = abs((ord(a.lower()) - ord("a") + 1) - (ord(b.lower()) - ord("a") + 1))
print(f'Between "{a.lower()}" and "{b.lower()}" placed {between - 1} letters.')
