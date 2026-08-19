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

# Custom JSON Encoding

Custom JSON encoding is a powerful feature in Python's `json` module that allows you to serialize complex Python objects that are not natively supported by JSON.

This is particularly useful when working with custom classes or objects that do not have a direct JSON representation.

## The `JSONEncoder` Class

To create a custom JSON encoder, subclass the `json.JSONEncoder` class and override its `default()` method:

```python
import json


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomClass):
            return obj.to_dict()

        return json.JSONEncoder.default(self, obj)
```

The `default()` method is called when Python encounters an object that cannot normally be serialized into JSON.

If the object is an instance of our custom class, we can convert it into a dictionary or another JSON-compatible type.

For objects we do not know how to handle, we should fall back to the original encoder:

```python
return json.JSONEncoder.default(self, obj)
```

## Using the Custom Encoder

Once the custom encoder has been created, pass it to `json.dumps()` using the `cls` parameter:

```python
json_string = json.dumps(your_object, cls=CustomEncoder)
```

We can also use it with `json.dump()` when writing JSON directly to a file.

---

## Example: Encoding a Custom Class

Consider this example:

```python
import json
from datetime import datetime


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {
                "name": obj.name,
                "birthdate": obj.birthdate.isoformat()
            }

        elif isinstance(obj, datetime):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)


person = Person("Alice", datetime(1990, 5, 15))

json_string = json.dumps(
    person,
    cls=CustomEncoder,
    indent=2
)

print(json_string)
```

Here, the `Person` object is not directly JSON serializable.

The custom encoder converts it into a dictionary:

```python
{
    "name": obj.name,
    "birthdate": obj.birthdate.isoformat()
}
```

The `datetime` object is also converted into a JSON-compatible string using `isoformat()`.

---

# Challenge

**Difficulty: Easy**

Create a custom JSON encoder for a `ComplexNumber` class.

The encoder should convert complex numbers to a JSON object with `"real"` and `"imag"` keys for the real and imaginary parts, respectively.

### Requirements

1. Define a `ComplexNumber` class with `real` and `imag` attributes.
2. Create a custom `JSONEncoder` subclass that handles `ComplexNumber` objects.
3. Implement a function that takes a list of `ComplexNumber` objects and returns a JSON string representation using the custom encoder.
4. Print the resulting JSON string.
5. Ensure that the JSON is formatted with an indent of 2 spaces.

### Input

The following input will be provided:

```text
3.14,2.71
1.41,-1.73
2.0,0
0,-1
```

Each line represents a complex number with the real and imaginary parts separated by a comma.

### Expected JSON Structure

Each `ComplexNumber` should be converted into an object with this structure:

```json
{
  "real": 3.14,
  "imag": 2.71
}
```

The complete output should therefore be a JSON array containing all the converted complex numbers.

---

# Solution

```python
import json


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


class ComplexNumberEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ComplexNumber):
            return {
                "real": obj.real,
                "imag": obj.imag
            }

        return json.JSONEncoder.default(self, obj)


def encode_complex_numbers(numbers):
    return json.dumps(
        numbers,
        cls=ComplexNumberEncoder,
        indent=2
    )


numbers = []

while True:
    try:
        line = input().strip()

        if not line:
            break

        real, imag = map(float, line.split(","))
        numbers.append(ComplexNumber(real, imag))

    except EOFError:
        break


print(encode_complex_numbers(numbers))
```

---

# Solution Explanation

## 1. Import the `json` module

```python
import json
```

The `json` module provides the `JSONEncoder` class and the `json.dumps()` function that we need to convert Python objects into JSON.

---

## 2. Define the `ComplexNumber` class

```python
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
```

The class contains two attributes:

* `real` — the real part of the complex number.
* `imag` — the imaginary part of the complex number.

For example:

```python
number = ComplexNumber(3.14, 2.71)
```

creates an object equivalent to:

```text
real = 3.14
imag = 2.71
```

---

## 3. Create the custom JSON encoder

```python
class ComplexNumberEncoder(json.JSONEncoder):
```

The class inherits from `json.JSONEncoder`.

This allows us to customize how `ComplexNumber` objects are converted to JSON.

---

## 4. Override the `default()` method

```python
def default(self, obj):
    if isinstance(obj, ComplexNumber):
        return {
            "real": obj.real,
            "imag": obj.imag
        }

    return json.JSONEncoder.default(self, obj)
```

The `default()` method is called when the JSON encoder encounters an object that it does not know how to serialize.

We use:

```python
isinstance(obj, ComplexNumber)
```

