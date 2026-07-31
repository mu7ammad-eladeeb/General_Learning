# What is an Exception?

An **Exception** is an error that occurs **during the execution** of a program.

Even if your code is **syntactically correct**, it may encounter an unexpected situation while running (such as invalid operations, missing variables, or running out of memory). When this happens, the Python interpreter **raises an exception** and, unless it is handled, the program stops execution.

---

## Example 1: `TypeError`

```python
a = 10
b = "Hii"

print(a + b)   # TypeError
print("Rest of Code")
```

### Explanation

- Here, we are trying to add an **integer** (`a`) and a **string** (`b`).
- Python does **not** allow addition between different data types.
- For the `+` operator, both operands must be of compatible types.
- Therefore, Python stops execution and raises a **`TypeError`**.
- The line:

```python
print("Rest of Code")
```

is **not executed**.

---

## Example 2: `NameError`

```python
MY_NAME = "Mike"

print(my_name)   # NameError
```

### Explanation

- The variable `MY_NAME` exists.
- However, we are trying to print `my_name`, which has **not** been defined.
- Since Python cannot find a variable with that exact name, it raises a **`NameError`**.

---

## Notes

> **Note 1:** Python is a **case-sensitive** language.

This means:

```python
MY_NAME != my_name
```

They are treated as two completely different variable names.

> **Note 2:** Both example programs are **syntactically correct**.

The errors occur **during execution**, not while parsing the code. Therefore, they are called **Exceptions** rather than syntax errors.

---

## Key Points

- **Exceptions** are errors that occur **during program execution**.
- A program can be **syntactically correct** and still raise exceptions.
- When an exception is not handled, Python **terminates the program**.
- Examples of exceptions:
  - `TypeError`
  - `NameError`
  - `ValueError`
  - `IndexError`
  - `KeyError`
  - `ZeroDivisionError`

# Exception vs Error

There are two types of errors in Python:

1.  **Syntax Error (Compile-Time Error)**
2.  **Exception (Run-Time Error)**

## Syntax Error

If the code you write doesn't follow Python syntax and rules, the
interpreter will raise a **SyntaxError**. These errors cannot be
handled.

**Example:**

``` python
print("Hello World"))
```

The above program raises a **SyntaxError** because of an unmatched
parenthesis. You need to fix it before the program can run successfully.

## Exception

An **Exception** occurs because of logical errors, runtime problems, or
invalid inputs. To avoid sudden termination of a program, exceptions can
be handled using **Exception Handling** concepts.

# try-except

The **try-except** block in Python is used to catch and handle
exceptions.

## Basic Structure

``` python
try:
    statement_1
    # statements that can cause an error
    statement_3
except [ExceptionName]:
    # code for exception handling
```

## How It Works

-   Python executes the code inside the `try` block.
-   If an exception occurs, execution immediately jumps to the `except`
    block.
-   The remaining statements in the `try` block are skipped.
-   If no exception occurs, the entire `try` block executes
    successfully, and the `except` block is skipped.

## try Block

Contains code where an exception may occur.

## except Block

Contains the code that handles the exception if it occurs.

## Example

``` python
try:
    a = int(input())
    b = int(input())
    div = a / b
    print("Division is:", div)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Rest of code")
```

## Explanation

-   The program runs normally if the user enters a non-zero value for
    `b`.
-   If the user enters `0` for `b`, the expression `a / b` raises a
    `ZeroDivisionError`.
-   Control immediately moves to the `except` block, which prints:

``` text
Cannot divide by zero
```

-   After handling the exception, the program continues executing the
    remaining code and prints:

``` text
Rest of code
```

Using `try-except` prevents the program from terminating unexpectedly
when an exception occurs.

# else

We can use optional `else` block with `try-except` statement.

It is useful for code that must be executed if the `try` block does **not** raise an exception.

## Example

```python
try:
    a = 10
    b = "hello"
    result = a + b  # code which can cause exception
except TypeError:
    print("Cannot do addition")  # code to handle exception
else:
    print("Addition performed successfully")  # code to be executed when no exception in try block
```

In the above example, an exception is generated and control goes to the `except` block. Therefore, the `else` block will **not** be executed.

If you set:

```python
b = 20
```

No exception will occur, and the `else` block will be executed.

- **Exception** → `except` block
- **No Exception** → `else` block

> **Note:** Either the `except` block or the `else` block will be executed.

# Finally Block in Python

Finally
There is another optional block which is called finally.
This block is executed under all circumstances. This block runs whether or not the try statement produces an Exception.

