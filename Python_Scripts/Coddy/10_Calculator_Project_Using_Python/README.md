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
