# Intro to JSON

**JSON (JavaScript Object Notation)** is a lightweight, text-based **data interchange format**. It is easy for humans to read and write, and simple for machines to parse and generate.

JSON is commonly used for exchanging and storing structured data.

## Structure of JSON

JSON is built on two main structures:

1. **A collection of name/value pairs** — similar to a Python dictionary.
2. **An ordered list of values** — similar to a Python list.

### JSON Objects

JSON data is represented using **key-value pairs** enclosed in curly braces `{}`.

```json
{
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"]
}
```

In this example:

* `"name"` is a key and `"John Doe"` is its value.
* `"age"` is a key and `30` is its value.
* `"city"` is a key and `"New York"` is its value.
* `"hobbies"` is a key whose value is an array.

A JSON object is similar to a Python dictionary:

```python
{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
```

### JSON Arrays

JSON arrays are ordered collections of values enclosed in square brackets `[]`.

For example:

```json
["reading", "swimming", "coding"]
```

A JSON array is similar to a Python list:

```python
["reading", "swimming", "coding"]
```

## JSON Data Types

JSON supports the following main data types:

### 1. String

A string is text enclosed in double quotes:

```json
"Hello, World!"
```

Example:

```json
{
    "name": "John"
}
```

> JSON strings use **double quotes**.

### 2. Number

JSON supports numbers such as integers and floating-point numbers:

```json
42
```

```json
3.14
```

Example:

```json
{
    "age": 30,
    "height": 1.75
}
```

### 3. Boolean

JSON has two Boolean values:

```json
true
```

and:

```json
false
```

Example:

```json
{
    "is_student": true
}
```

Notice that JSON uses lowercase `true` and `false`.

In Python, the equivalents are:

```python
True
False
```

### 4. Null

JSON uses `null` to represent the absence of a value:

```json
null
```

Example:

```json
{
    "middle_name": null
}
```

The Python equivalent is:

```python
None
```

### 5. Object

An object is a collection of key-value pairs enclosed in `{}`:

```json
{
    "name": "John",
    "age": 30
}
```

The JSON object is similar to a Python dictionary:

```python
{
    "name": "John",
    "age": 30
}
```

### 6. Array

An array is an ordered collection of values enclosed in `[]`:

```json
[1, 2, 3]
```

It is similar to a Python list:

```python
[1, 2, 3]
```

## JSON vs Python Data Types

| JSON    | Python          |
| ------- | --------------- |
| Object  | `dict`          |
| Array   | `list`          |
| String  | `str`           |
| Number  | `int` / `float` |
| `true`  | `True`          |
| `false` | `False`         |
| `null`  | `None`          |

For example, this JSON:

```json
{
    "name": "Alice",
    "age": 25,
    "is_student": true,
    "courses": ["Python", "SQL"],
    "address": null
}
```

is equivalent to this Python data:

```python
{
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "courses": ["Python", "SQL"],
    "address": None
}
```

## Common Use Cases

JSON is widely used for:

### 1. API Responses

Many web services and APIs use JSON to send data between a server and a client.

Example:

```json
{
    "id": 101,
    "name": "Alice",
    "email": "alice@example.com"
}
```

### 2. Configuration Files

Applications often use JSON files to store settings and configuration information.

Example:

```json
{
    "theme": "dark",
    "language": "English",
    "notifications": true
}
```

### 3. Data Storage

JSON can be used to store structured information in files.

Example:

```json
{
    "name": "Python",
    "year": 1991,
    "versions": ["3.8", "3.9", "3.10", "3.11"]
}
```

### 4. Data Exchange Between Programming Languages

JSON makes it easy for different programming languages and systems to exchange data.

For example, a Python application can send JSON data to a JavaScript application, and the JavaScript application can process it.

## Why JSON Is Important

JSON is popular because it is:

* **Simple** — its structure is easy to understand.
* **Lightweight** — it does not contain unnecessary formatting.
* **Human-readable** — people can easily read and edit it.
* **Language-independent** — many programming languages support it.
* **Widely supported** — it is commonly used in APIs, web applications, and data storage.

Because of its simplicity and versatility, **JSON is one of the most important formats for modern data exchange and storage**.

# JSON vs Python Data Types

JSON and Python have similar data types, but there are some important differences.

Understanding how JSON data types correspond to Python data types is essential when working with JSON in Python, especially when **encoding** and **decoding** data.

## JSON and Python Data Type Mappings

### 1. Object → Dictionary