```python
try:
    f = open("data.txt", encoding='utf-8')
except FileNotFoundError:
    print("File does not exist")
else:
    print(f.read())
finally:
    print("cleanup activities like closing file")
```
In above example, Exception will be raised if data.txt doesn't exist and except block will be executed.

If file exists, control goes to else block because of no exception and interpreter will read the data. 

Finally block is executed in both cases which will perform cleanup activities, mandatory code, system operations, releasing memory etc

# Challenge
Easy

Write a function to add new key-value pairs into given dictionary. Handle TypeError when user enters mutable keys i.e list and print "Cannot give mutable keys". If key-value added successfully, then print added value for new key. Finally, print a dictionary after operation is done. 

## Solution
```python
data = {
    'John' : 89,
    'Mike' : 91,
    'Angela': 85,
}

def insert_data(key, value):
    try:
        data[key] = value
    except TypeError:
        print("Cannot give mutable keys")
    else:
        print(data[key])
    finally:
        print(data)
```
# Printing Exception Message

```python
f = open("data.txt", encoding='utf-8')
my_data = f.read()
print(my_data)
```

If `data.txt` doesn't exist, `FileNotFoundError` will be raised and below message gets printed on console.

```text
Traceback (most recent call last):
  File "C:/Users/Lenovo/Desktop/example.py", line 1, in <module>
    f = open("data.txt",encoding='utf-8')
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
```

Above message includes:

- Traceback details
- Exception Name
- Exception Message

We can print above details in except block so user will get an idea what happened.

## Syntax

```python
except ExceptionName as object_Name:
    print(object_Name)
```

```python
try:
    f = open("data.txt", encoding='utf-8')
    my_data = f.read()
    print(my_data)
except FileNotFoundError as obj:
    print(obj)
```

If `data.txt` doesn't exist, control goes to except block and Exception message will be stored in `obj` object and it will be printed.

---

# Challenge

**Easy**

You will have list as input. Write a program to sum all elements in a list. If it encounters an exception during summation, it will raise an Exception. Otherwise, it will print summation. The Exception type is `TypeError` and text will be standard message text. (use for loop only and not `sum()`)

## Solution

```python
def summation(my_list):
    try:
        sum1 = 0
        for ele in my_list:
            sum1 = sum1 + ele
    except TypeError as obj:
        print(obj)
    else:
        print(sum1)
```

# Printing Exception Name

## Printing Exception Name

We can print the name of an exception using the exception object's `__class__` attribute.

### Syntax

```python
try:
    # code which can cause exception
except ExceptionName as object_name:
    print(object_name.__class__)
```

Here:
- `object_name` stores the exception object.
- `object_name.__class__` returns the class of the exception (for example, `<class 'TypeError'>`).

---

## Challenge
Easy

You are given a list as input. Write a function `summation(my_list)` that calculates the sum of all elements in the list.

- If all elements are valid numbers, print the total sum.
- If an exception occurs during summation, handle the exception.
- The exception type is **TypeError**.
- Print the exception in the following format:

```text
<class 'TypeError'>:Standard message
```

Use an **f-string** to print the exception.

---

## Hint

Use an f-string to print both the exception class and the exception message.

```python
print(f"{obj.__class__}:{obj}")
```

---

## Solution

```python
def summation(my_list):
    try:
        sum1 = 0
        for ele in my_list:
            sum1 = sum1 + ele
    except TypeError as obj:
        print(f"{obj.__class__}:{obj}")
    else:
        print(sum1)
```

# Handling Multiple Exceptions

Suppose there is a possibility of multiple exceptions in your code. You can handle all exceptions as follows:

```python
try:
    # code which can cause
    # TypeError, ValueError, ZeroDivisionError
except (TypeError, ValueError, ZeroDivisionError) as obj:
    print(obj)
```

If any of the above three exceptions occurs, control goes to the `except` block and the program does not terminate.

## Handle Any Exception

If you are not sure which exception will occur, do not write anything after the `except` keyword.

```python
try:
    # code which can cause
    # TypeError, ValueError, ZeroDivisionError
except:
    print("Something went wrong")
```

The above syntax handles any exception from the `try` block, but you will not have an object to print exception information.

Use the following syntax instead:

```python
try:
    # code which can cause
    # TypeError, ValueError, ZeroDivisionError
except Exception as obj:
    print(obj)
```

The above syntax handles any exception raised in the `try` block, and you can print the exception message using `obj`.

## Challenge

**Easy**

Complete the function `calculator` which takes two integers as arguments and performs division. Handle all causing exceptions and print the standard message. If no exception occurs, print the result using the `else` block.

