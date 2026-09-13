def calc(operator, num1, num2=None):
    operator = operator.lower()
    
    if not isinstance(num1, (int, float)):
        raise Exception(f'Invalid number "{num1}"')

    if num2 is not None and not isinstance(num2, (int, float)):
        raise Exception(f'Invalid number "{num2}"')

    if operator not in ['+', '-', '*', '/', '^', '%',
                        'add', 'sub', 'mul', 'div', 'pow', 'mod']:
        raise Exception(f'Invalid operator "{operator}"')

    # Single number operations
    if num2 is None:
        if operator == '+' or operator == 'add':
            return num1
        elif operator == '-' or operator == 'sub':
            return -num1
        else:
            raise Exception(f'Invalid operator "{operator}"')

    # Two number operations
    if operator == '+' or operator == 'add':
        return num1 + num2
    elif operator == '-' or operator == 'sub':
        return num1 - num2
    elif operator == '*' or operator == 'mul':
        return num1 * num2
    elif operator == '/' or operator == 'div':
        if num2 == 0:
            raise Exception("Division by zero")
        return num1 / num2
    elif operator == '^' or operator == 'pow':
        return num1 ** num2
    elif operator == '%' or operator == 'mod':
        if num2 == 0:
            raise Exception("Division by zero")
        return num1 % num2
# eval function to unpack a list
def eval(lst):
    if not isinstance(lst, list) or len(lst) not in [2, 3]:
        raise Exception(f'Failed to evaluate "{lst}"')

    if len(lst) == 2:
        operator, num1 = lst

        if isinstance(num1, list):
            num1 = eval(num1)

        return calc(operator, num1)

    elif len(lst) == 3:
        operator, num1, num2 = lst

        if isinstance(num1, list):
            num1 = eval(num1)

        if isinstance(num2, list):
            num2 = eval(num2)

        return calc(operator, num1, num2)
# struct function to format the list to be suitable for eval function
def struct(lst):
    operators_high = ['*', '/', '%', 'mul', 'div', 'mod']
    operators_low = ['+', 'add', '-', 'sub']

    while len(lst) > 1:
        has_high = any(item in operators_high for item in lst)

        for i in range(1, len(lst) - 1):
            if has_high and lst[i] in operators_high:
                lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
                break

            elif not has_high and lst[i] in operators_low:
                # Replace 3 elements (left, op, right) with 1 nested prefix list
                lst[i - 1:i + 2] = [[lst[i], lst[i - 1], lst[i + 1]]]
                break  # exits for loop so we can start iterating from 0 again

    return lst[0]
