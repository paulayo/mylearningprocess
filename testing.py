for i in range(1,11):
    print(f"8 * {i} = {8 * i}")



for i in range(2, 12):
    print(f"{3} * {i} = {3 * i}")
def print_multiplication_table(table):
    for i in range(1,11):
        print(f"{table} * {i} = {table * i}")
print_multiplication_table(3)

def _method_to_understand_indentation():
    for i in range(1,11):
        print(i)
        print(5)
_method_to_understand_indentation()


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


print(sleep_in('a,a'))


def print_string(str="Money  Bank", no_of_times=3):
    for i in range(1,  no_of_times+1):
        print(str)
print_string()


print_string(55)

print_string(no_of_times=6)

print_string(7, 8)

print_string(7.5, int("8"))


for i in range(1,10, -1):
    print(i)
print(i)

for i in range(10, 0, -1):
    print(i)
    print(i*i)

x = 34 - 23
y = "Hello "
z = 3.45
if z == 3.45 or y == "Hello ":
    x = y + "World"
print(x)
print(y)



# How to merge two dicts
# in python 3.5 +


x = {'a': 1, 'b':2}
y = {'b':3, 'c':4}

z = {**x, **y}

print(z)

