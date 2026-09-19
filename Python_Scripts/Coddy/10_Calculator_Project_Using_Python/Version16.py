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
    operators_power = ['^', '**', 'pow']

    if not isinstance(lst, list):
        raise Exception(f'Failed to structure "{lst}"')

    if len(lst) == 2:
        return lst

    if len(lst) <= 1 or len(lst) % 2 == 0:
        raise Exception(f'Failed to structure "{lst}"')

    while len(lst) > 1:
        has_high = any(item in operators_high for item in lst)
        has_low = any(item in operators_low for item in lst)
        has_power = any(item in operators_power for item in lst)

        has_typo = any(
            not isinstance(item, (int, float, list))
            and item not in (operators_high + operators_low + operators_power)
            for item in lst
        )

        reduced = False

        if has_power:
            for i in range(len(lst) - 2, 0, -1):
                if lst[i] in operators_power:
                    lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
                    reduced = True
                    break

        elif has_high:
            for i in range(1, len(lst) - 1):
                if lst[i] in operators_high:
                    lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
                    reduced = True
                    break

        elif has_low:
            for i in range(1, len(lst) - 1):
                if lst[i] in operators_low:
                    lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
                    reduced = True
                    break

        elif has_typo:
            for i in range(1, len(lst) - 1):
                if (
                    lst[i] not in (operators_high + operators_low + operators_power)
                    and not isinstance(lst[i], (int, float, list))
                ):
                    lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
                    reduced = True
                    break

        if not reduced:
            raise Exception(f'Failed to structure "{lst}"')

    return lst[0]
def get_next(str_val, indx):

    n_list = []

    for i in str_val[indx:]:

        if i.isdigit() or i == ".":
            n_list.append(i)

        else:
            break

    finale = "".join(n_list)

    if "." in finale:
        return float(finale)

    else:
        return int(finale)