to check whether the object is a `ComplexNumber`.

If it is, we convert it into a dictionary:

```python
{
    "real": obj.real,
    "imag": obj.imag
}
```

Dictionaries are natively supported by JSON, so the encoder can then serialize this dictionary.

For any other unsupported object, we use:

```python
json.JSONEncoder.default(self, obj)
```

This falls back to the standard JSON encoder behavior.

---

## 5. Create the encoding function

```python
def encode_complex_numbers(numbers):
    return json.dumps(
        numbers,
        cls=ComplexNumberEncoder,
        indent=2
    )
```

The function receives a list of `ComplexNumber` objects.

The important part is:

```python
cls=ComplexNumberEncoder
```

This tells `json.dumps()` to use our custom encoder.

The:

```python
indent=2
```

parameter formats the JSON using two spaces for indentation.

---

## 6. Read the input

```python
numbers = []

while True:
    try:
        line = input().strip()

        if not line:
            break

        real, imag = map(float, line.split(","))
        numbers.append(ComplexNumber(real, imag))

    except EOFError:
        break
```

We start with an empty list:

```python
numbers = []
```

Each input line contains two values separated by a comma:

```text
3.14,2.71
```

We split the line:

```python
line.split(",")
```

which produces:

```python
["3.14", "2.71"]
```

Then:

```python
map(float, ...)
```

converts the values into floating-point numbers.

Finally, we create a `ComplexNumber` object:

```python
ComplexNumber(real, imag)
```

and add it to the list.

---

## 7. Print the JSON

```python
print(encode_complex_numbers(numbers))
```

The list of `ComplexNumber` objects is passed to our encoding function.

The custom encoder converts every `ComplexNumber` into a dictionary before producing the final JSON string.

For the provided input, the result is:

```json
[
  {
    "real": 3.14,
    "imag": 2.71
  },
  {
    "real": 1.41,
    "imag": -1.73
  },
  {
    "real": 2.0,
    "imag": 0.0
  },
  {
    "real": 0.0,
    "imag": -1.0
  }
]
```

## Key Points

* `JSONEncoder` can be subclassed to support custom Python objects.
* The `default()` method handles objects that are not natively JSON serializable.
* `isinstance()` checks whether the object is a `ComplexNumber`.
* The custom object is converted into a dictionary containing `"real"` and `"imag"`.
* `cls=ComplexNumberEncoder` tells `json.dumps()` to use the custom encoder.
* `indent=2` produces nicely formatted JSON.
* Calling `json.JSONEncoder.default()` provides a fallback for objects that our custom encoder does not handle.

The overall process is:

```text
ComplexNumber object
        ↓
Custom JSONEncoder
        ↓
Dictionary
        ↓
JSON object
```

This approach allows custom Python classes to be easily integrated into JSON-based applications.

# `json.loads()`

The `json.loads()` function is an important part of Python's built-in `json` module. It is used to **parse a JSON-formatted string and convert it into a Python object**. This process is called **deserialization**.

## Basic Usage

The basic syntax of `json.loads()` is:

```python
import json

python_object = json.loads(json_string)
```

The function takes a JSON string as its argument and returns the corresponding Python object.

For example:

```python
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

parsed_data = json.loads(json_string)

print(type(parsed_data))
print(parsed_data)
```

Output:

```text
<class 'dict'>
{'name': 'John', 'age': 30, 'city': 'New York'}
```

The JSON object is converted into a Python dictionary.

## Data Type Conversion

`json.loads()` automatically converts JSON data types into their corresponding Python types:

| JSON Type | Python Type      |
| --------- | ---------------- |
| Object    | `dict`           |
| Array     | `list`           |
| String    | `str`            |
| Number    | `int` or `float` |
| `true`    | `True`           |
| `false`   | `False`          |
| `null`    | `None`           |

For example:

```python
import json

json_string = '''
{
    "name": "John",
    "age": 30,
    "is_student": false,
    "courses": ["Python", "JSON"],
    "address": null
}
'''

data = json.loads(json_string)

print(type(data))              # <class 'dict'>
print(type(data["courses"]))   # <class 'list'>
print(data["is_student"])      # False
print(data["address"])         # None
```

`json.loads()` is especially useful when JSON data is received as a string, such as data returned by an API.

---

# Challenge

**Difficulty: Easy**

Create a function that parses a JSON string containing information about a book and performs several operations on the parsed data.

The function should:

1. Use `json.loads()` to parse the input JSON string.
2. Extract:

   * The title of the book
   * The number of pages
   * The list of authors
