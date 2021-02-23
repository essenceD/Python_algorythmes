from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'name, age')
p_1 = Person('Vasya', 25)
p_2 = Person('Kolya', 30)
p_3 = Person('Olya', 23)

people = [p_1, p_2, p_3]
print(people)
res = sorted(people)
print(res)


def by_age(pers):
    return pers.age


res = sorted(people, key=by_age)
print(res)


res_2 = sorted(people, key=attrgetter('age'))
print(res_2)
