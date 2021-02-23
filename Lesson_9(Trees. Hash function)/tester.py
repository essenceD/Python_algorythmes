# Для измерения максимальной глубины списка

def get_depth(arr: list) -> int:
    return 1 + max(get_depth(itm) for itm in arr) if type(arr) == list else 0


print(get_depth([[['о', ['б', 'я']], [[['в', 'е'], ['ж', 'з']], [['и', 'к'], ['л', 'п']]]], [[[['р', 'т'], ['ч', 'ы']], ' '], [['с', 'у'], [['ь', 'а'], 'н']]]]))