### Solution

```python
def calculator(n1, n2):
    try:
        div = n1 / n2
    except Exception as obj:
        print(obj)
    else:
        print(div)
```

# sys Module for Information

`exc_info` function from `sys` module prints Exception details.

```python
import sys

try:
    # code which can cause exception
except:
    print(sys.exc_info())
```
## Output:
( class_name, standard_message, traceback_object )

It returns a tuple containing three values as above.

# Challenge
Difficulty: Easy

A function takes a key as argument. Complete function to fetch value for entered key. If key not found in dictionary, KeyError will be raised. Handle it and print exception class name and standard message by using above way. Else, print value in else block.

## Hints
Hint 1: Use Slicing to get class name and standard message

# Solution
```python
import sys

age = {
    'Peter': 23,
    'Lopez': 24,
    'Glenn': 27,
    'Jay': 29
}

def fetch(key):
    try:
        value = age[key]
    except:
        print(sys.exc_info()[0:2])
    else:
        print(value)
```

# Types of Exceptions

There are **two types of Exceptions** in Python:

## 1. Built-in Exceptions

These Exceptions are already available in Python.

**Examples:**
- `EOFError`
- `IndexError`
- `TypeError`
- `ValueError`

## 2. User-defined Exceptions (Custom Exceptions)

These Exceptions are created by programmers.

**Example:**
- Raising an Exception if the user enters an invalid password.

## Remember

Every Exception is actually a **class** in Python inherited from the built-in `BaseException` class.

So, `IndexError` is also a built-in class inherited from `BaseException`.

As soon as an Exception occurs, an **object (instance)** of the raised Exception class is created.

---

## Example

```python
def observe(idx):
    try:
        # A list containing 4 elements.
        data = [10, 20, 30, 40]

        # Tries to access the element at the given index.
        # If idx is outside the valid range (0-3),
        # Python raises an IndexError.
        print(data[idx])

    except Exception as e:
        # 'e' is the exception object created by Python.
        # type(e) shows the class of the exception object.
        print(type(e))

        # mro() stands for Method Resolution Order.
        # It returns a list of classes that Python searches
        # when looking for methods or attributes.
        # Since IndexError inherits from LookupError,
        # LookupError inherits from Exception,
        # Exception inherits from BaseException,
        # and BaseException inherits from object,
        # mro() displays this inheritance chain.
        print(IndexError.mro())
```

### Output

```text
<class 'IndexError'>
[<class 'IndexError'>,
 <class 'LookupError'>,
 <class 'Exception'>,
 <class 'BaseException'>,
 <class 'object'>]
```

### Explanation of Output

- `type(e)` prints:

  ```python
  <class 'IndexError'>
  ```

  This shows that the exception object `e` belongs to the `IndexError` class.

- `IndexError.mro()` prints the inheritance hierarchy of the `IndexError` class:

  - `IndexError` → The actual exception raised.
  - `LookupError` → Parent class of `IndexError`.
  - `Exception` → Base class for most built-in exceptions.
  - `BaseException` → Root class of all Python exceptions.
  - `object` → The root class of all Python classes.

This demonstrates that every built-in exception is a class and ultimately inherits from `BaseException`.

# Raising an Exception

## `raise` Keyword

You can raise any Exception (Built-in or Custom) by using the `raise` keyword.

You can also pass a message inside the raised Exception that describes the problem.

### Syntax

```python
raise ExceptionName(optional_message)
```

### Example

```python
try:
    n = int(input("Enter the number for factorial:"))
    if n < 0:
        raise ValueError("Number cannot be negative")
    # factorial code here
except Exception as obj:
    print(obj)
```

**Explanation:**

In the above example, the `raise` statement is executed if the user enters a number less than `0`. This raises a `ValueError`, and control is transferred to the `except` block. The message `"Number cannot be negative"` is stored in `obj` and printed on the console.

---

# Challenge (Easy)

A function will take a mobile number (`string`) as input.

- Raise `ValueError` if any character is not a digit or if the length is not equal to **12** digits.
- Print `"Invalid"` on the console if an exception is raised.
- Otherwise, print `"valid"`.

## Hint

Use the `isdigit()` method of the `str` class.

### Solution

```python
def contact_details(mobile):
    try:
        if not (mobile.isdigit() and len(mobile) == 12):
            raise ValueError("Invalid")
    except ValueError as obj:
        print(obj)
    else:
        print("valid")
```

# User Defined Exception

## How to Create a User-Defined Exception?

There are three steps:

