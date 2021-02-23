# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

ans = {f'Numbers are even {i + 2}':
       [j for j in range(2, 100) if j % (i + 2) == 0] for i in range(8)}
for i in ans.keys():
    print(f'Total {len(ans[i])} {i}:', *ans[i])