3. Perform the following operations:

   * Convert the title to uppercase.
   * Increase the number of pages by `10`.
   * Sort the authors alphabetically.
4. Create a new dictionary containing the modified data.
5. Return a string in this format:

```text
TITLE | Pages: X | Authors: A, B, C
```

The input will be:

```json
{"title": "Python Programming", "pages": 300, "authors": ["John Smith", "Alice Johnson", "Bob Wilson"]}
```

Print the resulting string.

---

# Solution

```python
import json


def process_book(json_string):
    book = json.loads(json_string)

    title = book["title"].upper()
    pages = book["pages"] + 10
    authors = sorted(book["authors"])

    modified_book = {
        "title": title,
        "pages": pages,
        "authors": authors
    }

    return f'{modified_book["title"]} | Pages: {modified_book["pages"]} | Authors: {", ".join(modified_book["authors"])}'


json_string = '{"title": "Python Programming", "pages": 300, "authors": ["John Smith", "Alice Johnson", "Bob Wilson"]}'

print(process_book(json_string))
```

Output:

```text
PYTHON PROGRAMMING | Pages: 310 | Authors: Alice Johnson, Bob Wilson, John Smith
```

---

# Solution Explanation

### 1. Import `json`

```python
import json
```

The `json` module provides the `json.loads()` function that we need to convert the JSON string into a Python dictionary.

### 2. Parse the JSON string

```python
book = json.loads(json_string)
```

The input is a JSON string:

```json
{"title": "Python Programming", "pages": 300, "authors": ["John Smith", "Alice Johnson", "Bob Wilson"]}
```

After calling `json.loads()`, it becomes a Python dictionary:

```python
{
    "title": "Python Programming",
    "pages": 300,
    "authors": ["John Smith", "Alice Johnson", "Bob Wilson"]
}
```

Now we can access its values using dictionary keys.

### 3. Convert the title to uppercase

```python
title = book["title"].upper()
```

`book["title"]` gives:

```text
Python Programming
```

Calling `.upper()` converts it to:

```text
PYTHON PROGRAMMING
```

### 4. Increase the number of pages

```python
pages = book["pages"] + 10
```

The original number of pages is `300`, so:

```text
300 + 10 = 310
```

Therefore, `pages` becomes `310`.

### 5. Sort the authors

```python
authors = sorted(book["authors"])
```

The original list is:

```python
["John Smith", "Alice Johnson", "Bob Wilson"]
```

`sorted()` returns the authors in alphabetical order:

```python
["Alice Johnson", "Bob Wilson", "John Smith"]
```

### 6. Create a new dictionary

```python
modified_book = {
    "title": title,
    "pages": pages,
    "authors": authors
}
```

This creates a new dictionary containing all the modified values:

```python
{
    "title": "PYTHON PROGRAMMING",
    "pages": 310,
    "authors": ["Alice Johnson", "Bob Wilson", "John Smith"]
}
```

### 7. Build the final string

```python
return f'{modified_book["title"]} | Pages: {modified_book["pages"]} | Authors: {", ".join(modified_book["authors"])}'
```

The `f-string` inserts the modified values into the required format.

The `join()` method converts the list of authors:

```python
["Alice Johnson", "Bob Wilson", "John Smith"]
```

into:

```text
Alice Johnson, Bob Wilson, John Smith
```

The final result is:

```text
PYTHON PROGRAMMING | Pages: 310 | Authors: Alice Johnson, Bob Wilson, John Smith
```

### Key Idea

The important part of this challenge is understanding that **`json.loads()` converts JSON text into a Python object**, allowing you to work with the data using normal Python operations such as dictionary access, `.upper()`, `+`, `sorted()`, and `.join()`.

# Handling JSON Data Types

Understanding how JSON data types are converted into Python types is important when working with `json.loads()`. After parsing JSON, the resulting values are normal Python objects, so you can use Python's built-in type-checking functions such as `isinstance()` and `type()` to determine how each value should be processed.

## JSON → Python Type Conversions

| JSON Type | Python Type      |
| --------- | ---------------- |
| Object    | `dict`           |
| Array     | `list`           |
| String    | `str`            |
| Number    | `int` or `float` |
| Boolean   | `bool`           |
| `null`    | `None`           |

### 1. JSON Objects → Python Dictionaries

JSON objects are converted into Python dictionaries:

```python
import json

json_string = '{"name": "John", "age": 30}'
python_dict = json.loads(json_string)

print(type(python_dict))       # <class 'dict'>
print(python_dict["name"])     # John
```

