# сравнение строк через хэш
import hashlib


def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Strings should not be empty!'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f'hash_1 = {ha}\nhash_2 = {hb}')

    return ha == hb


s_1 = input('Enter message 1: ')
s_2 = input('Enter message 2: ')
print('Strings are same!' if is_eq_str(s_1, s_2, verbose=True) else 'Strings are different!')













