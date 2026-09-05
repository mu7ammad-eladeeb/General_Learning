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

# **Handling errors**

There are some possible errors we should consider,

- Division by zero - `calc('/', 3, 0)` or `calc('%', 5, 0)`
- Invalid operator - `calc('$', 3, 2)`
- Invalid number - `calc('+', 'not_a_number', 2)`


# **Challenge**

Medium

Add to `calc` option to raise an exceptions when the above errors happen.

The error messages should be in the following formats,

- `calc('/', 3, 0)` -> `Division by zero`
- `calc('$', 3, 2)` -> `Invalid operator "$"`
- `calc('+', [], 3)` -> `Invalid number "[]"`

> ***Number**** is of type **`int`** or **`float`**

## **Hints**

To raise an exception with the message `"msg"` use,

```python
raise Exception("msg")
```

To check if `var` is of type `int`,

```python
isinstance(var, int)
```

Don't forget to check also `float`!

---

# Solution

```python
def calc(operator, num1, num2):
    operator = operator.lower()

    if not isinstance(num1, (int, float)):
        raise Exception(f'Invalid number "{num1}"')

    if not isinstance(num2, (int, float)):
        raise Exception(f'Invalid number "{num2}"')

    if operator not in ['+', '-', '*', '/', '^', '%',
                        'add', 'sub', 'mul', 'div', 'pow', 'mod']:
        raise Exception(f'Invalid operator "{operator}"')

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
```

# Explanation

The goal is to make `calc` detect three types of errors:

1. Invalid numbers
2. Invalid operators
3. Division by zero

## 1. Check that the numbers are valid

A valid number must be either an `int` or a `float`.

```python
if not isinstance(num1, (int, float)):
    raise Exception(f'Invalid number "{num1}"')
```

The same check is performed for `num2`:

```python
if not isinstance(num2, (int, float)):
    raise Exception(f'Invalid number "{num2}"')
```

`isinstance()` checks whether a value belongs to one of the specified types.

Using:

```python
isinstance(num1, (int, float))
```

means that `num1` is valid if it is either an `int` or a `float`.

If it isn't, we use `raise Exception()` to stop the function and display the required error message.

For example:

```python
calc('+', [], 3)
```

raises:

```text
Invalid number "[]"
```

## 2. Check that the operator is valid

We create a list containing all supported operators and aliases:

```python
if operator not in ['+', '-', '*', '/', '^', '%',
                    'add', 'sub', 'mul', 'div', 'pow', 'mod']:
    raise Exception(f'Invalid operator "{operator}"')
```

If the operator isn't in this list, an exception is raised.

For example:

```python
calc('$', 3, 2)
```

raises:

```text
Invalid operator "$"
```

We use `operator.lower()` at the beginning:

```python
operator = operator.lower()
```

This makes the aliases case-insensitive.

For example, `ADD`, `Add`, and `add` are all converted to `add`.

## 3. Check for division by zero

Division by zero is handled before performing the division:

```python
if num2 == 0:
    raise Exception("Division by zero")
```

This is used for both `/` and `%` because modulo by zero is also invalid:

```python
elif operator == '/' or operator == 'div':
    if num2 == 0:
        raise Exception("Division by zero")
    return num1 / num2
```

And:

```python
elif operator == '^' or operator == 'pow':
    return num1 ** num2
```

The `%` operation is checked separately:

```python
elif operator == '%' or operator == 'mod':
    if num2 == 0:
        raise Exception("Division by zero")
    return num1 % num2
```

## 4. Perform the calculation

After all the error checks pass, the function performs the requested operation normally:

```python
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

The important idea is to **validate the inputs before performing the calculation**. If something is invalid, `raise Exception()` immediately stops the function and provides the required error message.
