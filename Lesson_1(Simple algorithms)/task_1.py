# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

n1 = int(bin(a), 2)
n2 = int(bin(b), 2)

_or = bin(n1 | n2)
_and = bin(n1 & n2)
_xor = bin(n1 ^ n2)
_inv_pos = bin(~n1)
_inv_neg = bin(~(~n1))
_strafe_right = bin(n1 >> 2)
_strafe_left = bin(n1 << 2)

print(f'{bin(a)} ({a}) OR {bin(b)} ({b}) = {_or} ({n1 | n2})')
print(f'{bin(a)} ({a}) AND {bin(b)} ({b}) = {_and} ({n1 & n2})')
print(f'{bin(a)} ({a}) XOR {bin(b)} ({b}) = {_xor} ({n1 ^ n2})')
print(f'(INVERT)~ {bin(a)} ({a}) = {_inv_pos} ({~n1})')
print(f'(INVERT)~ {bin(~n1)} ({~n1}) = {_inv_neg} ({~(~n1)})')
print(f'BIT SHIFT RIGHT: {bin(n1)} >> 2 = {_strafe_right} ({n1 >> 2})')
print(f'BIT SHIFT LEFT: {bin(n1)} << 2 = {_strafe_left} ({n1 << 2})')
