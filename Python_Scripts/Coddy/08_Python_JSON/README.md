# The `json` Module

The **`json` module** is a built-in Python library that provides functions for working with **JSON (JavaScript Object Notation)** data.

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
