# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

a = int(input('Enter side A: '))
b = int(input('Enter side B: '))
c = int(input('Enter side C: '))
if a + b <= c or a + c <= b or b + c <= a:
    print('Impossible triangle')
elif a != b and a != c and b != c:
    print('Versatile triangle')
elif a == b == c:
    print('Equilateral triangle')
else:
    print('Isosceles triangle')
