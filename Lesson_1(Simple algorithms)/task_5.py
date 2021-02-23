# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


num = int(input('Enter id of letter: '))
if 0 < num < 27:
    letter = chr(ord('a') + num - 1)
    print(f'It is letter "{letter}"')
else:
    print(f'There is no letter with id = {num}')
