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

# **Single number**

Currently the `calc` function supports only two numbers operations.

Let's add single number operations for `'+'` and `'-'`,

- `calc('+', 5.4)` -> `5.4`
- `calc('-', 3)` -> `-3`

---

# **Challenge**

Easy

Add support for single number operators for `'+'` and `'-'`.

- Add default value, `None`, to the 3rd argument of `calc`

---

## **Hints**

Hint 1

To add default value, `None`, use,

```python
def calc(op, n1, n2=None):
```

---

# Solution

```python
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
```

# Explanation

The main change is giving the third argument a default value of `None`:

```python
def calc(operator, num1, num2=None):
```

This means that `num2` is optional. If the user doesn't provide a third argument, `num2` will automatically be `None`.

For example:

```python
calc('+', 5.4)
```

is equivalent to:

```python
calc('+', 5.4, None)
```

## 1. Validate the first number

The first number must still be an `int` or `float`:

```python
if not isinstance(num1, (int, float)):
    raise Exception(f'Invalid number "{num1}"')
```

## 2. Validate the second number only when it exists

Because `num2` can now be `None`, we need to make sure we don't treat `None` as an invalid number:

```python
if num2 is not None and not isinstance(num2, (int, float)):
    raise Exception(f'Invalid number "{num2}"')
```

The condition checks whether `num2` is not `None` before checking its type.

## 3. Handle single-number operations

We check whether the user provided only one number:

```python
if num2 is None:
```

For `+`, the number stays unchanged:

```python
if operator == '+' or operator == 'add':
    return num1
```

For `-`, we return the negative version of the number:

```python
elif operator == '-' or operator == 'sub':
    return -num1
```

Therefore:

```python
calc('+', 5.4)  # 5.4
calc('-', 3)    # -3
```

If a single number is provided with an operator that requires two numbers, such as `*` or `/`, an exception is raised:

```python
else:
    raise Exception(f'Invalid operator "{operator}"')
```

## 4. Keep the existing two-number operations

If `num2` is provided, the function continues to perform the normal two-number calculations:

```python
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

So the function now supports both single-number and two-number operations:

```python
calc('+', 5.4)       # 5.4
calc('-', 3)         # -3

calc('+', 1, 3)      # 4
calc('-', 1, 3)      # -2
calc('*', 2, 3)      # 6
calc('/', 1, 4)      # 0.25
calc('^', 2, 3)      # 8
calc('%', 10, 3)     # 1
```

The key idea is using `None` as the default value for `num2` to determine whether the function should perform a **single-number** or **two-number** operation.

# **Basic structure**

The next step is to evaluate a list of expressions.

The basic structure is:

```python
[op, num1, num2]
```

Some examples:

```python
['+', 1, 2]      ->  calc('+', 1, 2)
['*', 3, 2]      ->  calc('*', 3, 2)
['/', 5.3, 0]    ->  calc('/', 5.3, 0)
```


# **Challenge**

Easy

Create function `eval` which gets a basic structure, a list as described above, and returns the calculation result.

Use the `calc` function you created!

---

# Solution

```python
def eval(expression):
    operator, num1, num2 = expression
    return calc(operator, num1, num2)
```

# Explanation

The `eval` function receives a list containing three values:

```python
[op, num1, num2]
```

For example:

```python
['+', 1, 2]
```

The first value is the operator, the second value is the first number, and the third value is the second number.

We unpack the list into three variables:

```python
operator, num1, num2 = expression
```

For:

```python
['+', 1, 2]
```

the variables become:

```python
operator = '+'
num1 = 1
num2 = 2
```

Then we pass these values directly to the `calc` function:

```python
return calc(operator, num1, num2)
```

This allows us to reuse all the functionality and error handling that we already implemented in `calc`.

For example:

```python
eval(['+', 1, 2])      # 3
eval(['*', 3, 2])      # 6
eval(['/', 5.3, 0])    # raises "Division by zero"
```

The main idea is that `eval` acts as a simple interface for a list-based expression: it **unpacks the list** and then **passes its values to `calc`**.

# **Recursive structure**

The real power of the structure we saw last lesson comes with **recursion**.

Consider calculation with more than one operator, for example:

- `2 + 3 * 4 + 5`

There is an order according to math rules, first we need to calculate `3 * 4` and then all the rest.

The following calculation will be formatted into recursive structure in the possible ways:

- `['+', ['+', 2, ['*', 3, 4]], 5]`
- `['+', 2, ['+', 5, ['*', 3, 4]]]`
- `['+', 5, ['+', ['*', 3, 4], 2]]`

Notice that the deepest simple structure is always `['*', 3, 4]` which is the first to calculate. Also note that everything is the basic structure `[op, num1, num2]`.

Some more examples of calculations to recursive structure:

- `2 - 3` -> `['-', 2, 3]`
- `1 - 2 + 3` -> `['+', ['-', 1, 2], 3]`
- `1 * 2 - 3` -> `['-', ['*', 1, 2], 3]`
- `2.3 + 3 / 4.2 - 2` -> `['-', ['+', 2.3, ['/', 3, 4.2]], 2]`

---

# **Challenge**

Medium

Upgrade the `eval` function to support recursive structures as described above.

Notes:

- Call `calc` when the structure is a simple structure, with an operator and **two numbers**.
- Call `eval` recursively if one of the arguments is another structure (list).

---

## **Hints**

Hint 1

To check if `val` is a `list`, use:

```python
isinstance(val, list)
```

This is also the way to determine if one of the arguments is another structure (list) and call `eval` recursively with **this argument**.

---

# Solution

```python
def eval(expression):
    operator, num1, num2 = expression

    if isinstance(num1, list):
        num1 = eval(num1)

    if isinstance(num2, list):
        num2 = eval(num2)

    return calc(operator, num1, num2)
