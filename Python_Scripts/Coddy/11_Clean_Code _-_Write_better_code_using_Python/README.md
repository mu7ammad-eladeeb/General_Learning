# **What is clean code?**

**Clean code** is a set of rules that help to keep our code *readable*, *maintainable*, and *extendable*.

It's one of the most important aspects of writing good quality code.

> *Writing code is easy, but writing good, clean code is hard.*

---

Clean code is:

- Easy to understand
- More efficient
- easier to maintain, scale, refactor and debug

# **What will you learn?**

In this course you will learn the concepts of **Clean Code** when coding with **Python&#x20;**.

Main topics are :

- Styles conventions
- Pythonic code
- PEP 8

As always the key to success is **practice** so we will practice a lot.

Let's start from a simple challenge!



## **Challenge**

Easy

You are given a code for function **`init`** which gets **`name`** and **`age`**.

The function prints some greet and then calculates some kind of id and returns it.

As we will learn this function uses some bad practices but for now your task is to **seperate the concerns&#x20;**.

Create two helper functions to take care of the greet and the id calculations separately.

In the end it will look something like this,
```python
def init(name, age):
    greet(name, age)
    res = calc_id(name, age)
    return res
```

> ***`ord`** function converts char to his ASCII representation (int)*



### **Hints**

#### Hint 1



Create 2 functions, **`greet`** and **`calc_id`** and call the from **`init`** function,
```python
def greet(name, age):
    ...

def calc_id(name, age):
    ...

def init(name, age):
    greet(name, age)
    res = calc_id(name, age)
    return res
```

## **Solution**

```python
def greet(name, age):
    print('Hello,', name)

def calc_id(name, age):
    if age >= 18:
        print('Above 18')
    else:
        print('Below 18')

    res = 0
    for c in name:
        res += ord(c) * age
    return res

def init(name, age):
    greet(name, age)
    res = calc_id(name, age)
    return res
```

## **Explanation**

The main idea of this challenge is **separation of concerns**.

**Separation of concerns** means dividing a program into different functions where each function is responsible for a specific task. Instead of putting the greeting, age check, ID calculation, and result handling into one large function, we separate them into smaller functions.

### `greet()` function

```python
def greet(name, age):
```

- **`def`** is the Python keyword used to define a function.
- **`greet`** is the name of the function.
- **`(`** starts the parameter list.
- **`name`** is the first parameter.
- **`,`** separates the parameters.
- **`age`** is the second parameter.
- **`)`** ends the parameter list.
- **`:`** starts the function body.

```python
print('Hello,', name)
```

- **`print()`** displays information on the screen.
- **`'Hello,'`** is a string.
- **`name`** is the value passed to the function.
- The comma between the two arguments causes `print()` to place a space between them by default.

For example:

```python
greet("John", 20)
```

prints:

```text
Hello, John
```

The important point is that **`greet()`** is responsible only for the greeting.

---

### `calc_id()` function

```python
def calc_id(name, age):
```

This defines the **`calc_id()`** function. It receives **`name`** and **`age`** as parameters and is responsible for the age message and ID calculation.

```python
if age >= 18:
```

- **`if`** checks whether a condition is true.
- **`age`** is the current age.
- **`>=`** means "greater than or equal to".
- **`18`** is the value being compared against.
- **`:`** starts the code that runs when the condition is true.

If the age is 18 or greater:

```python
print('Above 18')
```

prints:

```text
Above 18
```

```python
else:
```

- **`else`** handles the opposite case.
- It runs when **`age >= 18`** is false.

```python
print('Below 18')
```

prints:

```text
Below 18
```

when the age is less than 18.

---

### Calculating the ID

```python
res = 0
```

- **`res`** is a variable used to store the calculated result.
- **`=`** is the assignment operator.
- **`0`** is the starting value.

We start at `0` because values will be added to `res` during the loop.

```python
for c in name:
```

This loops through every character in the `name`.

- **`for`** starts a loop.
- **`c`** is the loop variable and represents the current character.
- **`in`** tells Python to iterate through `name`.
- **`name`** is the string being iterated over.
- **`:`** starts the loop body.

For example, if:

```python
name = "Bob"
```

the loop processes:

```text
B
o
b
```

one character at a time.

```python
res += ord(c) * age
```

This calculates a value for each character and adds it to `res`.

- **`ord(c)`** converts the character into its integer Unicode code point. For standard English characters, these values correspond to their ASCII representations.
- **`*`** multiplies the character's numeric value by `age`.
- **`+=`** adds the calculated value to the current value of `res`.

This:

```python
res += ord(c) * age
```

is equivalent to:

```python
res = res + ord(c) * age
```

The calculation is repeated for every character in the name.

```python
return res
```

- **`return`** sends a value back to the code that called the function.
- **`res`** is the final calculated ID.

Unlike the previous version, this solution correctly **returns** the calculated ID instead of only printing it.

---

### `init()` function

```python
def init(name, age):
```

This defines the **`init()`** function, which receives the person's name and age.

```python
greet(name, age)
```

This calls the **`greet()`** function and passes `name` and `age` to it.

The greeting responsibility is therefore handled by `greet()` instead of being written directly inside `init()`.

```python
res = calc_id(name, age)
```

This calls **`calc_id()`** and stores the value it returns in the variable **`res`**.

Because `calc_id()` ends with:

```python
return res
```

the calculated ID is returned to `init()`.

```python
return res
```

Finally, `init()` returns that calculated ID to whatever code called `init()`.

---

### Why is this cleaner?

Instead of one large function doing everything, the responsibilities are separated:

