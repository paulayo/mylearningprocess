

import string
import random


def id_generator(size=6, chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print(id_generator())

print(id_generator(3, "6793YUIO"))


print(string.ascii_uppercase)

print(string.digits)

print(string.ascii_uppercase+string.digits)

print(range(4))


print(['elem' for _ in range(4)])

print(random.choice("abcde"))

print(random.choice("abcde"))
print(random.choice("abcde"))
print(random.choice("abcde"))
random.choice("abcde")
print([random.choice('abcde') for _ in range(3)])
print([random.choice('abcde') for _ in range(3)])
[random.choice('abcde') for _ in range(3)]

[random.choice('abcde') for _ in range(3)]

print(''.join(['a','b','b']))

print([''.join(random.choice('abcde')) for _ in range(3)])

print([' '.join(random.choice('vaecdeg123')) for _ in range(5)])

print((id_generator()))


################
# how to sum items in list seperately

def count_items(column_list):
    return [column_list.count(item) for item in set(column_list)]


    column_list = ['male','male','','','','female','male','female']


print(count_items(['male','male','','','','female','male','female']))