```

# Explanation

The `eval` function receives a structure containing an operator and two arguments:

```python
operator, num1, num2 = expression
```

For example:

```python
['+', ['-', 5, 2], 3]
```

After unpacking:

```python
operator = '+'
num1 = ['-', 5, 2]
num2 = 3
```

The important part is that `num1` is a list, which means it is another calculation that needs to be evaluated first.

## 1. Check if the first argument is a list

```python
if isinstance(num1, list):
    num1 = eval(num1)
```

If `num1` is a list, we call `eval()` again with that list.

For example:

```python
eval(['-', 5, 2])
```

returns:

```python
3
```

So `num1` becomes `3`.

## 2. Check if the second argument is a list

We do the same thing for `num2`:

```python
if isinstance(num2, list):
    num2 = eval(num2)
```

This allows either argument to contain another nested calculation.

## 3. Use `calc` when both arguments are numbers

After recursively evaluating any nested lists, `num1` and `num2` are numbers.

We can then call the `calc` function:

```python
return calc(operator, num1, num2)
```

This follows the challenge requirement to use `calc` for the actual calculation.

## Example

Consider:

```python
eval(['+', ['-', 5, 2], 3])
```

The structure represents:

```text
(5 - 2) + 3
```

First, `eval` sees that `num1` is a list:

```python
['-', 5, 2]
```

So it recursively evaluates it:

```python
eval(['-', 5, 2])
```

This calls:

```python
calc('-', 5, 2)
```

which returns:

```python
3
```

The original expression is now effectively:

```python
calc('+', 3, 3)
```

which returns:

```python
6
```

Therefore:

```python
eval(['+', ['-', 5, 2], 3])  # 6
```

The key idea is that **`eval` handles the structure, while `calc` performs the actual calculation**. Whenever `eval` encounters a nested list, it calls itself recursively until it reaches the deepest simple structure. That deepest calculation is evaluated first, and its result is then passed back up to the previous level.

# **Single number operator**

As we discussed in previous lesson we can add support to single number operator and not a pair.

This is some examples with `eval`,

- `eval(['-', 4])` -> `-4`
- `eval(['+', 4, ['-', 4]])` -> `0`
- `eval(['*', ['+', 4], ['-', 4]])` -> `-16`


# **Challenge**

Easy

Add support for single number operator for the `eval` function.


## **Hints**

Hint 1


Add separation between the length of the list,

```python
def eval(lst):
    if len(lst) == 2:
        # Handle single number operator
    elif len(lst) == 3:
        # Handle two numbers operator (regular)
```

---

# Solution

```python
def eval(lst):
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
```

# Explanation

The `eval` function needs to support both **single-number** and **two-number** operations.

We can determine which type of operation we have by checking the length of the list:

```python
if len(lst) == 2:
```

A list with two elements represents a single-number operation:

```python
['-', 4]
```

We unpack the list:

```python
operator, num1 = lst
```

Then we check if `num1` is another list:

```python
if isinstance(num1, list):
    num1 = eval(num1)
```

If it is a nested structure, we recursively call `eval()` to calculate it first.

Finally, we pass the operator and number to `calc`:

```python
return calc(operator, num1)
```

Since `calc` already supports single-number operations, it can handle `+` and `-`.

For example:

```python
eval(['-', 4])
```

calls:

```python
calc('-', 4)
```

and returns:

```python
-4
```

For a list with three elements:

```python
elif len(lst) == 3:
```

we have the regular two-number structure:

```python
[operator, num1, num2]
```

We unpack it:

```python
operator, num1, num2 = lst
```

Then we check both arguments for nested lists:

```python
if isinstance(num1, list):
    num1 = eval(num1)

if isinstance(num2, list):
    num2 = eval(num2)
