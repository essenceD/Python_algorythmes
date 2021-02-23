# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.


year = int(input('Enter year: '))
if year % 400 == 0:
    print(f'Year {year} is leap!')
elif year % 100 == 0:
    print(f'Year {year} is NOT leap!')
elif year % 4 == 0:
    print(f'Year {year} is leap!')
else:
    print(f'Year {year} is NOT leap!')