### 2. JSON Arrays → Python Lists

JSON arrays become Python lists:

```python
json_array = '[1, 2, 3, 4, 5]'
python_list = json.loads(json_array)

print(type(python_list))       # <class 'list'>
print(python_list[2])          # 3
```

### 3. JSON Strings → Python Strings

JSON strings become Python strings:

```python
json_string = '"Hello, World!"'
python_string = json.loads(json_string)

print(type(python_string))     # <class 'str'>
print(python_string)           # Hello, World!
```

### 4. JSON Numbers → Python `int` or `float`

JSON numbers become Python integers or floats:

```python
json_integer = '42'
json_float = '3.14'

python_integer = json.loads(json_integer)
python_float = json.loads(json_float)

print(type(python_integer))    # <class 'int'>
print(type(python_float))      # <class 'float'>
```

### 5. JSON Booleans → Python `bool`

JSON `true` and `false` become Python `True` and `False`:

```python
json_bool = 'true'
python_bool = json.loads(json_bool)

print(type(python_bool))       # <class 'bool'>
print(python_bool)             # True
```

### 6. JSON `null` → Python `None`

JSON `null` becomes Python `None`:

```python
json_null = 'null'
python_none = json.loads(json_null)

print(type(python_none))       # <class 'NoneType'>
print(python_none)             # None
```

---

# Challenge

**Difficulty: Easy**

Create a function that processes a JSON string containing a mixed array of different data types.

The function should:

1. Parse the JSON string using `json.loads()`.
2. Iterate through the parsed array and perform the following operations:

   * For strings: convert to uppercase.
   * For numbers (`int` or `float`): multiply by 2.
   * For booleans: invert the value.
   * For `null`: replace with the string `"null_value"`.
   * For nested arrays: sum all numeric values, ignoring non-numeric values.
   * For nested objects: count the number of key-value pairs.
3. Return a new list with the processed values.
4. Print the resulting list as a string, with elements separated by commas.

### Input

```text
["hello", 42, true, null, [1, "two", 3], {"a": 1, "b": 2}]
```

### Expected Output

```text
HELLO,84,False,null_value,4,2
```

---

# Solution 1 — Using `isinstance()`

```python
import json


def process_json(json_string):
    data = json.loads(json_string)
    result = []

    for value in data:
        if isinstance(value, bool):
            result.append(not value)

        elif isinstance(value, str):
            result.append(value.upper())

        elif isinstance(value, (int, float)):
            result.append(value * 2)

        elif value is None:
            result.append("null_value")

        elif isinstance(value, list):
            total = sum(
                item for item in value
                if isinstance(item, (int, float)) and not isinstance(item, bool)
            )
            result.append(total)

        elif isinstance(value, dict):
            result.append(len(value))

    return result


json_string = '["hello", 42, true, null, [1, "two", 3], {"a": 1, "b": 2}]'

result = process_json(json_string)

print(",".join(map(str, result)))
```

## Explanation

First, `json.loads()` converts the JSON string into a Python list:

```python
data = json.loads(json_string)
```

The JSON:

```text
["hello", 42, true, null, [1, "two", 3], {"a": 1, "b": 2}]
```

becomes approximately:

```python
["hello", 42, True, None, [1, "two", 3], {"a": 1, "b": 2}]
```

The function then loops through every value and determines its type.

### Boolean

```python
if isinstance(value, bool):
    result.append(not value)
```

This checks whether the value is a Boolean and reverses it.

```python
True → False
False → True
```

The Boolean check must come before the number check because Python's `bool` type is a subclass of `int`.

### String

```python
elif isinstance(value, str):
    result.append(value.upper())
```

Strings are converted to uppercase.

```text
"hello" → "HELLO"
```

### Numbers

```python
elif isinstance(value, (int, float)):
    result.append(value * 2)
```

The tuple `(int, float)` allows `isinstance()` to check for either an integer or a floating-point number.

```text
42 → 84
3.5 → 7.0
```

### `None`

```python
elif value is None:
    result.append("null_value")
```

JSON `null` is converted to Python `None`.

Therefore, we check:

```python
value is None
```

and replace it with:

```text
"null_value"
```

### Nested Arrays

```python
elif isinstance(value, list):
    total = sum(
        item for item in value
        if isinstance(item, (int, float)) and not isinstance(item, bool)
    )
    result.append(total)
```

A nested JSON array becomes a Python list.

For:

```python
[1, "two", 3]
```

only the numeric values are included:

```text
1 + 3 = 4
```