```

This allows us to handle recursive structures such as:

```python
eval(['+', 4, ['-', 4]])
```

The inner structure:

```python
['-', 4]
```

is evaluated first:

```python
calc('-', 4)
```

which gives:

```python
-4
```

The outer calculation then becomes:

```python
calc('+', 4, -4)
```

which returns:

```python
0
```

The same logic works when both arguments are nested:

```python
eval(['*', ['+', 4], ['-', 4]])
```

The two nested expressions are evaluated first:

```python
['+', 4]  ->  4
['-', 4]  ->  -4
```

Then the outer calculation becomes:

```python
calc('*', 4, -4)
```

which returns:

```python
-16
```

The key idea is to **use `len(lst)` to determine whether the expression has one or two operands**, and then use recursion whenever an operand is itself a list. Finally, `calc` performs the actual calculation.

# **Handling errors**

Currently `eval` is not considering invalid input. The possible errors are:

- Not a list as input.
- Wrong size of list, only acceptable sizes are 2 and 3.

---

# **Challenge**

Easy

Add exception handling for the above errors.

Some examples of the error messages by calls:

- `eval('not a list')` -> `Failed to evaluate "not a list"`
- `eval([])` -> `Failed to evaluate "[]"`
- `eval(['+', 2, 3, 4])` -> `Failed to evaluate "['+', 2, 3, 4]"`
- `eval(5)` -> `Failed to evaluate "5"`

---

# Solution

```python
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
```

# Explanation

The first thing we need to do is validate the input before trying to unpack or evaluate it.

We check whether `lst` is actually a list:

```python
isinstance(lst, list)
```

We also need to make sure that the list has either **2 or 3 elements**, because these are the only valid structures supported by `eval`.

We combine both checks:

```python
if not isinstance(lst, list) or len(lst) not in [2, 3]:
    raise Exception(f'Failed to evaluate "{lst}"')
```

The condition is true when either:

- `lst` is not a list, or
- the list does not contain exactly 2 or 3 elements.

If either case occurs, we raise an exception with the required message:

```python
raise Exception(f'Failed to evaluate "{lst}"')
```

For example:

```python
eval('not a list')
```

raises:

```text
Failed to evaluate "not a list"
```

And:

```python
eval([])
```

raises:

```text
Failed to evaluate "[]"
```

Similarly:

```python
eval(['+', 2, 3, 4])
```

raises:

```text
Failed to evaluate "['+', 2, 3, 4]"
```

After the input passes the validation, we can safely check the length of the list.

If the list has 2 elements:

```python
if len(lst) == 2:
```

it represents a single-number operation:

```python
['-', 4]
```

We unpack it:

```python
operator, num1 = lst
```

If `num1` is another list, we evaluate it recursively:

```python
if isinstance(num1, list):
    num1 = eval(num1)
```

Then we use `calc` to perform the operation:

```python
return calc(operator, num1)
```

If the list has 3 elements:

```python
elif len(lst) == 3:
```

it represents the regular two-number structure:

```python
['+', 2, 3]
```

We unpack it:

```python
operator, num1, num2 = lst
```

Then we recursively evaluate either argument if it is a list:

```python
if isinstance(num1, list):
    num1 = eval(num1)

if isinstance(num2, list):
    num2 = eval(num2)
```

Finally, we pass the evaluated values to `calc`:

```python
return calc(operator, num1, num2)
```

The important idea is to **validate the structure before processing it**. `eval` only accepts lists with exactly 2 or 3 elements. Once the input is valid, the function can continue with the existing recursive evaluation logic.

# **Basic operators**

The next step is to struct list into our basic structure.

Consider the calculation, 1 + 2 + 3, first we transform it into the list - `[1, '+', 2, '+', 3]` and then we **struct** it into what our `eval` function get - `['+',  ['+', 1, 2], 3]`.

In this step we only care about structuring the list into the format the `eval` function get.

Examples:

- `[4.5, '-', 3]`  ->  `['-', 4.5, 3]`
- `[4.5, '-', 3, '+', 2]`  ->  `['+', ['-', 4.5, 3], 2]`
- `[1, 'sub', 2, 'add', 3, '+', 4]`  ->  `['+', ['add', ['sub', 1, 2], 3], 4]`


# **Challenge (2 Solutions Below)**

Medium

Create the function `struct` which gets list in the above format and returns the format applicable to the `eval` function.

Currently deal only with basic operators `'+'` and `'-'`.


## **Hints**

Hint 1


Start from dealing with [num1, op, num2] formats and then move to the other ones.


Hint 2


change the input on the go,

1. `struct([1, '+', 2, '+', 3, '+', 4])`
2. `[1, '+', 2, '+', 3, '+', 4]`
3. `[['+', 1, 2], '+', 3, '+', 4]`
4. `[['+', ['+', 1, 2], 3], '+', 4]`
5. `['+', ['+', ['+', 1, 2], 3], 4]`

Use while loop and iterate over the list and **search** for the operators `'+'` or `'-'`.

---

## Solution 1

```python
def struct(lst):
    while len(lst) > 1:
        for i in range(1, len(lst) - 1):
            if lst[i] in ['+', 'add'] or lst[i] in ['-', 'sub']:
                # Replace 3 elements (left, op, right) with 1 nested prefix list
                lst[i - 1:i + 2] = [[lst[i], lst[i - 1], lst[i + 1]]]
                break

    return lst[0]
