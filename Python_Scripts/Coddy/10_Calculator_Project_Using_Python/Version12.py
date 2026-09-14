def struct(lst):
    operators_high = ['*', '/', '%', 'mul', 'div', 'mod']
    operators_low = ['+', 'add', '-', 'sub']
    operators_power = ['^', '**', 'pow']

    while len(lst) > 1:
        has_high = any(item in operators_high for item in lst)
        has_power = any(item in operators_power for item in lst)
        reduced = False

        if has_power:
            for i in range(len(lst)-2, 0, -1):
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

        elif not has_high:
            for i in range(1, len(lst) - 1):
                if lst[i] in operators_low:
                    lst[i - 1:i + 2] = [[lst[i], lst[i - 1], lst[i + 1]]]
                    reduced = True
                    break

        if not reduced:
            break

    return lst[0]
