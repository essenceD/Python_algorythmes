# поиск подстроки в строке через хэш
import hashlib


def rabin_karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Strings should not be empty!'
    assert len(s) >= len(subs), 'Substring should be longer than string!'

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            return i
    return -1


s_1 = input('Enter string: ')
s_2 = input('Enter substring to search: ')
pos = rabin_karp(s_1, s_2)
print(f'Substring was fond in {pos} position!' if pos != -1 else 'Substring was not fond!')