```

### Explanation

### How `struct()` Collapses Linear Expressions

The `struct` function converts a flat list of operations—such as `[1, 'sub', 2, 'add', 3]`—into a nested prefix structure like `['add', ['sub', 1, 2], 3]` so `eval()` can process it recursively.

### Code Implementation

def struct(lst):
    while len(lst) > 1:
        for i in range(1, len(lst) - 1):
            if lst[i] in ['+', 'add'] or lst[i] in ['-', 'sub']:
                # Replace 3 elements (left, op, right) with 1 nested prefix list
                lst[i - 1:i + 2] = [[lst[i], lst[i - 1], lst[i + 1]]]
                break  # Exit for-loop immediately after modifying lst

    return lst[0]

---

### Step-by-Step Execution Mechanics

1. Outer Loop (`while len(lst) > 1`):
   - Controls the global process. It keeps running as long as there are multiple items in `lst`.
   - Every time a triplet is collapsed, `len(lst)` shrinks by 2.

2. Operator Search (`for i in range(...)`):
   - Scans the list from left to right to locate the first valid operator (`+`, `-`, `add`, or `sub`).

3. In-Place Slice Replacement (`lst[i - 1:i + 2] = [...]`):
   - Target Range: `i - 1:i + 2` targets 3 elements:
     * `lst[i - 1]` -> Left number/expression
     * `lst[i]` -> Operator
     * `lst[i + 1]` -> Right number/expression
   - Replacement: `[[lst[i], lst[i - 1], lst[i + 1]]]` creates the prefix triplet `[operator, left, right]`.
   - Double Brackets `[[...]]`: Necessary for slice assignment so Python replaces all 3 original items with a single nested list object.

4. Loop Reset (`break`):
   - Calling `break` immediately stops the `for` loop after modifying `lst`.
   - This prevents index errors or processing shifted elements, forcing the `while` loop to re-evaluate the updated list from index 0.

5. Final Unwrapping (`return lst[0]`):
   - When `len(lst) == 1`, the outer list contains only one item: your fully formatted prefix tree. Returning `lst[0]` extracts that inner structure for `eval()`.

---

### Execution Trace Example

For input `[1, 'sub', 2, 'add', 3]`:

Iteration | State of `lst` | Operation Performed | `len(lst)`
--- | --- | --- | ---
Start | [1, 'sub', 2, 'add', 3] | Initial list | 5
Pass 1 | [['sub', 1, 2], 'add', 3] | Collapses `1, 'sub', 2` at indices `0:3` | 3
Pass 2 | [['add', ['sub', 1, 2], 3]] | Collapses `['sub', 1, 2], 'add', 3` at indices `0:3` | 1
Finish | ['add', ['sub', 1, 2], 3] | Returns `lst[0]` | —


## Solution 2

```python
def struct(lst):

    while len(lst) > 1:

        num1 = lst[0]

        op = lst[1]

        num2 = lst[2]

        new_structure = [op, num1, num2]

        lst[0:3] = [new_structure]

    return lst[0]
```

### Explanation

This solution follows the same basic idea, but it is simpler because it doesn't use a `for` loop to search for the operator.

We always work with the **first three elements**.

For example:

```python
[1, '+', 2, '+', 3]
```

First:

```python
num1 = lst[0]
```

gives:

```python
num1 = 1
```

Then:

```python
op = lst[1]
```

gives:

```python
op = '+'
```

And:

```python
num2 = lst[2]
```

gives:

```python
num2 = 2
```

We then create the required structure:

```python
new_structure = [op, num1, num2]
```

which gives:

```python
['+', 1, 2]
```

Then:

```python
lst[0:3] = [new_structure]
```

replaces the first three elements:

```python
[1, '+', 2]
```

with one element:

```python
['+', 1, 2]
```

So:

```python
[1, '+', 2, '+', 3]
```

becomes:

```python
[['+', 1, 2], '+', 3]
```

The `while` loop continues doing the same thing until only one element remains.

Finally:

```python
lst
```

looks like:

```python
[['+', ['+', 1, 2], 3]]
```

and:

```python
return lst[0]
```

returns:

```python
['+', ['+', 1, 2], 3]
```


### Difference between the two solutions

**Solution 1** follows the hint exactly: it uses a `while` loop, iterates over the list with a `for` loop, and searches for `'+'` or `'-'`.

**Solution 2** is shorter because it assumes we can always process the first three elements. It doesn't need to search for the operator.

Both solutions use the same main idea:

```text
[num1, op, num2]
        ↓
