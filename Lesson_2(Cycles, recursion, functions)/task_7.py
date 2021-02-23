# 7.
# Написать программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n, ans_1, line = int(input('Enter any number to check usability of following equal:\n'
                           '1 + 2 + ... + n = n * (n + 1) / 2\n'
                           'N = ')), 0, '0'
for i in range(1, n + 1):
    ans_1 += i
    line += f' + {i}'
ans_2 = n * (n + 1) / 2
line_2 = f'{n} * ({n} + 1) / 2 = {int(ans_2)}'
line += f' = {ans_1}'
print(f'{line}  <=>  {line_2}  => ')
if ans_1 == ans_2:
    print('=> Equal is correct!')
else:
    print('=> Equal is incorrect!')