The string `"two"` is ignored.

The additional Boolean check:

```python
and not isinstance(item, bool)
```

prevents `True` and `False` from being treated as numbers.

### Nested Objects

```python
elif isinstance(value, dict):
    result.append(len(value))
```

A JSON object becomes a Python dictionary.

For:

```python
{"a": 1, "b": 2}
```

there are two key-value pairs, so:

```python
len(value)
```

returns:

```text
2
```

### Printing the Result

```python
print(",".join(map(str, result)))
```

The resulting list is:

```python
["HELLO", 84, False, "null_value", 4, 2]
```

Because `join()` requires strings, `map(str, result)` converts each element to a string.

The final output is:

```text
HELLO,84,False,null_value,4,2
```

---

# Solution 2 — Using `type()`

```python
import json


def process_json(json_string):
    data = json.loads(json_string)
    result = []

    for value in data:
        if type(value) is bool:
            result.append(not value)

        elif type(value) is str:
            result.append(value.upper())

        elif type(value) in (int, float):
            result.append(value * 2)

        elif value is None:
            result.append("null_value")

        elif type(value) is list:
            total = sum(
                item for item in value
                if type(item) in (int, float)
            )
            result.append(total)

        elif type(value) is dict:
            result.append(len(value))

    return result


json_string = '["hello", 42, true, null, [1, "two", 3], {"a": 1, "b": 2}]'

result = process_json(json_string)

print(",".join(map(str, result)))
```

## Explanation

This solution performs the same operations, but uses `type()` instead of `isinstance()`.

### Boolean

```python
if type(value) is bool:
    result.append(not value)
```

This checks whether the exact type of `value` is `bool`.

### String

```python
elif type(value) is str:
    result.append(value.upper())
```

This checks whether the exact type is `str`, then converts the string to uppercase.

```text
"hello" → "HELLO"
```

### Numbers

```python
elif type(value) in (int, float):
    result.append(value * 2)
```

This checks whether the exact type is either `int` or `float`.

```text
42 → 84
```

### `None`

```python
elif value is None:
    result.append("null_value")
```

JSON `null` becomes Python `None`, so it is replaced with `"null_value"`.

### Nested Arrays

```python
elif type(value) is list:
    total = sum(
        item for item in value
        if type(item) in (int, float)
    )
    result.append(total)
```

This checks for an exact `list` type and sums its numeric values.

For:

```python
[1, "two", 3]
```

the calculation is:

```text
1 + 3 = 4
```

### Nested Objects

```python
elif type(value) is dict:
    result.append(len(value))
```

This checks for an exact `dict` type and counts its key-value pairs.

```python
{"a": 1, "b": 2}
```

contains two key-value pairs, so the result is:

```text
2
```

### Printing the Result

```python
print(",".join(map(str, result)))
```

The final result is:

```text
HELLO,84,False,null_value,4,2
```

---

# `isinstance()` vs `type()`

Both solutions work for this challenge, but they behave differently.

### `isinstance()`

```python
isinstance(value, str)
```

Checks whether an object is an instance of a type or one of its subclasses.

It is generally more flexible and is commonly preferred when checking types in Python.

### `type()`

```python
type(value) is str
```

Checks whether the object has exactly the specified type.

It does not handle subclasses in the same way as `isinstance()`.

For this challenge, both approaches produce:

```text
HELLO,84,False,null_value,4,2
```

**Key takeaway:** `json.loads()` converts JSON values into native Python objects. Once parsed, you can use `isinstance()` or `type()` to determine the type of each value and perform the appropriate operation.

## Boolean values as numbers:

In Python, `bool` is a subclass of `int`. This means Boolean values have a numeric representation:

```python
True  = 1
False = 0
```

Because of this relationship, Boolean values can participate in mathematical operations just like integers.

For example:

```python
print(True + 1)
```

produces:

```text
2
```

And:

```python
print(False + 1)
```

produces:

```text
1
```

Multiplication works the same way:

```python
print(True * 2)
```

produces:

```text
2
```

because it is equivalent to:

```python
1 * 2
```

Similarly:

```python
print(False * 2)
```

produces:

```text
0
```

because it is equivalent to:

```python
0 * 2
```

### Why Is `bool` a Subclass of `int`?

Python was designed so that Boolean values can naturally be used in situations where numeric values are expected.

For example:

```python
print(isinstance(True, int))
```

outputs:

```text
True
```

This confirms that `True` is considered an instance of `int`.

However, `True` and `False` are still Boolean values:

```python
print(type(True))
```