```text
init()
 ├── greet()       → handles the greeting
 └── calc_id()     → handles the age check and ID calculation
```

This makes the code easier to:

- **Read** — each function has a clear purpose.
- **Understand** — the details of each task are separated.
- **Maintain** — changes to the greeting can be made inside `greet()`.
- **Reuse** — `greet()` and `calc_id()` can be called independently.
- **Test** — each function can be tested separately.

This is the main clean-code concept being practiced in this challenge: **separate different responsibilities into different functions**.

# **Naming Conventions**

Naming is crucial part of writing code, You give names to variable, function, classes and more...

Python introduce some suggested naming styles:

| Type     | Convention                       | Example                                    |
| -------- | -------------------------------- | ------------------------------------------ |
| Variable | Snake case                       | **`x`**, **`index`**, **`max_number`**     |
| Function | Snake case                       | **`calculate`**, **`convert_to_int`**      |
| Class    | Pascal case                      | **`Person`**, **`JavaCompiler`**           |
| Method   | Snake case                       | **`print`**, **`make_sound`**              |
| Constant | Snake case (all caps)            | **`PI`**, **`MAX_TIMEOUT`**, **`MIN_AGE`** |
| Module   | Snake case                       | **`script.py`**, **`my_app.py`**           |
| Package  | Snake case (without underscores) | **`package`**, **`mypackage`**             |

- Snake case (snake_case) - Lower case letters, words separated with underscores.
- Pascal case (PascalCase) - Capitalised words

More detailed example of using it all together,
```python
import my_module


class ImportantClass:
    MY_CONSTANT = 3.14

    def good_function(self, variable):
        return variable
        
    def better_function(self):
        return MY_CONSTANT
        

def __name__ == '__main__':
    var = my_module.secret()
    important_class = ImportantClass()
    important_class.good_function(var)
    print(important_class.better_function())


```

Notice all the diferent types here!

> *Did you know? the difference between function and method is that method is a function associated with object/class*

# **The Right Name**

When choosing names, you should always choose **descriptive names** that make your code much more **readable**.

For example:
```python
def foo(x):
    return x * 2

```

The example above is unclear because the function name **`foo`** and the parameter name **`x`** do not tell us what they represent.

## **The right way:**
```python
def multiply_by_2(num):
    return num * 2

```

Now the code is clear even without reading the function's body. The name **`multiply_by_2`** tells us exactly what the function does, while **`num`** makes it clear that the parameter represents a number.

> *Whenever possible, avoid using one-letter names like `a`, `x`, `i`, etc. Use descriptive names that make the purpose of the variable or function clear.*

**Note:** One-letter names can sometimes be appropriate when their meaning is obvious from the context, such as **`i`** in a simple loop:
```python
for i in range(10):
    print(i)
```

# **Block Comments**

> *“If the implementation is hard to explain, it’s a bad idea.”*
>
> *- The Zen of Python*

Comments are important so that anyone who will read your code can understand it.

Comments in Python seperate into 3 kinds:

- Block Comments
- Inline Comments
- Documentation Strings

Let's start from the **Block Comments** -

- Starts from the same indent block as the code they describe.
- Start each line with a **`#`** followed by a single space.

For example,
```python
while i < 10:
    # Loop over i until i < 10
    # print i with new line and increment it by 1
    print(i, '\n')
    i += 1
```
# **Inline Comments**

Inline comments explain a single statement in a piece of code.

- Write inline comments on the same line as the statement they refer to.
- Separate inline comments by **two or more spaces** from the statement.
- Starts with a **`#`** and a single space.
- Don’t use them to explain the obvious.

For example,
```python
result = check(name)  # Check if name is good

```

> *Most of the times you will prefer using Comments Blocks instead of Inline Blocks.*

# **Documentation Strings**

Document String or Docstring it mostly occurs as the **first statement** in a module, function, class, or method definition.

Declare docstring by wrapping string with **`"""`** or **`'''`** for example,
```python
def complex(real=0.0, imag=0.0):
    """
    Form a complex number.

        Parameters:
            real (float) -- the real part (default 0.0)
            imag (float) -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...

```

take a look at how it documents the **`complex(real, imag)`** function. 

> *Notice the indentation of the doc body and the **`"""`***

After using docstring like this you can use **`__doc__`** property to get the documentation,
```python
complex.__doc__

```

Will output the following,
```python
Form a complex number.

    Parameters:
        real (float) -- the real part (default 0.0)
        imag (float) -- the imaginary part (default 0.0)
```

# **The Zen**

**The Zen of Python** is a collection of 19 guiding principles for writing Python code.

> *Beautiful is better than ugly.*
>
> *Explicit is better than implicit.*
>
> *Simple is better than complex.*
>
> *Complex is better than complicated.*
>
> *Flat is better than nested.*
>
> *Sparse is better than dense.*
>
> *Readability counts.*
>
> *Special cases aren't special enough to break the rules.*
>
> *Although practicality beats purity.*
>
> *Errors should never pass silently.*
>
> *Unless explicitly silenced.*
>
> *In the face of ambiguity, refuse the temptation to guess.*
>
> *There should be one-- and preferably only one --obvious way to do it.*
>
> *Although that way may not be obvious at first unless you're Dutch.*
>
> *Now is better than never.*
>
> *Although never is often better than *right* now.*
>
> *If the implementation is hard to explain, it's a bad idea.*
>
> *If the implementation is easy to explain, it may be a good idea.*
>
> *Namespaces are one honking great idea -- let's do more of those!*

Hopefully, after this course, you will **understand and follow** some of these guidelines!

You can print the Zen of Python by running the following in the Python interpreter:

```python
>>> import this
```