1. Create an Exception class by inheriting the `Exception` class.
2. Raise the created Exception for a particular condition.
3. Handle that Exception.

---

## Example: Prevent Division by Five

Suppose you want to prevent users from dividing by `5`. If the second number is `5`, a custom Exception should be raised.

### Step 1: Create a Custom Exception Class

```python
class FiveDivisionError(Exception):
    pass
```

`FiveDivisionError` is a custom Exception created by inheriting the `Exception` class.

> **Note:** You can define a constructor to customize the Exception, but in this example, the message is provided in the `raise` statement.

---

### Step 2: Raise the Exception

```python
try:
    a = int(input("1st Number: "))
    b = int(input("2nd Number: "))

    if b == 5:
        raise FiveDivisionError("Cannot divide by five")

    div = a / b
    print("Division:", div)
```

If `b == 5`, the `FiveDivisionError` Exception is raised.

---

### Step 3: Handle the Exception

```python
except Exception as obj:
    print(obj)
```

The `except` block catches the raised Exception and prints its message.

---

# Challenge

## Easy

Age will be passed to the function `access`.

Complete the function so that:

- Print `"Access Denied!"` and stop function execution if `age` is less than `18`.
- Otherwise, print `"Session Created!"`.

Use **Exception handling only** and create a custom Exception named `AccessError`.

---

## Hints

### Hint 1

Print the messages exactly as given in the challenge.

---

# Solution

```python
class AccessError(Exception):
    pass


def access(age):
    try:
        if age < 18:
            raise AccessError("Access Denied!")
    except Exception as e:
        print(e)
    else:
        print("Session Created!")
```

# Exception Handling Exercise-1

## Problem Statement

The signed password for user **`"coddy"`** is **`"12345"`**.

Create a function that takes a password as input from the user. If the entered password does not match the stored password, raise an **`Invalid_Password`** exception with the message:

```text
Invalid password, try again
```

Otherwise, print:

```text
session created
```

The user should be prompted again until the correct password is entered.

---

## Hint

- Use **recursion** to prompt the user again after an incorrect password.

---

## Solution

```python
stored_password = "12345"  # fetched from database (Imagine)

class Invalid_Password(Exception):
    pass

def login():
    try:
        password = input()
        if password != stored_password:
            raise Invalid_Password("Invalid password, try again")
    except Exception as e:
        print(e)
        login()
    else:
        print("session created")
```

---

## Explanation

- The correct password is stored in the variable `stored_password`.
- A custom exception named `Invalid_Password` is created by inheriting from `Exception`.
- The `login()` function reads the password entered by the user.
- If the entered password does not match the stored password, an `Invalid_Password` exception is raised with the message:

  ```text
  Invalid password, try again
  ```

- The exception is caught in the `except` block, where:
  - The error message is printed.
  - The `login()` function is called again (using recursion) to prompt the user for another attempt.
- If no exception occurs, the `else` block executes and prints:

  ```text
  session created
  ```

- This process continues until the user enters the correct password.

  ## Alternative Solution (Using a `while` Loop) -> More Efficient Solution

```python
stored_password = "12345"  # fetched from database (Imagine)

class Invalid_Password(Exception):
    pass

def login():
    while True:
        try:
            password = input()
            if password != stored_password:
                raise Invalid_Password("Invalid password, try again")
        except Exception as obj:
            print(obj)
        else:
            print("session created")
            break
```

### Explanation

- The correct password is stored in the variable `stored_password`.
- A custom exception named `Invalid_Password` is created by inheriting from the `Exception` class.
- The `login()` function uses a `while True` loop to repeatedly prompt the user for a password.
- Inside the `try` block:
  - The user enters a password using `input()`.
  - If the entered password does not match the stored password, an `Invalid_Password` exception is raised with the message:
    ```text
    Invalid password, try again
    ```
- The `except` block catches the exception and prints the error message.
- If no exception occurs, the `else` block executes:
  - It prints:
    ```text
    session created
    ```
  - The `break` statement exits the loop, ending the function.
- Unlike the recursive solution, this approach uses a loop to repeatedly ask for the password, avoiding recursive function calls and making it more efficient for a large number of incorrect attempts.

# Exception Handling Example-2

## Example 1

Let's take an example of bank transactions. We are having multiple custom exceptions.

1. Assume a user's bank account must contain at least **100$**. While making a transaction, if the remaining balance goes below **100$**, an exception should be generated.

2. A user should have a maximum of **3 attempts**. If the user tries for a **fourth attempt**, an exception should be generated and the bank account should be frozen.

> In this example, only the **first case** is implemented. The second case is left as a challenge.