A JSON **object** is equivalent to a Python **dictionary (`dict`)**.

**JSON:**

```json
{
    "name": "John",
    "age": 30
}
```

**Python:**

```python
{
    "name": "John",
    "age": 30
}
```

Both use key-value pairs.

---

### 2. Array → List

A JSON **array** is equivalent to a Python **list (`list`)**.

**JSON:**

```json
[1, 2, 3, 4]
```

**Python:**

```python
[1, 2, 3, 4]
```

Both represent an ordered collection of values.

---

### 3. String → String

A JSON **string** corresponds to a Python **string (`str`)**.

**JSON:**

```json
"Hello, World!"
```

**Python:**

```python
"Hello, World!"
```

> JSON strings use double quotes.

---

### 4. Number → Integer

A JSON number without a decimal point corresponds to a Python **integer (`int`)**.

**JSON:**

```json
42
```

**Python:**

```python
42
```

---

### 5. Number → Float

A JSON number with a decimal point corresponds to a Python **float (`float`)**.

**JSON:**

```json
3.14
```

**Python:**

```python
3.14
```

---

### 6. Boolean → Boolean

JSON has two Boolean values:

```json
true
false
```

Python uses:

```python
True
False
```

So:

**JSON:**

```json
{
    "is_student": true
}
```

**Python:**

```python
{
    "is_student": True
}
```

The main difference is capitalization.

---

### 7. Null → None

JSON uses `null` to represent the absence of a value.

Python uses `None`.

**JSON:**

```json
null
```

**Python:**

```python
None
```

For example:

**JSON:**

```json
{
    "middle_name": null
}
```

**Python:**

```python
{
    "middle_name": None
}
```

## Quick Comparison Table

| JSON Type | Python Equivalent   | Example            |
| --------- | ------------------- | ------------------ |
| Object    | Dictionary (`dict`) | `{"name": "John"}` |
| Array     | List (`list`)       | `[1, 2, 3]`        |
| String    | String (`str`)      | `"Hello"`          |
| Number    | Integer (`int`)     | `42`               |
| Number    | Float (`float`)     | `3.14`             |
| Boolean   | Boolean (`bool`)    | `true` → `True`    |
| Null      | `None`              | `null` → `None`    |

## Key Differences

### 1. Boolean and Null Values

JSON uses lowercase:

```json
true
false
null
```

Python uses:

```python
True
False
None
```

This difference is important when manually writing JSON data.

---

### 2. Numbers

JSON uses a general **number** type.

It does not explicitly distinguish between Python's `int` and `float` types in the same way Python does.

For example, JSON can contain:

```json
42
```

and:

```json
3.14
```

When JSON data is decoded by Python, these are normally represented as:

```python
42       # int
3.14     # float
```

---

### 3. Python Has Additional Data Types

Python supports data types that do not have direct JSON equivalents.

For example:

```python
(1, 2, 3)
```

is a **tuple**, while:

```python
{1, 2, 3}
```

is a **set**.

JSON does not have separate tuple or set data types.

When converting Python data to JSON, these types may need to be converted into JSON-supported types first.

For example, a tuple can be represented as a JSON array:

```python
(1, 2, 3)
```

becomes:

```json
[1, 2, 3]
```

## Why These Mappings Matter

When working with JSON in Python, data is often converted between the two formats.

For example:

```text
Python object → JSON → Python object
```

Using the `json` module:

```python
json.dumps()
```

converts Python data into JSON.

```python
json.loads()
```

converts JSON data back into Python.

The mappings can be summarized as:

```text
Python dict    ↔ JSON object
Python list    ↔ JSON array
Python str     ↔ JSON string
Python int     ↔ JSON number
Python float   ↔ JSON number
Python True    ↔ JSON true
Python False   ↔ JSON false
Python None    ↔ JSON null
```

Understanding these mappings is crucial when working with JSON data in Python because they determine how data is **encoded and decoded** between the two formats.

# The `json` Module

The **`json` module** is a built-in Python module in the standard python library that provides functions for working with **JSON (JavaScript Object Notation)** data.

It allows you to:

* Convert Python objects into JSON strings.
* Convert JSON strings into Python objects.
* Write Python objects to JSON files.
* Read JSON data from JSON files.

JSON is commonly used when working with **APIs, configuration files, and data exchange between different systems**.

## Importing the `json` Module

To use the JSON module in Python, import it first:

```python
import json
```

## Main Functions

The `json` module provides four main functions:

1. `json.dumps()` — Converts a Python object into a JSON string.
2. `json.loads()` — Converts a JSON string into a Python object.
3. `json.dump()` — Writes a Python object directly to a JSON file.
4. `json.load()` — Reads a JSON file and returns a Python object.

### `json.dumps()`

`dumps()` converts a Python object, such as a dictionary, into a JSON-formatted string.

```python
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)

print(json_string)
```

Output:

```text
{"name": "John", "age": 30, "city": "New York"}
```

The result of `json.dumps()` is a **string**.

---

### `json.loads()`

`loads()` converts a JSON string back into a Python object.

```python
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

data = json.loads(json_string)

print(data)
print(type(data))
```

Output:

```text
{'name': 'John', 'age': 30, 'city': 'New York'}
<class 'dict'>
```

So, `loads()` performs the reverse operation of `dumps()`:

```text
Python object → dumps() → JSON string
JSON string  → loads() → Python object
```

---

### `json.dump()`

`dump()` is used to write a Python object **directly into a JSON file**.

```python
import json

data = {
    "name": "John",
    "age": 30
}

with open("data.json", "w") as f:
    json.dump(data, f)
```

The dictionary is converted into JSON and stored in `data.json`.

---

### `json.load()`

`load()` reads JSON data from a file and converts it into a Python object.

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
```

The result is a Python dictionary.

## Difference Between the Four Functions

The easiest way to remember the functions is:

```text
Python object ──dumps()──> JSON string
JSON string   ──loads()──> Python object

Python object ──dump()───> JSON file
JSON file     ──load()───> Python object
```

The important difference is:

* `dumps()` and `loads()` work with **strings**.
* `dump()` and `load()` work with **files**.

# Challenge

**Difficulty:** Easy

Create a program that demonstrates the use of all four main functions of the `json` module:

* `dumps()`
* `loads()`
* `dump()`
* `load()`

## Requirements

1. Create a Python dictionary with the following key-value pairs:

   * `"name": "Python"`
   * `"year": 1991`
   * `"creator": "Guido van Rossum"`
   * `"is_oop": True`
   * `"versions": ["2.7", "3.6", "3.7", "3.8", "3.9"]`

2. Use `json.dumps()` to convert the dictionary to a JSON string and print the result.

3. Use `json.loads()` to parse the JSON string back into a Python object and print its type.

4. Use `json.dump()` to write the dictionary to a file named `python_info.json`.

5. Use `json.load()` to read the contents of `python_info.json` into a new Python object.

6. Print the value associated with the `"creator"` key from the new object.

The following input will be provided:

```text
Python
1991
Guido van Rossum
true
2.7,3.6,3.7,3.8,3.9
```

**Note:** The versions input is a comma-separated string, so it must be converted into a Python list.

# Solution

```python
import json

name = input()
year = int(input())
creator = input()
is_oop = input().lower() == "true"
versions = input().split(",")

python_info = {
    "name": name,
    "year": year,
    "creator": creator,
    "is_oop": is_oop,
    "versions": versions
}

# Convert Python dictionary to JSON string
json_string = json.dumps(python_info)
print(json_string)

# Convert JSON string back to Python object
python_object = json.loads(json_string)
print(type(python_object))

# Write dictionary to a JSON file
with open("python_info.json", "w") as f:
    json.dump(python_info, f)

# Read JSON data from the file
with open("python_info.json", "r") as f:
    new_object = json.load(f)

# Print the creator
print(new_object["creator"])
```

# Solution Explanation

## 1. Import the `json` Module

```python
import json
```

This imports Python's built-in `json` module so that we can use `dumps()`, `loads()`, `dump()`, and `load()`.

## 2. Read the Input

```python
name = input()
year = int(input())
creator = input()
is_oop = input().lower() == "true"
versions = input().split(",")
```

The `year` is converted from a string into an integer:

```python
year = int(input())
```

The `is_oop` input is converted into a Boolean:

```python
is_oop = input().lower() == "true"
```

If the input is:

```text
true
```

the result is:

```python
True
```

The versions are provided as a comma-separated string:

```text
2.7,3.6,3.7,3.8,3.9
```

Using:

```python
versions = input().split(",")
```

converts it into a list:

```python
["2.7", "3.6", "3.7", "3.8", "3.9"]
```

## 3. Create the Dictionary

```python
python_info = {
    "name": name,
    "year": year,
    "creator": creator,
    "is_oop": is_oop,
    "versions": versions
}
```

This creates the Python dictionary containing all the information.

## 4. Use `json.dumps()`

```python
json_string = json.dumps(python_info)
```

`dumps()` converts the Python dictionary into a **JSON string**.

```python
print(json_string)
```

The JSON representation will look similar to:

```json
{"name": "Python", "year": 1991, "creator": "Guido van Rossum", "is_oop": true, "versions": ["2.7", "3.6", "3.7", "3.8", "3.9"]}
```

Notice that Python's:

```python
True
```

becomes JSON's:

```json
true
```

## 5. Use `json.loads()`

```python
python_object = json.loads(json_string)
```

`loads()` converts the JSON string back into a Python object.

```python
print(type(python_object))
```

The output is:

```text
<class 'dict'>
```

because a JSON object is converted into a Python dictionary.

## 6. Use `json.dump()`

```python
with open("python_info.json", "w") as f:
    json.dump(python_info, f)
