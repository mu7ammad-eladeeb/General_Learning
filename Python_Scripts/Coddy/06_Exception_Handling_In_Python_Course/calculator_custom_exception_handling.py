class InvalidOperation(Exception):
    pass


class InvalidOperator(Exception):
    pass


def calculator(exp):
    try:
        operators = ('+', '-', '*', '/')
        elements = exp.split()

        if len(elements) != 3:
            raise InvalidOperation(
                "Please enter two operands and operator separated by space"
            )

        op = elements[1]

        if op not in operators:
            raise InvalidOperator("Invalid operator")

        num1 = float(elements[0])
        num2 = float(elements[2])

        num1 / num2

    except Exception as e:
        print(e)

    else:
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2

        print(result)