[op, num1, num2]
```

and repeat this process until the entire expression has been transformed into the recursive format required by `eval`.

# **Level one operators**

As we discussed before there is an order in math.

The operators `'*'`, `'/'` and `'%'` calculated before `'+'` and `'-'`.

In this course we call to the operators `'*'`, `'/'` and `'%'` - **level one operators**.

And the operators `'+'` and `'-'` - **level two operators**.



# **Challenge**

Easy

Currently struct only supports level two operators.

Your task is to add support for level one operators for `struct`.

Make sure the order of calculations is taking place!

Examples:

- `struct([3, '*', 2])`  ->  `['*', 3, 2]`
- `struct([1, '+', 2, 'mul', 3])`  ->  `['+', 1, ['mul', 2, 3]]`
- `struct([2, 'mod', 3, '-', 4, '/', 5.2])`  ->  `['-', ['mod', 2, 3], ['/', 4, 5.2]]`



## **Hints**

Hint 1



First go over all the **level one operators** and then the **level two operators**.



# Solution

```python
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
```

# Explanation

The main purpose of this solution is to make `struct` respect the mathematical order of operations.

We have two groups of operators:

```python
operators_high = ['*', '/', '%', 'mul', 'div', 'mod']
```

These are the **level one operators**, so they must be processed first.

```python
operators_low = ['+', 'add', '-', 'sub']
```

These are the **level two operators**, so they are processed after all level one operators have been handled.

## 1. Continue until one structure remains

```python
while len(lst) > 1:
```

We repeatedly restructure the list until it contains only one element.

For example:

```python
[1, '+', 2, 'mul', 3]
```

will eventually become:

```python
[['+', 1, ['mul', 2, 3]]]
```

and then:

```python
return lst[0]
```

returns:

```python
['+', 1, ['mul', 2, 3]]
```

## 2. Check whether a level one operator exists

```python
has_high = any(item in operators_high for item in lst)
```

`any()` checks whether **at least one** element in `lst` is a level one operator.

For example:

```python
lst = [1, '+', 2, 'mul', 3]
```

contains `'mul'`, which is a level one operator.

Therefore:

```python
has_high
```

is:

```python
True
```

This tells us that we must process the level one operator before processing `'+'`.

## 3. Iterate through the list

```python
for i in range(1, len(lst) - 1):
```

We start at index `1` because an operator needs an element before it and an element after it.

For:

```python
[1, '+', 2, 'mul', 3]
```

the indexes are:

```text
index:  0    1    2     3    4
        1   '+'   2    mul   3
```

## 4. Process level one operators first

```python
if has_high and lst[i] in operators_high:
```

If a level one operator exists, we look for it and process it first.

For:

```python
[1, '+', 2, 'mul', 3]
```

we find:

```python
'mul'
```

and restructure:

```python
[2, 'mul', 3]
```

into:

```python
['mul', 2, 3]
```

So the whole list becomes:

```python
[1, '+', ['mul', 2, 3]]
```

Notice that `'+'` was **not** processed yet.

This is exactly what we want because multiplication has higher priority than addition.

## 5. Why `break` is important

After restructuring one operation:

```python
lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
```

we use:

```python
break
```

This exits the `for` loop.

Then the `while` loop starts again and checks the newly modified list.

This is important because the indexes and length of `lst` have changed.

For example:

```python
[1, '+', 2, 'mul', 3]
```

becomes:

```python
[1, '+', ['mul', 2, 3]]
```

Then we start searching again from the beginning.

## 6. Process level two operators

The `elif` handles level two operators:

```python
elif not has_high and lst[i] in operators_low:
```

This part is reached only when there are **no level one operators left**.

For example, after processing:

```python
[1, '+', 2, 'mul', 3]
```

we have:

```python
[1, '+', ['mul', 2, 3]]
```

There are no level one operators left, so:

```python
has_high
```

is now:

```python
False
```

The code can therefore process `'+'`:

```python
[1, '+', ['mul', 2, 3]]
```

becomes:

```python
[['+', 1, ['mul', 2, 3]]]
```

Now the list has one element, so the `while` loop stops.

## 7. Why `lst[0]` is returned

At the end, `lst` contains one element:

```python
[['+', 1, ['mul', 2, 3]]]
```

The complete structure is that single element:

```python
['+', 1, ['mul', 2, 3]]
```

Therefore:

```python
return lst[0]
```

returns the structure required by `eval`.

## Example 1

```python
struct([3, '*', 2])
```

There is a level one operator:

```python
'*'
```

So:

```python
[3, '*', 2]
```

becomes:

```python
[['*', 3, 2]]
```

Finally:

```python
return lst[0]
```

returns:

```python
['*', 3, 2]
```

## Example 2

```python
struct([1, '+', 2, 'mul', 3])
```

First, `'mul'` is processed because it is a level one operator:

```python
[1, '+', 2, 'mul', 3]
```

becomes:

```python
[1, '+', ['mul', 2, 3]]
```

There are no level one operators left, so `'+'` is processed:

```python
[1, '+', ['mul', 2, 3]]
```

becomes:

```python
[['+', 1, ['mul', 2, 3]]]
```

The final result is:

```python
['+', 1, ['mul', 2, 3]]
```

## Example 3

```python
struct([2, 'mod', 3, '-', 4, '/', 5.2])
```

The level one operators are:

```text
'mod'
'/'
```

They are processed before `'-'`.

The result becomes:

```python
['-', ['mod', 2, 3], ['/', 4, 5.2]]
```

This correctly represents the mathematical order:

```text
2 mod 3
```

and:

```text
4 / 5.2
```

are calculated before the subtraction.

### Key idea

The important part of this solution is:

```python
has_high = any(item in operators_high for item in lst)
```

followed by:

```python
if has_high and lst[i] in operators_high:
```

and:

```python
elif not has_high and lst[i] in operators_low:
```

This guarantees that **level one operators are always processed before level two operators**, so the resulting structure preserves the correct order of calculations.

# **Functions operators**

**Function operators** are `'^'` (more to come?).

The function operators calculated before **all** the other operators.



# **Challenge**

Easy

Add support for function operators in `struct`.

---

## Solution

```python
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
```

## Explanation

The main change in this version is that we now have **three levels of operators**:

```python
operators_power = ['^', '**', 'pow']
```

These are the **function operators**, and they have the highest priority.

Then:

```python
operators_high = ['*', '/', '%', 'mul', 'div', 'mod']
```

These are the level one operators.

Finally:

```python
operators_low = ['+', 'add', '-', 'sub']
```

These are the level two operators.

So the order is:

```text
Function operators
        ↓
