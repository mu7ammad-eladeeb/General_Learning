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

# **Variable Tricks**

Python offers various options for dealing with variables. One of the most powerful is **variable unpacking**.

When it comes to swapping values, you can do it this way:
```python
temp = a
a = b
b = temp

```

Now the values of **`a`** and **`b`** have been swapped.

In a Pythonic way, using variable unpacking, you can do it easily:
```python
a, b = b, a

```

Or to unpack tuples:
```python
x, y = (10, 20)  # x = 10, y = 20

```

Using **`*`**, we can deal with multiple values at once!
```python
a, *b, c = [1, 2, 3, 4]  # a = 1, b = [2, 3], c = 4

```

> *If there are not enough values to unpack into the variables, Python will raise an error!*
>
> ```python
> a, b = [1, 2, 3]  # Error
>
> ```
>
> ```python
> a, *b = [1, 2, 3]  # a = 1, b = [2, 3]
> ```

# **Dealing With Lists**

Lists are a big part of Python, so various list techniques can make your code more Pythonic.

You can initialize or create a list in a simple way using the **`*`** operator.
```python
arr = [1] * 3  # arr = [1, 1, 1]

```

Using a **`for`** loop, you can filter or map elements and create lists in a more Pythonic way.
```python
numbers = [1, 2, -3, -2, 5]

# Filter the numbers list to contain only positive numbers
# filtered_list = [1, 2, 5]
filtered_list = [num for num in numbers if num > 0]

# Map numbers to a list of their squares
# mapped_list = [1, 4, 9, 4, 25]
mapped_list = [num * num for num in numbers]

```

You can map and filter at the same time!
```python
positive_and_power = [num * num for num in numbers if num > 0]

```

> *When using `()` instead of `[]`, Python creates a generator expression instead of a list comprehension.*
>
> ```python
> filtered_gen = (num for num in numbers if num > 0)
> print(next(filtered_gen))  # 1
> print(next(filtered_gen))  # 2
> print(next(filtered_gen))  # 5
> ```

# **With a File**

Python uses a special keyword when dealing with files: **`with`**.

When using the **`with open`** syntax, the file you open will **automatically** close for you when you exit the **`with`** block.
```python
with open('file.txt') as f:
    content = f.read()
    ...

```

> *The **`with`** statement is better because it ensures that the file is always closed, even if an exception is raised inside the **`with`** block.*

# **Access a Dictionary Element**

When accessing an element in a dictionary, there is always the risk that the key does not exist.

The Pythonic way to check if a key exists in a dictionary is the **`in`** keyword:
```python
if 'name' in person_dict:
    print(person_dict['name'])

```

If a default value can be supplied, it is a good idea to use **`get()`**:
```python
print(person_dict.get('name', 'Anonymous'))

```

The following will print **`'Anonymous'`** if **`'name'`** does not exist in **`person_dict`**; otherwise, it will print the value associated with **`'name'`**.

## **Challenge**

Easy

Create a function **`area(sizes)`**.

**`sizes`** is a dictionary with 2 keys - **`width`** and **`height`**. If the keys do not exist, the default value should be **`1`**.

The expected output should be the **area size** - **`width * height`**.

> *Write Pythonic Code!*

### **Hints**

Hint 1

To get the **`width`**, you can use:
```python
width = sizes.get('width', 1)

```

In the same way, get the **`height`** and then return the product of the two values.

## **Solution**
```python
def area(sizes):
    width = sizes.get('width', 1)
    height = sizes.get('height', 1)
    return width * height
```

## **Explanation**

- `def area(sizes):` defines a function named `area` that accepts a dictionary called `sizes`.
- `sizes.get('width', 1)` retrieves the value associated with the key `'width'`. If the key does not exist, it returns the default value `1`.
- `sizes.get('height', 1)` does the same for the key `'height'`.
- `return width * height` multiplies the width by the height and returns the calculated area.

Using **`get()`** makes the code concise and avoids a `KeyError` when either key is missing.

# **Equals Operations**

Using the **`not`** and **`is`** keywords is good practice when checking truthiness or comparing with **`None`**.
```python
if value1:
    print("value1 is truthy!")

if not value2:
    print("value2 is falsey!")

if value3 is None:
    print("value3 is None!")

if value4 is not None:
    print("value4 is not None!")

```

Using **`==`** and **`!=`** to compare with **`True`**, **`False`**, or **`None`** is generally not the Pythonic way.

For example, prefer **`if value:`** over **`if value == True:`**, and **`if value is None:`** over **`if value == None:`**.
# **PEP8**

## **Introduction**