outputs:

```text
<class 'bool'>
```

So the relationship can be understood as:

```text
bool
 └── int
      ├── True  → 1
      └── False → 0
```

### Important Rule

Whenever a Boolean is used in a numeric context:

```text
True  → 1
False → 0
```

Therefore:

```text
True  +  True  = 2
True  +  False = 1
False + False  = 0
```

and:

```text
True  *  2 = 2
False *  2 = 0
```

This behavior is a built-in feature of Python and is useful when Boolean values need to be counted or used in mathematical calculations.

# Custom JSON Decoding

Custom JSON decoding is an advanced feature of Python's `json` module that allows you to control how JSON data is converted into Python objects. This is particularly useful when dealing with complex data structures or when you want to create specific Python objects from JSON data.

### The JSONDecoder Class

To implement custom JSON decoding, you need to subclass the `json.JSONDecoder` class and override its `object_hook` method:

```python
import json

class CustomDecoder(json.JSONDecoder):
    def object_hook(self, dct):
        # Custom decoding logic here
        return dct
```

### Using the Custom Decoder

Once you've defined your custom decoder, you can use it with `json.loads()` or `json.load()`:

```python
decoded_object = json.loads(json_string, cls=CustomDecoder)
```

The `cls` parameter tells `json.loads()` which custom decoder class to use.

When the JSON is decoded, the `object_hook()` method can inspect each JSON object and decide whether it should remain a dictionary or be converted into a custom Python object.

### Example: Decoding to Custom Objects

Let's look at a practical example where we decode JSON data into custom Python objects:

```python
import json
from datetime import datetime

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

class CustomDecoder(json.JSONDecoder):
    def object_hook(self, dct):
        if 'name' in dct and 'birthdate' in dct:
            return Person(dct['name'], datetime.fromisoformat(dct['birthdate']))
        return dct

json_string = '{"name": "Alice", "birthdate": "1990-05-15"}'
person = json.loads(json_string, cls=CustomDecoder)

print(type(person))  # Output: <class '__main__.Person'>
print(person.name)   # Output: Alice
print(person.birthdate)  # Output: 1990-05-15 00:00:00
```

In this example, `object_hook()` checks whether the decoded dictionary contains both `"name"` and `"birthdate"`.

If both keys exist, it creates a `Person` object instead of returning the dictionary.

The `birthdate` string is also converted into a Python `datetime` object using `datetime.fromisoformat()`.

If the dictionary does not contain the required keys, `return dct` leaves it as a normal dictionary.

### Key Points

* The `object_hook` method is called for each decoded object.
* You can check for specific keys or patterns to determine how to decode the object.
* Return the object as-is if no custom decoding is needed for that particular structure.
* Custom decoders are useful for creating domain-specific objects directly from JSON data.

By using custom JSON decoders, you can seamlessly integrate JSON data into your Python application's object model, making data deserialization more flexible and aligned with your specific needs.

---

# Challenge

**Difficulty: Easy**

Create a custom JSON decoder for a weather data system. The decoder should convert JSON strings into `WeatherData` objects with specific attributes and conversions.

Implement the following:

1. Define a `WeatherData` class with attributes: `location`, `temperature`, `humidity`, and `conditions`.
2. Create a custom `JSONDecoder` subclass that:

   * Converts temperature from Fahrenheit to Celsius, rounded to one decimal place.
   * Ensures humidity is represented as a percentage (e.g., `0.65` becomes `65%`).
   * Capitalizes each word in the conditions string.
3. Implement a function that takes a JSON string, uses the custom decoder to parse it, and returns a formatted string with the weather data.

The following input will be provided:

```json
{"location": "new york", "temperature": 72, "humidity": 0.65, "conditions": "partly cloudy"}
```

Print the resulting formatted string in the following format:

```text
"Location: [location], Temperature: [temp]°C, Humidity: [humidity], Conditions: [conditions]"
```

---

# Solution

```python
import json


class WeatherData:
    def __init__(self, location, temperature, humidity, conditions):
        self.location = location
        self.temperature = temperature
        self.humidity = humidity
        self.conditions = conditions


class WeatherDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        # Explicitly pass object_hook so it isn't set to None
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if all(key in dct for key in ["location", "temperature", "humidity", "conditions"]):
            location = dct["location"].title()
            temperature = round((dct["temperature"] - 32) * 5 / 9, 1)
            humidity = round(dct["humidity"] * 100)
            conditions = dct["conditions"].title()

            return WeatherData(
                location,
                temperature,
                humidity,
                conditions
            )

        return dct


def format_weather(json_string):
    weather = json.loads(json_string, cls=WeatherDecoder)

    return (
        f"Location: {weather.location}, Temperature: {weather.temperature}°C, Humidity: {weather.humidity}%, Conditions: {weather.conditions}"
    )


json_string = '{"location": "new york", "temperature": 72, "humidity": 0.65, "conditions": "partly cloudy"}'

print(format_weather(json_string))
```