Level one operators
        ↓
Level two operators
```

### 1. Check for function operators

```python
has_power = any(item in operators_power for item in lst)
```

This checks whether the list contains a function operator such as:

```python
'^'
```

or:

```python
'**'
```

or:

```python
'pow'
```

If one exists, we must process it **before anything else**.

### 2. Why do we search from right to left?

When we find a function operator, we use:

```python
for i in range(len(lst)-2, 0, -1):
```

This means we start searching from the **right side of the list** and move toward the left.

This is important for power operations because exponentiation is evaluated from **right to left**.

For example:

```python
2 ^ 3 ^ 2
```

is interpreted as:

```text
2 ^ (3 ^ 2)
```

rather than:

```text
(2 ^ 3) ^ 2
```

So we need to process the rightmost `^` first.

For example:

```python
[2, '^', 3, '^', 2]
```

First we find the second `^`:

```python
[2, '^', 3, '^', 2]
             ↑
```

and restructure:

```python
[2, '^', ['^', 3, 2]]
```

Then the remaining `^` is processed:

```python
[['^', 2, ['^', 3, 2]]]
```

Finally:

```python
return lst[0]
```

returns:

```python
['^', 2, ['^', 3, 2]]
```

This preserves the correct order of exponentiation.

### 3. Create the nested structure

The same slice assignment is used:

```python
lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
```

It takes:

```python
[num1, op, num2]
```

and replaces it with:

```python
[op, num1, num2]
```

as one element inside the list.

For example:

```python
[2, '^', 3]
```

becomes:

```python
[['^', 2, 3]]
```

### 4. The `reduced` variable

```python
reduced = False
```

At the beginning of every `while` iteration, we assume that nothing was changed.

When an operator is found and processed:

```python
reduced = True
```

This tells us that the list was successfully reduced.

For example:

```python
[2, '^', 3]
```

has three elements.

After restructuring:

```python
[['^', 2, 3]]
```

it has one element.

So the list was reduced.

### 5. Why do we check `reduced`?

At the end:

```python
if not reduced:
    break
```

If no operator was found, `reduced` remains:

```python
False
```

and we break out of the `while` loop.

This prevents the function from getting stuck in an infinite loop when the list cannot be reduced any further.

### 6. If there are no function operators

If:

```python
has_power
```

is `False`, we move to:

```python
elif has_high:
```

So level one operators such as:

```python
'*'
'/'
'%'
```

are processed next.

For example:

```python
[1, '+', 2, '*', 3]
```

has no power operator, but it has a level one operator:

```python
'*'
```

So we process `*` first:

```python
[1, '+', ['*', 2, 3]]
```

Then there is no level one operator left, so we can process `+`:

```python
[['+', 1, ['*', 2, 3]]]
```

The final result is:

```python
['+', 1, ['*', 2, 3]]
```

### 7. Finally, process level two operators

If there are no function operators and no level one operators, we reach:

```python
elif not has_high:
```

and search for:

```python
operators_low
```

which contains:

```python
['+', 'add', '-', 'sub']
```

These are processed last.

---

## Example

Consider:

```python
[2, '^', 3, '*', 4, '+', 5]
```

The function operator `^` has the highest priority.

First:

```python
[2, '^', 3, '*', 4, '+', 5]
```

becomes:

```python
[['^', 2, 3], '*', 4, '+', 5]
```

Now there is no function operator, so `*` is processed:

```python
[[ '*', ['^', 2, 3], 4], '+', 5]
```

Finally, `+` is processed:

```python
[['+', ['*', ['^', 2, 3], 4], 5]]
```

The final result is:

```python
['+', ['*', ['^', 2, 3], 4], 5]
```

This structure correctly represents:

```text
(2 ^ 3) * 4 + 5
```

### Key idea

The solution now respects the priority of all three operator levels:

```text
'^', '**', 'pow'
        ↓
