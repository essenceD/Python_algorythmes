# 1.
# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
# задача считается не решённой.

import hashlib as h


def count_subs(s: str) -> int:

    num_subs = set()
    values = set()
    for i in range(len(s) + 1):
        for j in range(len(s) + 1):
            if len(s[i:j]) > 0 and s[i:j] != s:
                num_subs.add(h.sha1(s[i:j].encode('utf-8')).hexdigest())
                values.add(s[i:j])

    # Just for fun! We can count reverse sub-strings too! =)

    # for i in range(len(s) + 1):
    #     for j in range(len(s) + 1):
    #         if len(s[i:j]) > 0 and s[::-1][i:j] != s:
    #             num_subs.add(h.sha1(s[::-1][i:j].encode('utf-8')).hexdigest())
    #             values.add(s[::-1][i:j])

    # To check:
    if len(num_subs) > 0:
        print(values, num_subs, sep='\n')
    return len(num_subs)


s_1 = input('Enter string to count sub-strings: ')
ans = count_subs(s_1)
print(f'Number of different sub-strings: {ans}' if ans > 0 else 'There is no sub-strings!')
