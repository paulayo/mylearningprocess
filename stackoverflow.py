

# import string
# import random


# def id_generator(size=6, chars=string.ascii_uppercase+string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

# print(id_generator())

# print(id_generator(3, "6793YUIO"))


# print(string.ascii_uppercase)

# print(string.digits)

# print(string.ascii_uppercase+string.digits)

# print(range(4))


# print(['elem' for _ in range(4)])

# print(random.choice("abcde"))

# print(random.choice("abcde"))
# print(random.choice("abcde"))
# print(random.choice("abcde"))
# random.choice("abcde")
# print([random.choice('abcde') for _ in range(3)])
# print([random.choice('abcde') for _ in range(3)])
# [random.choice('abcde') for _ in range(3)]

# [random.choice('abcde') for _ in range(3)]

# print(''.join(['a','b','b']))

# print([''.join(random.choice('abcde')) for _ in range(3)])

# print([' '.join(random.choice('vaecdeg123')) for _ in range(5)])

# print((id_generator()))


# ################
# # how to sum items in list seperately

# def count_items(column_list):
#     return [column_list.count(item) for item in set(column_list)]


#     column_list = ['male','male','','','','female','male','female']


# print(count_items(['male','male','','','','female','male','female']))




#understanding generators in python

def myGen(n):
    yield n 
    yield n + 1


g = myGen(6)
next(g)

next(g)

next(g)

for n in myGen(n):
    print(n)


# Generator expressions
g = (n for n in range(3,5))
next(g)

next(g)
# List comprehension

lc = [n for n in range(3, 5)]

print(lc)


# Fibonacci Numbers

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

import itertools
list(itertools.islice(fib(), 10))



def myGenerator():
    yield 'These'
    yield 'words'
    yield 'come'
    yield 'one'
    yield 'at'
    yield 'a'
    yield 'time'

myGeneratorInstance = myGenerator()
next(myGeneratorInstance)

next(myGeneratorInstance)

for word in myGeneratorInstance:
    print(word)


# Dealing with infinity

from time import gmtime, strftime
def myGen():
    while True:
        yield strftime('%a, %d %b %Y %H:%M:%S +0000', gmtime())
myGeneratorInstance = myGen()
next(myGenertorInstance)

next(myGeneratorInstance)


# What does the yield keyword do?

def _get_child_candidates(self, distance, min_dist, max_dist):
    if self._leftchild and distance - max_dist < self._median:
        yield self._leftchild
    if self._rightchild and distance + max_dist >= self._median:
        yield self._rightchild
        result, candidates = [], [self]
while candidates:
    node = candidates.pop()
    distance = node._get_dist(obj)
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
return result