```

`dump()` writes the Python dictionary directly to the file:

```text
python_info.json
```

The `"w"` mode opens the file for writing.

## 7. Use `json.load()`

```python
with open("python_info.json", "r") as f:
    new_object = json.load(f)
```

`load()` reads the JSON data from the file and converts it back into a Python object.

The resulting object is stored in:

```python
new_object
```

## 8. Access the `"creator"` Value

```python
print(new_object["creator"])
```

This accesses the value associated with the `"creator"` key.

Output:

```text
Guido van Rossum
```

# Key Takeaway

Remember the difference between the four functions:

```text
dumps() → Python object → JSON string
loads() → JSON string   → Python object

dump()  → Python object → JSON file
load()  → JSON file     → Python object
```

A simple way to remember them:

* **`s` in `dumps` and `loads` → string**
* **No `s` in `dump` and `load` → file**

# `json.dumps()`

The `json.dumps()` function is a key component of Python's built-in `json` module.

It converts, or **serializes**, a Python object into a **JSON-formatted string**.

This is useful when you need to prepare Python data for:

* Storage
* Transmission
* APIs
* Configuration files
* Data exchange between different systems

## Basic Usage

The basic syntax of `json.dumps()` is:

```python
import json

json_string = json.dumps(python_object)
```

The function takes a Python object, such as a dictionary or list, and returns a JSON-formatted **string**.

## Example

Let's convert a Python dictionary into a JSON string:

```python
import json

python_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(python_dict)

print(json_string)
```

Output:

```text
{"name": "John", "age": 30, "city": "New York"}
```

The important point is that `json.dumps()` does **not** return another dictionary. It returns a **string** containing JSON data.

You can verify this using `type()`:

```python
print(type(json_string))
```

Output:

```text
<class 'str'>
```

# Data Type Conversion

`json.dumps()` automatically converts common Python data types into their corresponding JSON types.

| Python  | JSON    |
| ------- | ------- |
| `dict`  | Object  |
| `list`  | Array   |
| `str`   | String  |
| `int`   | Number  |
| `float` | Number  |
| `True`  | `true`  |
| `False` | `false` |
| `None`  | `null`  |

For example:

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "height": 1.65,
    "is_student": False,
    "courses": ["Python", "SQL"],
    "address": None
}

json_string = json.dumps(data)

print(json_string)
```

The Python values are converted to their JSON equivalents automatically.

Notice the difference between Python and JSON Boolean and null values:

```python
True   → true
False  → false
None   → null
```

# Formatting JSON with `json.dumps()`

`json.dumps()` provides several optional arguments that allow you to control how the resulting JSON string is formatted.

For example:

```python
json.dumps(
    data,
    indent=4,
    separators=(", ", ": "),
    sort_keys=True
)
```

### `indent=4`

```python
indent=4
```

Formats the JSON using **4 spaces** for each indentation level.

Without indentation:

```json
{"name": "Alice", "age": 30}
```

With `indent=4`:

```json
{
    "name": "Alice",
    "age": 30
}
```

### `separators=(", ", ": ")`

The `separators` argument controls how items and key-value pairs are separated.

```python
separators=(", ", ": ")
```

means:

* `", "` separates items with a comma followed by a space.
* `": "` separates keys and values with a colon followed by a space.

### `sort_keys=True`

```python
sort_keys=True
```

sorts dictionary keys alphabetically in the resulting JSON string.

For example:

```python
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

Using:

```python
json.dumps(data, sort_keys=True)
```

produces:

```json
{"age": 30, "city": "New York", "name": "Alice"}
```

# Challenge

**Difficulty:** Easy

Create a function that takes a Python object as input and returns a formatted JSON string with specific indentation and separators.

The function should:

1. Use `json.dumps()` to convert the input object to a JSON string.
2. Set the indentation to **4 spaces**.
3. Use `", "` as the item separator.
4. Use `": "` as the key separator.
5. Ensure that all keys in the resulting JSON string are sorted alphabetically.
6. Print the resulting formatted JSON string.

The following input will be provided:

```text
{"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "painting"], "is_student": false}
```

# Solution

```python
import json

data = json.loads(input())

def format_json(obj):
    return json.dumps(
        obj,
        indent=4,
        separators=(", ", ": "),
        sort_keys=True
    )

print(format_json(data))
```

# Solution Explanation

## 1. Import the `json` Module

```python
import json
```

This allows us to use `json.loads()` and `json.dumps()`.

## 2. Read and Parse the Input

The input is provided in JSON format:

```text
{"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "painting"], "is_student": false}
```

We use:

```python
data = json.loads(input())
```

to convert the JSON string into a Python dictionary.

This is necessary because the challenge asks us to create a function that takes a **Python object** as input.

After `json.loads()`, the data becomes approximately:

```python
{
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "painting"],
    "is_student": False
}
```

Notice that JSON's `false` becomes Python's `False`.

## 3. Define the Function

```python
def format_json(obj):
```

The function receives the Python object through the parameter `obj`.

## 4. Use `json.dumps()`

```python
return json.dumps(
    obj,
    indent=4,
    separators=(", ", ": "),
    sort_keys=True
)
```

The function uses four important arguments.

### `indent=4`

```python
indent=4
```

makes each nested level use 4 spaces.

### `separators=(", ", ": ")`

```python
separators=(", ", ": ")
```

specifies:

* `", "` between items.
* `": "` between keys and values.

### `sort_keys=True`

```python
sort_keys=True
```

sorts the dictionary keys alphabetically.

The keys will therefore appear in this order:

```text
age
city
hobbies
is_student
name
```

## 5. Print the Result

```python
print(format_json(data))
```

This calls the function and prints the formatted JSON string.

## Expected Output

```json
{
    "age": 30, 
    "city": "New York", 
    "hobbies": [
        "reading", 
        "painting"
    ], 
    "is_student": false, 
    "name": "Alice"
}
```

# Key Takeaways

The most important part of the solution is:

```python
json.dumps(
    obj,
    indent=4,
    separators=(", ", ": "),
    sort_keys=True
)
```

Remember:

* `json.dumps()` → Python object → JSON string
* `indent=4` → uses 4 spaces for indentation
* `separators=(", ", ": ")` → controls separators
* `sort_keys=True` → sorts keys alphabetically

The difference between `dumps()` and `loads()` is:

```text
Python object ──dumps()──> JSON string
JSON string   ──loads()──> Python object
```
# Formatting JSON Output

When working with JSON data, it's often useful to format the output for better readability. Python's `json.dumps()` function provides parameters to control the formatting of JSON output, making it more human-readable. This process is often called **pretty-printing**.

## The `indent` Parameter

The `indent` parameter in `json.dumps()` allows you to specify the number of spaces for indentation. This creates a more readable, hierarchical structure:

```python
import json

data = {"name": "John", "age": 30, "city": "New York"}

# Without indentation
print(json.dumps(data))

# With indentation
print(json.dumps(data, indent=2))
```

The output with `indent=2` will be:

```json
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

### How `indent` Works

* `indent=2` → uses 2 spaces for each indentation level.
* `indent=4` → uses 4 spaces for each indentation level.
* A larger value creates more spacing.
* If `indent` is not provided, the JSON is printed on a single line.

## The `separators` Parameter

The `separators` parameter allows you to specify the separators used between items and between keys and values.

It is a tuple containing two strings:

```python
(item_separator, key_separator)
```

For example:

```python
# Default separators
print(json.dumps(data, indent=2))

# Custom separators
print(json.dumps(data, indent=2, separators=(", ", ": ")))
```

The default separators are:

```python
(", ", ": ")
```

This means:

* `", "` separates items with a comma followed by a space.
* `": "` separates keys from their values with a colon followed by a space.

You can remove the spaces to create more compact JSON:

```python
print(json.dumps(data, separators=(",", ":")))
```

The result will look like:

```json
{"name":"John","age":30,"city":"New York"}
```

## Combining Parameters

You can combine `indent` and `separators` to have fine-tuned control over the JSON output:

```python
formatted_json = json.dumps(
    data,
    indent=4,
    separators=(", ", ": ")
)

print(formatted_json)
```

This produces a nicely formatted and easy-to-read JSON output, which is especially useful when working with complex nested structures.

---

# Challenge

**Difficulty:** Easy

Create a function that formats a nested JSON structure with custom indentation and separators.

The function should:

1. Accept three parameters:

   * A Python dictionary or list.
   * An indentation level.
   * A boolean flag for compact output.
2. Use `json.dumps()` to convert the input to a JSON string.
3. Use the specified indentation when `compact` is `False`.
4. Use no indentation when `compact` is `True`.
5. Use `", "` and `": "` as separators when `compact` is `False`.
6. Use `","` and `":"` as separators when `compact` is `True`.
7. Return the formatted JSON string.
8. Print the resulting formatted JSON string.

## Solution

```python
import json


def format_json(data, indent_level, compact):
    if compact:
        indent = None
        separators = (",", ":")
    else:
        indent = indent_level
        separators = (", ", ": ")

    return json.dumps(
        data,
        indent=indent,
        separators=separators
    )


data = {
    "menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
                {
                    "value": "New",
                    "onclick": "CreateNewDoc()"
                },
                {
                    "value": "Open",
                    "onclick": "OpenDoc()"
                },
                {
                    "value": "Close",
                    "onclick": "CloseDoc()"
                }
            ]
        }
    }
}

indent_level = 4
compact = False

result = format_json(data, indent_level, compact)

print(result)
```

## Solution Explanation

### 1. Import `json`

```python
import json
```

We import Python's built-in `json` module so that we can use `json.dumps()`.

---

### 2. Create the Function

```python
def format_json(data, indent_level, compact):
```

The function accepts three parameters:

* `data` → the dictionary or list that we want to convert to JSON.
* `indent_level` → the number of spaces used for indentation.
* `compact` → determines whether the JSON should be compact or readable.

---

### 3. Handle Compact Output

```python
if compact:
    indent = None
    separators = (",", ":")
```

If `compact` is `True`:

* `indent = None` prevents indentation.
* `(",", ":")` removes spaces after commas and colons.

For example:

```json
{"name":"John","age":30}
```

---

### 4. Handle Formatted Output

```python
else:
    indent = indent_level
    separators = (", ", ": ")
```

If `compact` is `False`:

* `indent` receives the specified indentation level.
* `(", ", ": ")` adds spaces after commas and colons.

For example:

```json
{
    "name": "John",
    "age": 30
}
```

---

### 5. Convert the Data to JSON

```python
return json.dumps(
    data,
    indent=indent,
    separators=separators
)
```

`json.dumps()` converts the Python dictionary into a JSON-formatted string.

The values of `indent` and `separators` are determined by the `compact` flag.

---

### 6. Create the Input Data

```python
data = {
    "menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
                {
                    "value": "New",
                    "onclick": "CreateNewDoc()"
                },
                {
                    "value": "Open",
                    "onclick": "OpenDoc()"
                },
                {
                    "value": "Close",
                    "onclick": "CloseDoc()"
                }
            ]
        }
    }
}
```

This is the nested Python dictionary that will be formatted as JSON.

---

### 7. Set the Function Arguments

```python
indent_level = 4
compact = False
```

The challenge provides:

```text
4
false
```

In Python, JSON's `false` corresponds to Python's `False`.

Therefore:

```python
indent_level = 4
compact = False
```

means that the output should use **4 spaces for indentation** and should **not** be compact.

---

### 8. Call the Function

```python
result = format_json(data, indent_level, compact)
```

The function receives:

```text
data
4
False
```

Since `compact` is `False`, the function uses:

```python
indent = 4
separators = (", ", ": ")
```

---

### 9. Print the Result

```python
print(result)
```

Finally, the formatted JSON string is displayed.

The output will be:

```json
{
    "menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
                {
                    "value": "New",
                    "onclick": "CreateNewDoc()"
                },
                {
                    "value": "Open",
                    "onclick": "OpenDoc()"
                },
                {
                    "value": "Close",
                    "onclick": "CloseDoc()"
                }
            ]
        }
    }
}
```

## Key Idea

The most important part of the solution is deciding the values of `indent` and `separators` based on the `compact` flag:

```python
if compact:
    indent = None
    separators = (",", ":")
else:
    indent = indent_level
    separators = (", ", ": ")
```

This allows the **same function** to produce either readable or compact JSON output.
