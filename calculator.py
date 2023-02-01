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
    return n1 / n2


print("**********************************")
print("C A L C U L A T O R")
print("**********************************")


def calc():
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    num1 = float(input("Enter the first number : "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_sym = input(f"pick an operation you want to perform from the above ?")
        num2 = float(input("Enter the next number : "))
        # operations[operation_sym] this produces add or subtract or multiply or divide values
        # for the key in operations dict
        calc_function = operations[operation_sym]
        # print(operations[operation_sym])
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_sym} {num2} equals {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to exit : ") == "y":
            num1 = answer
        else:
            should_continue = False
            calc()
            break


calc()