'*', '/', '%', 'mul', 'div', 'mod'
        ↓
'+', 'add', '-', 'sub'
```

And for the function operators specifically, the search is performed **from right to left**:

```python
for i in range(len(lst)-2, 0, -1):
```

so expressions involving multiple powers are structured correctly according to the right-to-left nature of exponentiation.

# **Single number operator**

As we saw before we handle special case when a single number operator, `'+'` or `'-'`.

This happen **only** when the list we get is of size 2!



# **Challenge**

Easy

Add support for single number operator in `struct`.



## **Hints**

Hint 1



If the `len` of the input is `2` return the input!

---

## Solution

```python
def struct(lst):
    operators_high = ['*', '/', '%', 'mul', 'div', 'mod']
    operators_low = ['+', 'add', '-', 'sub']
    operators_power = ['^', '**', 'pow']

    if len(lst) == 2:
        return lst

    while len(lst) > 1:
        has_high = any(item in operators_high for item in lst)
        has_power = any(item in operators_power for item in lst)
        reduced = False

        if has_power:
            for i in range(len(lst) - 2, 0, -1):
                if lst[i] in operators_power:
                    lst[i - 1:i + 2] = [[lst[i], lst[i - 1], lst[i + 1]]]
                    reduced = True
                    break

        elif has_high:
            for i in range(1, len(lst) - 1):
                if lst[i] in operators_high:
                    lst[i - 1:i + 2] = [[lst[i], lst[i - 1], lst[i + 1]]]
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
```

## Explanation

A **single number operator** is an operator that works with only one number.

For example:

```python
['+', 5]
```

means:

```text
+5
```

and:

```python
['-', 5]
```

means:

```text
-5
```

Normally, our `struct` function works with three elements:

```python
[num1, op, num2]
```

and transforms them into:

```python
[op, num1, num2]
```

But a single number operator has only two elements:

```python
[op, num]
```

For example:

```python
['-', 5]
```

There is no third element to process.

### Handling the special case

The hint tells us:

```python
if len(lst) == 2:
    return lst
```

So we add this at the beginning of the function:

```python
if len(lst) == 2:
    return lst
```

If the input is:

```python
['+', 5]
```

then:

```python
len(lst) == 2
```

is `True`.

Therefore, the function immediately returns:

```python
['+', 5]
```

Likewise:

```python
struct(['-', 5])
```

returns:

```python
['-', 5]
```

This is already in the correct format for `eval`, so there is no need to restructure anything.

### Why must we handle it before the `while` loop?

The normal restructuring code expects three elements:

```python
lst[i - 1]
lst[i]
lst[i + 1]
```

But with:

```python
['-', 5]
```

there is no `lst[i + 1]` that represents a second number.

So we handle the special case first:

```python
if len(lst) == 2:
    return lst
```

and avoid entering the normal restructuring process.

### Examples

```python
struct(['+', 5])
```

returns:

```python
['+', 5]
```

And:

```python
struct(['-', 3])
```

returns:

```python
['-', 3]
```

The important idea is:

> When `lst` has exactly two elements, it is already in the correct `eval` format, so we simply return it without restructuring.

# Handling Errors
As always raise error in case the input cannot be structured.

## Challenge

**Difficulty:** Easy

As always, raise an error in case the input cannot be structured.

### Examples

```python
struct(4)
# Exception: Failed to structure "4"

struct(['+'])
# Exception: Failed to structure "['+']"

struct([2, '+', 3, '+'])
# Exception: Failed to structure "[2, '+', 3, '+']"

struct([2, 'mul', '+'])
# ['mul', 2, '+']
```

## Solution

```python
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
        has_power = any(item in operators_power for item in lst)
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

        else:
            for i in range(1, len(lst) - 1):
                if lst[i] in operators_low:
                    lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
                    reduced = True
                    break

        if not reduced:
            raise Exception(f'Failed to structure "{lst}"')

    return lst[0]
```

## Explanation

### 1. Check the input type

```python
if not isinstance(lst, list):
    raise Exception(f'Failed to structure "{lst}"')
