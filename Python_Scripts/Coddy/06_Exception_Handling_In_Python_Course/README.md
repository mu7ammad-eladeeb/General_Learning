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
### Another Solution
```python
def contact_details(mobile):
    try:
        for i in mobile:
            if not int(i) and len(mobile) != 12:
                raise ValueError()
    except:
        print("Invalid")
    else:
        print("valid")
```