[PEP 8](https://www.python.org/dev/peps/pep-0008/) is a style guide that describes the coding standards for Python.

It's the most popular guide within the Python community.

We will go over some of the guidelines and get familiar with them.

> *PEP 8 is **not required** when coding in Python, although it's a very good practice to use it!*

## **Code Lay-out**

PEP 8 states some rules related to "Code Lay-out":

- Indent using 4 spaces or a tab.
- Lines should not be longer than 79 characters.

```python
# line with 137 characters
def some_very_long_function_name(very_important_argument1, very_important_argument2, very_important_argument3, very_important_argument4):
    pass

# Fix suggestion
def some_very_long_function_name(
    very_important_argument1,
    very_important_argument2,
    very_important_argument3,
    very_important_argument4):
    pass

# Much better!
```

> *Indenting continuation lines, as in the above example, is good practice.*

- Avoid multiple statements on the same line.

```python
do_calc1(); do_calc2(); x = 3;  # bad
```

```python
# good
do_calc1()
do_calc2()
x = 3
```

- Imports should be on separate lines.

```python
import sys, numpy  # bad
```

```python
# good
import sys
import numpy
```

## **Blank Lines**

PEP 8 rules related to blank lines:

- Surround top-level function and class definitions with two blank lines.

```python
import some_module


class ClassA:
    pass


class ClassB:
    pass

```

or

```python
def top_function1():
    pass


def top_function2():
    pass

```

- Method definitions inside a class are surrounded by a single blank line.

```python
class MyClass:
    def __init__(self):
        pass

    def func1(self):
        pass

    def func2(self):
        pass

```

- Extra blank lines may be used (sparingly) to separate groups of related functions.
- Use blank lines in functions, sparingly, to indicate logical sections.

## **Whitespace**

PEP 8 whitespace guidelines are the following:

- Avoid extra spaces within braces or brackets.

```python
items = [ 1 , 'abc'  ]  # bad
items = [1, 'abc']       # good

def func( parm ):  # bad
    ...
def func(parm):    # good
    ...

```

- Avoid trailing whitespace anywhere.

- Surround operators with one space on each side.

```python
n =3+5      # bad
n = 3 + 5   # good

```

- Don't use spaces around the **`=`** sign when it is used to indicate a keyword argument.

```python
def calc(num = 0.0):  # bad
    ...
def calc(num=0.0):    # good
    ...
```

# **SOLID**

## **Introduction**

**SOLID** principles are five basic rules to follow when programming:

**S**ingle-responsibility principle -

> *"There should never be more than one reason for a class to change."*

**O**pen–closed principle -

> *"Software entities should be open for extension, but closed for modification."*

**L**iskov substitution principle -

> *"Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."*

**I**nterface segregation principle -

> *"Many client-specific interfaces are better than one general-purpose interface."*

**D**ependency inversion principle -

> *"Depend upon abstractions, [not] concretions."*

SOLID principles can fit into a whole course. In this course, the basics will be shown with examples and challenges.

[Read more](https://en.wikipedia.org/wiki/SOLID)

## **Single responsibility**

> *"There should never be more than one reason for a class to change."*

Single responsibility principle (SRP) states that every class and function should have only one job or one reason to change.

Goals -

- Create highly cohesive and robust classes and functions.
- Promote class composition.
- Avoid code duplication.

## Open-Closed Principle

> *"Software entities should be open for extension, but closed for modification."*

The **Open-Closed Principle (OCP)** states that a function, module, or class should allow its behavior to be extended without requiring changes to its existing code.

This is one of the five principles of **SOLID**, a set of guidelines for designing maintainable and flexible object-oriented software.

### Example: A class that converts TXT files

Let's say we have a class called `TxtConvertor` that converts TXT files to JSON or XML:

```python
class TxtConvertor:
    def convert_to_json(self, file):
        print("converts file to json")

    def convert_to_xml(self, file):
        print("converts file to xml")
```

This structure violates the Open-Closed Principle because adding a new conversion format requires modifying the existing class.

#### Why?

For example, if we want to add support for converting TXT files to HTML, we would have to modify the existing `TxtConvertor` class by adding another method:

```python
def convert_to_html(self, file):
    print("converts file to html")
```

As the number of supported formats grows, the class keeps changing to accommodate each new format. This makes the code harder to maintain and extend.

- **Open for extension:** We should be able to add new functionality, such as HTML conversion.
- **Closed for modification:** We should avoid changing existing, working code whenever we add new functionality.
- **Violation:** Adding a new conversion format requires modifying the original class.

### So, what should we do?

One solution is to create an **abstract base class** that defines the common interface for all converters. Each specific converter can then implement its own conversion behavior.

```python
from abc import ABC, abstractmethod


class TxtConvertor(ABC):
    @abstractmethod
    def convert(self, file):
        pass


class TxtConvertorToJson(TxtConvertor):
    def convert(self, file):
        print("converts file to json")


class TxtConvertorToXml(TxtConvertor):
    def convert(self, file):
        print("converts file to xml")


class TxtConvertorToHtml(TxtConvertor):
    def convert(self, file):
        print("converts file to html")
```

#### Explanation of the solution

1. **`from abc import ABC, abstractmethod`** imports the tools needed to define an abstract base class and abstract methods.
2. **`class TxtConvertor(ABC)`** defines an abstract base class that establishes a common interface for all TXT converters.
3. **`@abstractmethod`** marks `convert()` as a method that subclasses must implement before their objects can be instantiated.
4. **`def convert(self, file):`** defines the common method signature. Each converter provides its own implementation.
5. **`pass`** is a placeholder that does nothing. It allows the abstract method to have a body, even though subclasses are expected to implement it.
6. **`TxtConvertorToJson`, `TxtConvertorToXml`, and `TxtConvertorToHtml`** are concrete subclasses that implement the `convert()` method for their respective formats.

Now, if we want to support another format, such as PDF, we can create a new subclass without modifying the existing converters:

```python
class TxtConvertorToPdf(TxtConvertor):
    def convert(self, file):
        print("converts file to pdf")
```

This makes the design easier to extend because each new format gets its own class.

### Important terms

- **Abstract base class (ABC):** A class designed to define a common interface or shared behavior for its subclasses. It generally cannot be instantiated directly when it contains unimplemented abstract methods.
- **Subclass:** A class that inherits from another class.
- **Inheritance:** An object-oriented programming feature that allows one class to inherit behavior and structure from another class.
- **Interface:** A set of methods that a class is expected to provide.
- **Implementation:** The actual code that performs a method's task.
- **Concrete class:** A class that implements all required abstract methods and can be instantiated.
- **`self`:** A reference to the current object instance, used to access its methods and attributes.
- **`file`:** A parameter representing the file or file-related data to convert. In this example, the methods only print messages; they do not perform actual file conversion.
- **SOLID:** Five object-oriented design principles intended to help developers create maintainable and extensible software.

> **Note:** The example demonstrates the design principle rather than a complete file-conversion system. In a real application, each `convert()` method would contain the actual conversion logic.

### Learn more

The Python `abc` library supports abstract base classes.

You can read more [here](https://docs.python.org/3/library/abc.html)

## **Liskov substitution**

> *"Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."*

This principle states that a child class must be substitutable from its parent class.

For example,

```python
class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f'Send {message} to {email}')


class SMS(Notification):
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')
```

As you can see both **`SMS`** and **`Email`** inherit from Notification but one is sending to **`email`** and one to **`phone`**, the **`SMS`** class is not substitutable from its parent **`Notification`**!


### **Challenge**

Medium

Fix the given code to apply Liskov substitution principle -

- **`notify`** function should only get **`message`** as argument.

- **`Email`** and **`SMS`** should each have constructor which will initiate **`email`** and **`phone`** accordingly.

- Edit the code to apply the changes.

> *This is only one suggested solution to apply Liskov principle there are more that will work!*

#### **Hints**

Hint 1

Your **`Email`** class should look like this,

```python
class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send {message} to {self.email}')
```

Now change accordingly for **`SMS`** and the main code!

Hint 2

Don't forget to change the main function,

```python
if __name__ == '__main__':
    email = input()
    phone = input()
    message = input()
    notification1 = Email(email)
    notification2 = SMS(phone)
    notification1.notify(message)
    notification2.notify(message)
```

### **Solution:**

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send {message} to {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send {message} to {self.phone}')


if __name__ == '__main__':
    email = input()
    phone = input()
    message = input()
    notification1 = Email(email)
    notification2 = SMS(phone)
    notification1.notify(message)
    notification2.notify(message)
```

#### **Explanation of solution**

1. **`from abc import ABC, abstractmethod`** imports the tools needed to define an abstract base class and abstract methods.
2. **`class Notification(ABC)`** defines an abstract base class that establishes a common interface for all notification types.
3. **`@abstractmethod`** marks `notify()` as a method that subclasses must implement before their objects can be instantiated.
4. **`def notify(self, message):`** defines the common method signature. Both `Email` and `SMS` must implement this method with the same parameter.
5. **`pass`** is a placeholder that does nothing. It allows the abstract method to have a body, even though subclasses are expected to implement it.
6. **`class Email(Notification)`** defines a child class that inherits from `Notification`.
7. **`def __init__(self, email):`** is the constructor that receives the email address when an `Email` object is created.
8. **`self.email = email`** stores the email address inside the object so the `notify()` method can use it later.
9. **`def notify(self, message):`** implements the notification behavior for email. It receives only the message and uses the stored email address as the recipient.
10. **`class SMS(Notification)`** defines another child class that inherits from `Notification`.
11. **`def __init__(self, phone):`** is the constructor that receives the phone number when an `SMS` object is created.
12. **`self.phone = phone`** stores the phone number inside the object.
13. **`def notify(self, message):`** implements the notification behavior for SMS. It receives only the message and uses the stored phone number as the recipient.
14. **`if __name__ == '__main__':`** checks whether the Python file is being executed directly.
15. **`input()`** reads the email address, phone number, and message from the user.
16. **`notification1 = Email(email)`** creates an email notification object and stores the email address in it.
17. **`notification2 = SMS(phone)`** creates an SMS notification object and stores the phone number in it.
18. **`notification1.notify(message)`** calls the email implementation of `notify()`.
19. **`notification2.notify(message)`** calls the SMS implementation of `notify()`.

#### **Why solution follows the Liskov Substitution Principle**

Both `Email` and `SMS` inherit from `Notification` and implement the same `notify(message)` interface. The recipient information is initialized in each class's constructor, so the calling code only needs to pass the message.

This means both child classes can be used wherever a `Notification` object is expected, without requiring the calling code to know which specific notification type it is using.

### **Important terms**

- **Abstract base class (ABC):** A class designed to define a common interface for its subclasses.
- **Subclass:** A class that inherits from another class.
- **Constructor (`__init__`):** A special method that initializes an object when it is created.
- **Method signature:** The method's name and its parameters.
- **Interface:** The methods and expected behavior that a class exposes to other code.
- **Substitutable:** Able to replace something else without breaking the expected behavior.
- **SOLID:** Five object-oriented design principles that help make software easier to maintain and extend.

## **Interface segregation**

> *"Many client-specific interfaces are better than one general-purpose interface."*

An interface is a description of behaviors that an object can do.

**The interface segregation** principle states that an interface should be as small a possible in terms of cohesion. In other words, it should only do **ONE** thing.

Let's see a bad example and we will fix it,

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def swim(self):
        pass
```

This is interface with multiple responsibilities!

And we will have problem when implementing this,

```python
class Frog(Animal):
    def walk(self):
        print("Walking")

    def swim(self):
        print("Swimming")


class Giraffe(Animal):
    def walk(self):
        print("Walking")

    def swim(self):
        raise Exception("Girrafe cannot swim!")
```

As you see this interface is not compatible with animals which cannot walk and swim!

### **Challenge**

Easy

Let's fix the above example by implementing **`Walkable`** and **`Swimable`** classes, you are given **`Frog`** and **`Giraffe`** classes which implements the new classes

Tasks:

- Create abstract class **`Walkable`** which has only one abstract function **`walk(self)`**
- Create abstract class **`Swimable`** which has only one abstract function **`swim(self)`**

Do not change the given code!

> *Notice that now each interface has only one responsibility and follows the principle.*

### **Solution:**

```python
from abc import ABC, abstractmethod


class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass


class Swimable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Frog(Walkable, Swimable):
    def walk(self):
        print("Walking")

    def swim(self):
        print("Swimming")


class Giraffe(Walkable):
    def walk(self):
        print("Walking")


if __name__ == "__main__":
    animal_type = input()
    if animal_type == "frog":
        animal = Frog()
        animal.walk()
        animal.swim()
    elif animal_type == "giraffe":
        animal = Giraffe()
        animal.walk()
        print("not Swimming")
```

#### **Brief explanation of the solution**

- **`Walkable(ABC)`** defines an abstract interface for animals that can walk. It requires the `walk()` method.
- **`Swimable(ABC)`** defines a separate abstract interface for animals that can swim. It requires the `swim()` method.
- **`Frog(Walkable, Swimable)`** inherits from both interfaces because a frog can walk and swim. It implements both methods.
- **`Giraffe(Walkable)`** inherits only from `Walkable` because a giraffe can walk but does not need to implement `swim()`.
- **`@abstractmethod`** requires subclasses to implement the specified method before their objects can be created.
- **`pass`** is a placeholder for the method implementation.

**Why this follows the Interface Segregation Principle:** Each interface has only one responsibility. Classes implement only the behaviors they need, so `Giraffe` is not forced to implement a swimming method it cannot use.