## Explanation of the Solution

### 1. Import the `json` module

```python
import json
```

The `json` module provides the tools needed to decode JSON data.

We specifically need:

* `json.JSONDecoder` to create our custom decoder.
* `json.loads()` to convert the JSON string into a Python object.

---

### 2. Create the `WeatherData` class

```python
class WeatherData:
    def __init__(self, location, temperature, humidity, conditions):
        self.location = location
        self.temperature = temperature
        self.humidity = humidity
        self.conditions = conditions
```

The `WeatherData` class represents the weather information as a Python object.

It has four attributes:

```text
location
temperature
humidity
conditions
```

For example, after decoding, we want to have an object similar to:

```python
weather.location
weather.temperature
weather.humidity
weather.conditions
```

---

### 3. Create the custom `JSONDecoder`

```python
class WeatherDecoder(json.JSONDecoder):
```

`WeatherDecoder` inherits from Python's built-in `json.JSONDecoder`.

Inheritance allows us to customize the normal JSON decoding behavior.

The important part of this custom decoder is the `object_hook()` method.

---

### 4. Customize the decoder's `__init__()` method

```python
def __init__(self, *args, **kwargs):
    # Explicitly pass object_hook so it isn't set to None
    super().__init__(object_hook=self.object_hook, *args, **kwargs)
```

This part is important because it explicitly tells the parent `JSONDecoder` to use our custom `object_hook()` method.

Normally, `JSONDecoder` can receive an `object_hook` argument when it is created.

Here, we explicitly pass:

```python
object_hook=self.object_hook
```

This means:

> "Whenever the JSON decoder creates a dictionary from a JSON object, call my `object_hook()` method with that dictionary."

### What are `*args` and `**kwargs`?

```python
*args
```

collects additional positional arguments.

```python
**kwargs
```

collects additional keyword arguments.

They allow our custom decoder to accept the normal arguments that a `JSONDecoder` can receive.

Then:

```python
super().__init__(...)
```

calls the `__init__()` method of the parent `json.JSONDecoder` class.

So this line:

```python
super().__init__(object_hook=self.object_hook, *args, **kwargs)
```

initializes the normal JSON decoder while also registering our custom `object_hook()`.

---

### 5. Define `object_hook()`

```python
def object_hook(self, dct):
```

The `object_hook()` method receives a dictionary whenever a JSON object is decoded.

For the challenge, the JSON:

```json
{"location": "new york", "temperature": 72, "humidity": 0.65, "conditions": "partly cloudy"}
```

is initially represented as a Python dictionary:

```python
{
    "location": "new york",
    "temperature": 72,
    "humidity": 0.65,
    "conditions": "partly cloudy"
}
```

That dictionary is passed to:

```python
object_hook(self, dct)
```

where `dct` contains the decoded data.

---

### 6. Check for all required keys

```python
if all(key in dct for key in ["location", "temperature", "humidity", "conditions"]):
```

This checks whether all four required keys exist in the dictionary.

The required keys are:

```text
location
temperature
humidity
conditions
```

The `all()` function returns `True` only if every condition is `True`.

So this:

```python
all(key in dct for key in ["location", "temperature", "humidity", "conditions"])
```

essentially asks:

> Does `dct` contain `location`, `temperature`, `humidity`, and `conditions`?

If all four exist, we know that the dictionary represents weather data.

---

### 7. Format the location

```python
location = dct["location"].title()
```

The `.title()` method capitalizes the first letter of each word.

The input is:

```text
new york
```

After `.title()`:

```text
New York
```

So the location is converted from:

```text
"new york"
```

to:

```text
"New York"
```

---

### 8. Convert Fahrenheit to Celsius

```python
temperature = round((dct["temperature"] - 32) * 5 / 9, 1)
```

The formula for converting Fahrenheit to Celsius is:

```text
Celsius = (Fahrenheit - 32) × 5 / 9
```

The input temperature is:

```text
72°F
```

So:

```text
(72 - 32) × 5 / 9
```

which gives approximately:

```text
22.222...
```

The `round()` function rounds the result to one decimal place:

