from art import logo


def addition(number1, number2):
    result = number1 + number2
    return result


def subtraction(number1, number2):
    result = number1 - number2
    return result


def division(number1, number2):
    result = number1 / number2
    return result


def multiplication(number1, number2):
    result = number1 * number2
    return result


operations = {"+": addition,
              "-": subtraction,
              "/": division,
              "*": multiplication,
              }


def calculator():
    print(logo)
    num1 = float(input("Enter First Number\n:"))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above\n:")
        num2 = float(input("What's your next number?\n:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        more = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start new or 'x' to exit. \n:")

        if more == "y":
            num1 = answer
        elif more == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False


calculator()