## Step 1: Create a User-Defined Exception Class

```python
class BalanceException(Exception):
    pass
```

## Step 2: Raise the Exception for a Particular Condition

```python
balance = 1000

try:
    amt = float(input("Enter the amount to withdraw:"))

    # Check remaining amount after transaction
    temp = balance - amt

    if temp < 100:
        raise BalanceException("Insufficient balance")

except Exception as obj:
    print(obj)
```

In the above code, a custom exception is raised if the remaining balance goes below **100$**.

## Using the `else` Block

If no exception occurs, the transaction can be completed by updating the balance.

```python
else:
    balance = balance - amt
```

## Using the `finally` Block

Whether an exception occurs or not, we want to print the remaining balance. We can use the `finally` block for that.

```python
finally:
    print("Remaining balance is:", balance)
```

## Challenge

**Medium**

Add another custom exception for the second case and update the given code.

### Hint

- Use **recursion** for the next attempt.
- Use the **`global`** keyword to access global data inside the function.

---

# Solution

```python
balance = 10000   # Imagine it is fetched from database.

class BalanceException(Exception):
    pass

class AttemptException(Exception):
    pass

attempt = 1

def transaction():
    global balance, attempt

    try:
        amt = float(input())

        # Check remaining amount after transaction
        temp = balance - amt

        if temp < 100:
            raise BalanceException("Insufficient balance")

    except Exception as obj:
        print(obj)

        try:
            if attempt == 3:
                raise AttemptException("No more attempts allowed!")

            attempt += 1
            transaction()

        except Exception as e:
            print(e)

    else:
        balance = balance - amt
        print("Transaction is success, Remaining balance is:", balance)
```

## Explanation

- **`BalanceException`** is raised if the withdrawal would reduce the remaining balance below **100$**.
- **`AttemptException`** is raised after **3 failed attempts**, preventing any further transactions.
- The **`attempt`** variable keeps track of the number of failed attempts.
- The **`global`** keyword allows the function to update the global variables `balance` and `attempt`.
- **Recursion** is used to give the user another chance after an invalid transaction.
- If no exception occurs, the transaction is completed and the updated balance is displayed.

# Exception Handling Example-3

## Exercise - 03

Create a function `calculator()` that handles both **user-defined (custom)** and **built-in** exceptions.

The function takes a mathematical expression (string) as input.

### Requirements

The expression must follow this format:

```text
operand operator operand
```

Example:

```text
6 * 5
```

---

## Exception Cases

### 1. Invalid Expression

The expression must contain **two operands and one operator**, separated by spaces.

Example of a valid expression:

```text
6 * 5
```

Otherwise, raise the user-defined exception:

```python
InvalidOperation
```

Print:

```text
Please enter two operands and operator separated by space
```

---

### 2. Invalid Operator

Only the following operators are allowed:

```text
+  -  *  /
```

If any other operator is used, raise the user-defined exception:

```python
InvalidOperator
```

Print:

```text
Invalid operator
```

---

### 3. Invalid Operands

Both operands must be numeric.

Raise the built-in exception:

```python
TypeError
```

Print the standard exception message.

---

### 4. Division by Zero

If division by zero occurs, raise the built-in exception:

```python
ZeroDivisionError
```

Print the standard exception message.

---

## Exception Messages

| Exception | Message |
|-----------|---------|
| `InvalidOperation` | `Please enter two operands and operator separated by space` |
| `InvalidOperator` | `Invalid operator` |
| `TypeError` | Standard exception message |
| `ZeroDivisionError` | Standard exception message |

---

## Solution

```python
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

        # Check for ZeroDivisionError before performing the actual operation
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
```

---

## Explanation

### Custom Exceptions

Two custom exceptions are created:

- `InvalidOperation` → Raised when the expression format is incorrect.
- `InvalidOperator` → Raised when an unsupported operator is used.

### Validation Steps

1. Split the expression into parts using `split()`.
2. Ensure there are exactly three elements.
3. Verify that the operator is one of `+`, `-`, `*`, or `/`.
4. Convert both operands to `float`.
5. Perform a temporary division (`num1 / num2`) to detect a `ZeroDivisionError` before calculating the final result.

### Exception Handling

All exceptions are handled by:

```python
except Exception as e:
    print(e)
```

This prints:

- Custom exception messages for `InvalidOperation` and `InvalidOperator`.
- Standard Python messages for `TypeError` and `ZeroDivisionError`.

### Successful Execution

If no exception occurs, the appropriate mathematical operation is performed and the result is printed.
