# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Enter 3 different numbers!')
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
if a == b or b == c or c == a:
    print('There is no numbers in the middle!')
else:
    if a > b:
        if a > c:
            if b > c:
                print(f'Middle is B = {b}')
            else:
                print(f'Middle is C = {c}')
        else:
            print(f'Middle is A = {a}')
    else:
        if b > c:
            if a > c:
                print(f'Middle is A = {a}')
            else:
                print(f'Middle is C = {c}')
        else:
            print(f'Middle is B = {b}')
