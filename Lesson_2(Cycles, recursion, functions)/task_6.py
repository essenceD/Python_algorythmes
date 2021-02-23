# 6.
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import randint as rd

num, tries = rd(0, 100), 10
print(f'You have {tries} tries to recognize a number i\'ve imagine.')
while tries >= 0:
    if tries == 0:
        print(f'That was number {num}. You lose.')
        break
    print(f'Tries left: {tries}')
    ans = int(input('My number is: '))
    if ans == num:
        print('Congrats! You won!')
        break
    elif ans > num:
        print('No, my number is smaller...')
        tries -= 1
    else:
        print('no, my number is bigger...')
        tries -= 1
