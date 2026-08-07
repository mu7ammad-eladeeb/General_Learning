# Opening Files in Python

Before you can perform any operation on a file, such as reading its contents, writing new data, or updating existing data, you must first **open** the file.

Python provides a built-in function called `open()` for this purpose.

## Syntax

```python
f = open("hello.txt")
```

## Explanation

- `open()` is a built-in Python function used to open a file.
- `"hello.txt"` is the name of the file you want to open.
- `f` is a **file object** (also called a file handle) that represents the opened file.
- Once the file is opened, you can use the file object (`f`) to perform different operations such as:
  - Reading data from the file.
  - Writing data into the file.
  - Appending new data.
  - Closing the file.

## Breaking Down the Statement

```python
f = open("hello.txt")
```

### `open()`

The `open()` function opens the specified file and returns a file object.

### `"hello.txt"`

This is the filename.

If the file is located in the same folder as your Python program, specifying only the filename is enough.

### `f`

The returned file object is stored in the variable `f`.

This variable is used to access the file and perform operations on it.

## Example

```python
f = open("hello.txt")
print(f)
```

### Possible Output

```python
<_io.TextIOWrapper name='hello.txt' mode='r' encoding='UTF-8'>
```

The output shows information about the opened file object.

## Why Do We Need to Open a File?

A file must be opened before Python can interact with it.

Opening a file creates a connection between your Python program and the file stored on disk. Through this connection, Python can:

- Read data from the file.
- Write new data into the file.
- Modify existing content (depending on the opening mode).

Without opening the file first, none of these operations are possible.

## Important Note

When you call:

```python
f = open("hello.txt")
```

Python opens the file using the **default mode**, which is **read mode (`"r"`)**.

This means Python expects the file to already exist and prepares it for reading.

The different file modes (such as read, write, append, etc.) will be discussed separately.

# Read from a File in Python

After opening a file, you can read its contents using the `read()` method.

## Syntax

```python
f = open("coddy.txt")
s = f.read()
```

### Explanation

- `open("coddy.txt")` opens the file named **coddy.txt** in **read mode** by default.
- `f.read()` reads **all the contents** of the file.
- The returned content is stored in the variable `s`.

## Example

```python
f = open("coddy.txt")
s = f.read()
print(s)
```

### Example File (`coddy.txt`)

```text
Hello, World!
Welcome to Python.
```

### Output

```text
Hello, World!
Welcome to Python.
```

---

# Challenge

## Problem

Given the file named **`a.txt`**, read its contents and print them.

## Solution

```python
f = open("a.txt")
print(f.read())
```

### Explanation

- Open the file **`a.txt`**.
- Use `read()` to read the entire file.
- Pass the result directly to `print()` to display the file's contents.

# File Open Modes in Python

When opening a file, you can specify how you want to use it by providing a **mode** as the second argument to the `open()` function.

## Syntax

```python
open(filename, mode)
```

- `filename` is the name (or path) of the file.
- `mode` determines how the file will be opened.

---

# File Modes

| Mode | Key | Description |
|------|-----|-------------|
| Read | `'r'` | Opens a file for reading. |
| Append | `'a'` | Opens a file for appending (adding content to the end of the file). |
| Write | `'w'` | Opens a file for writing. Existing contents are overwritten. |
| Create | `'x'` | Creates a new file. Raises an error if the file already exists. |

> **Note:** If the file does **not** exist, all modes will create the file **except** **read mode (`'r'`)**.

---

# Text and Binary Modes

You can also specify whether the file should be opened in **text** or **binary** mode.

| Mode | Key | Description |
|------|-----|-------------|
| Text | `'t'` | Opens the file in text mode. |
| Binary | `'b'` | Opens the file in binary mode. |

---

# Examples

## Open a file in append mode

```python
open("data.csv", "a")
```

Opens `data.csv` and appends new data to the end of the file.

---

## Open a file in write and binary mode

```python
open("foo.txt", "wb")
```

Opens `foo.txt` for writing in binary mode.

---

## Open a file in read and write mode

```python
open("bar.txt", "rw")
```

Opens `bar.txt` for both reading and writing.

---

# Default Mode

If no mode is specified, Python uses **read text mode (`'rt'`)** by default.

These two statements are equivalent:

```python
open("a.txt")
```

```python
open("a.txt", "rt")
```

Both open `a.txt` for reading in text mode.

# Writing to Files in Python

To write data into a file, you must open it in **write (`'w'`)** mode or **append (`'a'`)** mode.

## Write vs Append

| Mode | Description |
|------|-------------|
| `'w'` | Writes to the file. If the file already exists, **all existing content is overwritten**. If the file does not exist, it is created. |
| `'a'` | Appends (adds) new content to the **end** of the file. Existing content is preserved. If the file does not exist, it is created. |

---

# Writing with `write()`

Use the `write()` method to write text into a file.

## Syntax

```python
f = open("a.txt", "w")
f.write("Some text")
```

### Explanation

- `open("a.txt", "w")` opens the file in write mode.
- `write("Some text")` writes the given text into the file.
- If `a.txt` already contains data, it will be **replaced** with `"Some text"`.

---

# Example: Write Mode (`'w'`)

```python
f = open("notes.txt", "w")
f.write("Python is fun!")
```

### Result (`notes.txt`)

```text
Python is fun!
```

If `notes.txt` previously contained:

```text
Hello
Welcome
```

After running the code, it becomes:

```text
Python is fun!
```

---

# Example: Append Mode (`'a'`)

