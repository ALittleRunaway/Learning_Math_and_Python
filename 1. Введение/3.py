a = "3"
b = 2
def sum2(a, b):
    type_a = type(a)
    type_b = type(b)
    print(type_a, type_b)
    if ((type_a is not int) and (type_a is not float)) and ((type_b is not int) and (type_b is not float)):
        print("all arguments are not a numbers")
    elif (type_a is not int) and (type_a is not float):
        print("1st argument is not a number")
    elif (type_b is not int) and (type_b is not float):
        print("2nd argument is not a number")
    else:
        return sum([a, b])

def sum3(a, b):
    if type(a) not in (int, float) and type(b) not in (int, float):
        print("all arguments are not a numbers")
    elif type(a) not in (int, float):
        print("1st argument is not a number")
    elif type(b) not in (int, float):
        print("2nd argument is not a number")
    else:
        return (sum([a, b]))
# sum2(a, b)
# sum3(a, b)
