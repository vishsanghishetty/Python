# Addition


def add(n1, n2):
    """Adds given numbers"""
    return n1 + n2


# Subtraction
def subtract(n1, n2):
    """Subtracts given numbers"""
    return n1 - n2


# Multiplication

def multiply(n1, n2):
    """Multiplies given numbers"""
    return n1 * n2


# Division

def divide(n1, n2):
    """Divides given numbers"""
    return n1 * n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

for symbol in operations:
    print(symbol)


operation_sym = input(f"pick an operation you want to perform from the above ?")

# operations[operation_sym] this produces add or subtract or multiply or divide values for the key in operations dict
calc_function = operations[operation_sym]
# print(operations[operation_sym])
answer = calc_function(num1, num2)
print(f"{num1} {operation_sym} {num2} equals {answer}")