```python
f = open("notes.txt", "a")
f.write("\nKeep practicing!")
```

### Before

```text
Python is fun!
```

### After

```text
Python is fun!
Keep practicing!
```

Notice that the existing content remains unchanged, and the new text is added to the end of the file.

---

# Challenge

## Problem

The file **`c.txt`** initially contains:

```text
Hello World
```

Modify the file so that it finally contains:

```text
Hello World!
```

You may use either **append** mode or **write** mode.

---

## Solution 1: Using Append Mode (Recommended)

```python
f = open("c.txt", "a")
f.write("!")
```

### Result

```text
Hello World!
```

Since the file already contains `Hello World`, append mode simply adds the missing exclamation mark.

---

## Solution 2: Using Write Mode

```python
f = open("c.txt", "w")
f.write("Hello World!")
```

### Result

```text
Hello World!
```

This solution also works, but it **overwrites** the entire file before writing the new text.

# Creating Files in Python

Python can create a new file using the `open()` function with one of the following modes:

- **Append (`'a'`)**
- **Write (`'w'`)**
- **Create (`'x'`)**

## Syntax

```python
open(filename, mode)
```

---

# File Creation Modes

| Mode | Description |
|------|-------------|
| `'a'` | Opens a file for appending. If the file does not exist, it is created. |
| `'w'` | Opens a file for writing. If the file does not exist, it is created. If it already exists, its contents are overwritten. |
| `'x'` | Creates a new file. If the file already exists, Python raises a `FileExistsError`. |

---

# Example: Create a File Using Append Mode

```python
f = open("notes.txt", "a")
```

If `notes.txt` does not exist, Python creates it.

---

# Example: Create a File Using Write Mode

```python
f = open("report.txt", "w")
```

If `report.txt` does not exist, Python creates it.

If it already exists, its contents are erased before writing new data.

---

# Example: Create a File Using Create Mode

```python
f = open("data.txt", "x")
```

This creates a new file named `data.txt`.

If `data.txt` already exists, Python raises an error:

```text
FileExistsError: [Errno 17] File exists: 'data.txt'
```

---

# Summary

| Mode | Creates File if Missing | Overwrites Existing File | Raises Error if File Exists |
|------|:-----------------------:|:------------------------:|:---------------------------:|
| `'a'` | ✅ | ❌ | ❌ |
| `'w'` | ✅ | ✅ | ❌ |
| `'x'` | ✅ | ❌ | ✅ |

# Deleting Files in Python

Sometimes you need to delete a file from your computer using Python.

To do this, use the **`os`** module and its **`remove()`** function.

## Syntax

```python
import os

os.remove("filename")
```

- `import os` imports Python's built-in **os** module.
- `os.remove()` deletes the specified file.

---

# Example

Delete a file named `a.txt`:

```python
import os

os.remove("a.txt")
```

If `a.txt` exists, it will be permanently deleted.

---

# Another Example

Delete a file named `notes.txt`:

```python
import os

os.remove("notes.txt")
```

---

# Important Note

If the specified file does **not** exist, Python raises a `FileNotFoundError`.

Example:

```python
import os

os.remove("missing.txt")
```

### Output

```text
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
```

# More Ways to Read Files in Python

In addition to the basic `read()` method, Python provides several other ways to read data from a file.

---

# Read a Specific Number of Characters

You can specify how many characters you want to read by passing a number to `read()`.

## Syntax

```python
f = open("file.txt")
s = f.read(10)
```

### Explanation

- `f.read(10)` reads only the **first 10 characters** from the file.
- The characters are stored in the variable `s`.

### Example

Suppose `file.txt` contains:

```text
Hello Python Programming
```

```python
f = open("file.txt")
print(f.read(10))
```

### Output

```text
Hello Pyth
```

---

# Read One Line at a Time with `readline()`

The `readline()` method reads **one line** from the file each time it is called.

## Example

```python
f = open("file.txt")

print(f.readline())
print(f.readline())
```

If `file.txt` contains:

```text
Apple
Banana
Cherry
```

### Output

```text
Apple

Banana
```

The first call reads the first line, and the second call reads the next line.

---

# Read All Lines with `readlines()`

The `readlines()` method reads **all lines** from a file and returns them as a list of strings.

## Example

```python
f = open("file.txt")
print(f.readlines())
```

If `file.txt` contains:

```text
Apple
Banana
Cherry
```

### Output

```python
['Apple\n', 'Banana\n', 'Cherry']
```

Each element in the list represents one line from the file.

---

# Loop Through a File Line by Line

You can iterate over a file directly using a `for` loop.

## Example

```python
f = open("file.txt")

for line in f:
    print(line)
```

If `file.txt` contains:

```text
Apple
Banana
Cherry
```

### Output

```text
Apple
Banana
Cherry
```

This approach is commonly used when processing large files because it reads the file one line at a time.

---

# Challenge

## Problem

A file named **`numbers.txt`** contains one number on each line.

Your task is to:

1. Read the file **line by line**.
2. Print **only the even numbers** (numbers divisible by `2`).

> **Note:** When reading from a file, each line is returned as a **string**. Convert it to an integer using `int()` before performing arithmetic operations.

---

# Solution

```python
f = open("numbers.txt")

for line in f:
    if int(line) % 2 == 0:
        print(int(line))
```

### Explanation

- Open `numbers.txt`.
- Read the file one line at a time using a `for` loop.
- Convert each line from a string to an integer with `int(line)`.
- Check whether the number is even using `number % 2 == 0`.
- Print the number if the condition is true.
