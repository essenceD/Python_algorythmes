# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from random import randint as rd

base = [rd(-100, 100) for j in range(10)]
mx = -100
imx = 0
for i in base:
    if i < 0:
        if i > mx:
            mx = i
            imx = base.index(i)
print(f'Original list: {base}\nMAX negative value is "{mx}" with index "{imx}"')
