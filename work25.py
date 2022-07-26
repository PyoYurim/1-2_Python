def add1(a, b):
    result = a + b
    return result


def add2():
    result = 1 + 2
    return result

def add3(a, b):
    result = a + b
    print(result)

def add4():
    result = 3 + 6
    print(result)

value = add4()
print("add()", value)

value = add3(3, 4)
print("add3()", value)


value = add2()
print("add2()", value)

value = add1(1, 2)
print("add1()", value)