```

The function expects a list. If the input is not a list, it raises an error.

### 2. Handle a two-item list

```python
if len(lst) == 2:
    return lst
```

A two-item list is returned as-is, matching the challenge's expected behavior.

### 3. Check the list length

```python
if len(lst) <= 1 or len(lst) % 2 == 0:
    raise Exception(f'Failed to structure "{lst}"')
```

- `len(lst) <= 1` rejects lists with zero or one item.
- `len(lst) % 2 == 0` rejects lists with an even number of items.

A normal binary expression needs at least three items, such as `[2, '+', 3]`, and alternates between operands and operators.

### 4. Process operators by precedence

The function processes operators in this order:

1. Powers: `^`, `**`, `pow`
2. Multiplication and division: `*`, `/`, `%`, `mul`, `div`, `mod`
3. Addition and subtraction: `+`, `add`, `-`, `sub`

Power operators are processed from right to left. Other operators are processed from left to right.

### 5. Group the expression

```python
lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
```

This replaces three elements with one nested list.

For example:

```python
[2, 'mul', 3]
```

becomes:

```python
[['mul', 2, 3]]
```

### 6. Detect when no progress is possible

```python
if not reduced:
    raise Exception(f'Failed to structure "{lst}"')
```

If no recognized operator can be processed, the function raises an error instead of continuing indefinitely.

### 7. Return the result

```python
return lst[0]
```

When the expression has been reduced to one nested structure, the function returns it.

**Note:** This solution checks basic list structure and whether recognized operators can be processed. It does not fully validate that every operand is a valid number or expression.

# Structure for All

## Description

Currently, we are structuring all the supported operators, but we also want to structure “typos” so we can get the right error message from the `calc` function.

For example:

```python
struct([2, '?', 3])  # -> ['?', 2, 3]
```

Currently:

```python
struct([2, '?', 3])  # -> [2, '?', 3]
```

Notice that `'?'` should be in the operator place even though it is not a real operator we support.

## Challenge

**Difficulty:** Medium

Add support for structuring all kinds of operators in `struct`, including operators that are not supported yet or are typos.

## Hints

### Hint 1

Find the unsupported operators by looking for items that are not numbers (`int` or `float`).

### Hint 2

Also make sure not to count `list` as this kind of operator.

## Solution

```python
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
```

## Explanation

### 1. Define the operator groups

The operators are separated into three groups:

- `operators_power`: power operators such as `^`, `**`, and `pow`.
- `operators_high`: multiplication and division operators.
- `operators_low`: addition and subtraction operators.

This allows the function to structure expressions according to operator precedence.

### 2. Validate the input

```python
if not isinstance(lst, list):
    raise Exception(f'Failed to structure "{lst}"')
```

The function expects a list. If the input is not a list, it raises an exception.

```python
if len(lst) == 2:
    return lst

if len(lst) <= 1 or len(lst) % 2 == 0:
    raise Exception(f'Failed to structure "{lst}"')
```

A two-item list is returned as-is. Other expressions must contain at least three items and have an odd number of items.

### 3. Detect supported operators

```python
has_high = any(item in operators_high for item in lst)
has_low = any(item in operators_low for item in lst)
has_power = any(item in operators_power for item in lst)
```

`any()` returns `True` if at least one item in `lst` belongs to the corresponding operator group.

### 4. Detect unsupported operators or typos

```python
has_typo = any(
    not isinstance(item, (int, float, list))
    and item not in (operators_high + operators_low + operators_power)
    for item in lst
)
```

This checks whether the list contains an item that:

- Is not an integer or a float.
- Is not itself a list.
- Is not one of the supported operators.

For example, `'?'` is not a number, list, or supported operator, so it can be treated as an operator for structuring purposes.

### 5. Structure the expression

The function checks operators in precedence order:

1. Power operators.
2. Multiplication and division operators.
3. Addition and subtraction operators.
4. Unsupported operators or typos.

When it finds an operator, it replaces the operator and its two neighboring operands with a nested list:

```python
lst[i-1:i+2] = [[lst[i], lst[i-1], lst[i+1]]]
```

For example:

```python
[2, '?', 3]
```

becomes:

```python
[['?', 2, 3]]
```

The final `return lst[0]` returns the nested structure:

```python
['?', 2, 3]
```

### 6. Raise an exception if no restructuring happens

```python
if not reduced:
    raise Exception(f'Failed to structure "{lst}"')
```

`reduced` becomes `True` when the function successfully restructures part of the list.

If no operator can be processed, it remains `False`, and the function raises an exception rather than continuing the loop without making progress.

## Summary

The main addition is `has_typo`, which detects unsupported operator-like items. This allows `struct` to place typos such as `'?'` in the operator position, so the `calc` function can handle the unsupported operator and produce the appropriate error message.