```python
round(..., 1)
```

Therefore:

```text
22.2
```

is stored in `temperature`.

---

### 9. Convert humidity to a percentage

```python
humidity = round(dct["humidity"] * 100)
```

The JSON contains humidity as:

```text
0.65
```

To convert this decimal into a percentage, multiply it by `100`:

```text
0.65 × 100 = 65
```

Therefore, `humidity` becomes:

```text
65
```

The `%` symbol is added later when the final string is created.

---

### 10. Format the weather conditions

```python
conditions = dct["conditions"].title()
```

The input is:

```text
partly cloudy
```

Using `.title()` changes it to:

```text
Partly Cloudy
```

So the conditions are stored in a more readable format.

---

### 11. Create the `WeatherData` object

```python
return WeatherData(
    location,
    temperature,
    humidity,
    conditions
)
```

After all the conversions are complete, a `WeatherData` object is created.

The object receives:

```text
location     → New York
temperature  → 22.2
humidity     → 65
conditions   → Partly Cloudy
```

Instead of returning the original dictionary, `object_hook()` returns this custom object.

This is the main purpose of custom JSON decoding.

---

### 12. Return other dictionaries unchanged

```python
return dct
```

If the dictionary does not contain all four weather-related keys, it is returned unchanged.

This is important because `object_hook()` can be called for every JSON object encountered during decoding.

For example, if a JSON object is unrelated to weather data, we do not want to convert it into a `WeatherData` object.

---

### 13. Create the `format_weather()` function

```python
def format_weather(json_string):
```

This function receives the JSON string and handles the decoding and formatting.

---

### 14. Decode using the custom decoder

```python
weather = json.loads(json_string, cls=WeatherDecoder)
```

The `cls` parameter tells `json.loads()` to use our `WeatherDecoder`.

Without `cls=WeatherDecoder`, Python would normally use the default JSON decoder.

With:

```python
cls=WeatherDecoder
```

the custom decoder is used.

The process is:

```text
JSON string
    ↓
json.loads()
    ↓
WeatherDecoder
    ↓
object_hook()
    ↓
WeatherData object
```

Therefore, `weather` becomes a `WeatherData` object.

---

### 15. Create the formatted string

```python
return (
    f"Location: {weather.location}, Temperature: {weather.temperature}°C, Humidity: {weather.humidity}%, Conditions: {weather.conditions}"
)
```

The attributes of the `WeatherData` object are accessed using dot notation:

```python
weather.location
weather.temperature
weather.humidity
weather.conditions
```

The values are then inserted into the required output format.

The final result is:

```text
Location: New York, Temperature: 22.2°C, Humidity: 65%, Conditions: Partly Cloudy
```

---

### 16. Create the JSON input

```python
json_string = '{"location": "new york", "temperature": 72, "humidity": 0.65, "conditions": "partly cloudy"}'
```

This variable contains the JSON string that will be decoded.

The values are:

```text
location     → new york
temperature  → 72°F
humidity     → 0.65
conditions   → partly cloudy
```

---

### 17. Call the function

```python
print(format_weather(json_string))
```

The JSON string is passed to `format_weather()`.

The function:

1. Decodes the JSON using `WeatherDecoder`.
2. Converts the dictionary into a `WeatherData` object.
3. Converts Fahrenheit to Celsius.
4. Converts humidity to a percentage.
5. Capitalizes the location and conditions.
6. Creates the final formatted string.
7. Returns that string.
8. `print()` displays it.

The output is:

```text
Location: New York, Temperature: 22.2°C, Humidity: 65%, Conditions: Partly Cloudy
```

---

## Complete Flow

```text
JSON string
    ↓
json.loads(json_string, cls=WeatherDecoder)
    ↓
WeatherDecoder.__init__()
    ↓
object_hook() is registered
    ↓
JSON object becomes a dictionary
    ↓
object_hook(dct)
    ↓
Check for required weather keys
    ↓
Location → "New York"
Temperature → 72°F → 22.2°C
Humidity → 0.65 → 65%
Conditions → "Partly Cloudy"
    ↓
WeatherData object
    ↓
format_weather()
    ↓
Formatted string
```

## Key Idea

The most important concept in this example is that **`object_hook()` allows us to customize what Python creates from a JSON object**.

Normally:

```text
JSON object → Python dictionary
```

With the custom decoder:

```text
JSON object
    ↓
object_hook()
    ↓
WeatherData object
```

The custom decoder therefore lets us perform transformations during deserialization instead of manually processing the dictionary after `json.loads()` has finished.
