# **The basics**

Let's start with the calculation!


# **Challenge**

Easy

Create function `calc` which gets operator and two numbers and returns the calculation result.

Examples:

`calc('+', 1, 3)` -> `4`

`calc('*', 2, 3)` -> `6`

`calc('/', 1, 4)` -> `0.25`

`calc('-', 1, 3)` -> `-2`

For now, deal only with the basic operators: `+`, `-`, `*`, `/`.

> *The return value can be float and not only int!*

---

# Solution

```python
def calc(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
```

# Explanation

The `calc` function takes three arguments:

```python
def calc(operator, num1, num2):
```

- `operator` stores the mathematical operator, such as `+`, `-`, `*`, or `/`.
- `num1` is the first number.
- `num2` is the second number.

We then use `if` and `elif` statements to check which operator was provided.

For addition:

```python
if operator == '+':
    return num1 + num2
```

If the operator is `+`, the function adds the two numbers and returns the result.

For subtraction:

```python
elif operator == '-':
    return num1 - num2
```

If the operator is `-`, the function subtracts the second number from the first.

For multiplication:

```python
elif operator == '*':
    return num1 * num2
```

If the operator is `*`, the function multiplies the two numbers.

For division:

```python
elif operator == '/':
    return num1 / num2
```

If the operator is `/`, the function divides the first number by the second.

The `/` operator can produce a `float`, which is why the result can be a decimal value, as required by the challenge.

For example:

```python
calc('+', 1, 3)  # 4
calc('*', 2, 3)  # 6
calc('/', 1, 4)  # 0.25
calc('-', 1, 3)  # -2
```

The important idea is to use the value of `operator` to decide which calculation should be performed, then `return` the corresponding result.

# **More operators**

We've added the basics operators: `+`, `-`, `*`, `/`

Let's add some more!

# **Challenge**

Easy

Add support for the operators -

- `%` - modulo operator
- `^` - power operator, `2^3` equal to `2³`

---

# Solution

```python
def calc(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '^':
        return num1 ** num2
```

# Explanation

We keep the four basic operators from the previous challenge and add two new cases.

For the modulo operator `%`:

```python
elif operator == '%':
    return num1 % num2
```

The `%` operator returns the remainder after dividing `num1` by `num2`.

For example:

```python
calc('%', 10, 3)  # 1
```

Because `10` divided by `3` has a remainder of `1`.

For the power operator `^`:

```python
elif operator == '^':
    return num1 ** num2
```

In Python, `**` is the exponentiation operator. It raises the first number to the power of the second number.

For example:

```python
calc('^', 2, 3)  # 8
```

Because `2³ = 8`.

> **Important:** In Python, `^` itself is the bitwise XOR operator, not the power operator. Therefore, we use `**` inside the function to implement the challenge's `^` operator.

The function now supports all six operators:

```python
calc('+', 1, 3)   # 4
calc('-', 1, 3)   # -2
calc('*', 2, 3)   # 6
calc('/', 1, 4)   # 0.25
calc('%', 10, 3)  # 1
calc('^', 2, 3)   # 8
```

# **Aliases**

The calculator should accept **alias names** for each operation:

- `add` for `+`
- `sub` for `-`
- `div` for `/`
- `mul` for `*`
- `pow` for `^`
- `mod` for `%`

---

# **Challenge**

Easy

Make `calc` support the alias names described above. Check the test cases for any clarification.

---

# Solution

```python
def calc(operator, num1, num2):
    operator = operator.lower()

    if operator == '+' or operator == 'add':
        return num1 + num2
    elif operator == '-' or operator == 'sub':
        return num1 - num2
    elif operator == '*' or operator == 'mul':
        return num1 * num2
    elif operator == '/' or operator == 'div':
        return num1 / num2
    elif operator == '^' or operator == 'pow':
        return num1 ** num2
    elif operator == '%' or operator == 'mod':
        return num1 % num2
```

# Explanation

First, we convert the `operator` to lowercase:

```python
operator = operator.lower()
```

This makes the calculator accept aliases regardless of their capitalization.

For example:

```python
calc('ADD', 1, 3)
calc('Add', 1, 3)
calc('add', 1, 3)
```

All three become `add` after calling `.lower()`.

Then, each `if`/`elif` checks both the mathematical operator and its alias:

```python
if operator == '+' or operator == 'add':
    return num1 + num2
```

So both `+` and `add` perform addition.

```python
elif operator == '-' or operator == 'sub':
    return num1 - num2
```

Both `-` and `sub` perform subtraction.

```python
elif operator == '*' or operator == 'mul':
    return num1 * num2
```

Both `*` and `mul` perform multiplication.

```python
elif operator == '/' or operator == 'div':
    return num1 / num2
```

Both `/` and `div` perform division.

```python
elif operator == '^' or operator == 'pow':
    return num1 ** num2
```

Both `^` and `pow` perform exponentiation. We use Python's `**` operator because `^` in Python is the bitwise XOR operator.

```python
elif operator == '%' or operator == 'mod':
    return num1 % num2
```

Both `%` and `mod` perform the modulo operation.

Using `operator.lower()` makes the alias names case-insensitive while leaving the mathematical operators unchanged.
