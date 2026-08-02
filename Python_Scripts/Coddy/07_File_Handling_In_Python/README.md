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
