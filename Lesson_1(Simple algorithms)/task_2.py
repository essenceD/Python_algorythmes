# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

print('Enter coordinates for two dots to generate func y = kx + b')
x1 = float(input('Enter X1: '))
y1 = float(input('Enter Y1: '))
x2 = float(input('Enter X2: '))
y2 = float(input('Enter Y2: '))
if x1 == y1 and x2 == y2:
    print('Your func is: y = x')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y1 - k * x1
    if b > 0:
        print(f'Your func is: y = {round(k, 2)}x + {round(b, 2)}')
    else:
        if b < 0:
            print(f'Your func is: y = {round(k, 2)}x - {abs(round(b, 2))}')
        else:
            print(f'Your func is: y = {round(k, 2)}x')
