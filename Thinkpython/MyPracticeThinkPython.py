from Tools.scripts.parseentities import writefile

print("Hello")

def backwards(words):
    for i in words[::-1]:
        print (i)
backwards("stevens")

x = ["stevens"]

for v in x[::-1]:
    print(v)

print(len(x))


def string_backwards(string):

    i = len(string)
    print(i)


string_backwards("Paul")


def count_item(item_list):
    return [item_list.count(item) for item in item_list]


print(count_item([2, 4, 2, 1, 2, 3, 4]))


def prime_number(x):
    if x < 2:
        return False
    else:
        n = 2
        while n < x:
            if x % n == 0:
                return False
                break
            n = n + 1
        else:
            return True


print(prime_number(23))
print(prime_number(41))


def str_len(string):
    count = 0
    for letter in string:
        count += 1
    return count


print(str_len(['a', 'b', 'c', 'd', 'e', 'f', 'g']))



