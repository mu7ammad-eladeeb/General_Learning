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

# Closing Files in Python

It is good practice to **close a file after opening it**.

Closing a file releases the resources associated with it and ensures that the file is properly finished with.

---

# Using `close()`

You can close an opened file using the `close()` method.

## Example

```python
f = open("a.txt")
f.close()
```

### Explanation

- `open("a.txt")` opens the file.
- `f.close()` closes the file after you finish working with it.

If you perform operations on the file, close it afterward:

```python
f = open("a.txt")

print(f.read())

f.close()
```

---

# Using `with`

Python also provides a better and safer way to work with files by using the **`with` statement**.

## Syntax

```python
with open("a.txt") as f:
    # perform operations on f
```

The file is automatically closed when the `with` block finishes.

## Example

```python
with open("a.txt") as f:
    print(f.read())
```

You do **not** need to call `f.close()` yourself.

---

# Why Use `with`?

Using `with` automatically handles closing the file, even when you finish the operations inside the block.

### Without `with`

```python
f = open("a.txt")

print(f.read())

f.close()
```

### With `with`

```python
with open("a.txt") as f:
    print(f.read())
```

The `with` statement is generally preferred because it makes file handling simpler and helps ensure that the file is closed properly.

---

# Summary

| Method | File Closed Automatically? |
|--------|-----------------------------|
| `f.close()` | ❌ No, you must call it manually |
| `with open(...) as f:` | ✅ Yes |

# Practice #2 — Average Word Length

## Challenge

**Difficulty:** Medium

Write a function named `average_word_length` which gets a **filename** as an argument and returns the **average word length**, rounded to **two decimal places**, in the file.

For example, if `input1.txt` contains:

```text
The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away.
```

Then:

```python
average_word_length("input1.txt")
```

should return:

```text
3.71
```

> **Note:** Remove any punctuation before calculating the word lengths.

---

# Hints

## Hint 1

Remove these punctuation characters from the words:

```text
! ? ' " , .
```

Instead of completely removing the punctuation, replace each punctuation character with a **space**.

For example:

```python
text = text.replace(",", " ")
```

This changes:

```text
Hello,World
```

into:

```text
Hello World
```

This is useful because replacing punctuation with a space prevents words from being joined together.

---

## Hint 2

Use the `round()` function to round the result to two decimal places:

```python
round(res, 2)
```

Here, `res` is the calculated average.

---

# Solution

```python
def average_word_length(filename):
    with open(filename) as f:
        text = f.read()

    punctuation = "!?'\".,"

    for char in punctuation:
        text = text.replace(char, " ")

    words = text.split()
    total_length = sum(len(word) for word in words)

    return round(total_length / len(words), 2)
```

---

# Explanation

## 1. Define the Function

```python
def average_word_length(filename):
```

The function is named `average_word_length`.

It accepts one argument:

```python
filename
```

This represents the name of the file containing the text.

For example:

```python
average_word_length("input1.txt")
```

---

## 2. Open the File

```python
with open(filename) as f:
```

The `open()` function opens the specified file.

The file is opened in **read mode** by default.

The `with` statement automatically closes the file after the operations inside the block are finished.

---

## 3. Read the File

```python
text = f.read()
```

This reads the entire contents of the file and stores them in the variable `text`.

For example:

```text
The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away.
```

is stored as one string.

---

## 4. Define the Punctuation

```python
punctuation = "!?'\".,"
```

The string contains the punctuation characters that should be replaced:

```text
! ? ' " , .
```

Each character will be processed separately.

---

## 5. Replace Punctuation with Spaces

```python
for char in punctuation:
    text = text.replace(char, " ")
```

The `for` loop goes through each punctuation character.

For example:

```python
text = text.replace(",", " ")
```

replaces every comma with a space.

So:

```text
Hello,World
```

becomes:

```text
Hello World
```

Similarly:

```text
dog. barks, and fox!
```

becomes:

```text
dog  barks  and fox
```

Replacing punctuation with a space is important because simply removing punctuation could accidentally join two words together.

For example, removing the comma from:

```text
Hello,World
```

would produce:

```text
HelloWorld
```

But replacing it with a space produces the correct result:

```text
Hello World
```

---

## 6. Split the Text into Words

```python
words = text.split()
```

The `split()` method separates the text into individual words.

For example:

```python
"The quick brown fox"
```

becomes:

```python
["The", "quick", "brown", "fox"]
```

Because `split()` without an argument handles whitespace, multiple spaces are not a problem.

---

## 7. Calculate the Total Length

```python
total_length = sum(len(word) for word in words)
```

`len(word)` gives the number of characters in each word.

For example:

```python
len("The")
```

returns:

```text
3
```

The `sum()` function adds the lengths of all the words together.

For example:

```text
The    → 3
quick  → 5
brown  → 5
fox    → 3
```

The total is:

```text
3 + 5 + 5 + 3 = 16
```

---

## 8. Calculate the Average

```python
total_length / len(words)
```

The average word length is calculated by dividing the total number of characters by the number of words.

The formula is:

```text
Average Word Length =
Total Length of All Words / Number of Words
```

`len(words)` gives the number of words.

---

## 9. Round the Result

```python
round(total_length / len(words), 2)
```

The `round()` function rounds the result to **two decimal places**.

For example:

```python
round(3.714285, 2)
```

returns:

```text
3.71
```

The function returns this value.

---

# Complete Flow

The program processes the file in these steps:

```text
Read the file
     ↓
Replace punctuation with spaces
     ↓
Split the text into words
     ↓
Find the length of every word
     ↓
Add all word lengths
     ↓
Divide by the number of words
     ↓
Round to 2 decimal places
     ↓
Return the average
```

# Practice #3

## Challenge

**Difficulty:** Medium

Write a Python program that reads a CSV file named `scores.txt`, determines the highest score in each subject, identifies the student who achieved that score, and displays the results in a readable format.

## Tasks

1. Read the sample CSV file named `scores.txt`.
2. Determine the **highest score** in each subject.
3. Determine the **student who achieved** the highest score in each subject.
4. Display the calculated information in the required format.

## Sample CSV File — `scores.txt`

```text
Name,Math,Science,History
Alice,85,90,78
Bob,92,78,85
Carol,78,92,88
David,88,82,90
Eve,95,88,75
```

## Expected Output

```text
Highest Scores:
Math: Eve (95)
Science: Carol (92)
History: David (90)
```

---

# Solution

```python
with open("scores.txt", "r") as f:
    master = [line.strip().split(",") for line in f.readlines() if line.strip()]

headers = master[0]
subjects = headers[1:]
rows = master[1:]

row_dic = {}

for col_idx, subject in enumerate(subjects, start=1):
    max_score = -1
    top_student = ""

    for row in rows:
        stud_name = row[0]
        score = int(row[col_idx])

        if score > max_score:
            max_score = score
            top_student = stud_name

    row_dic[subject] = (top_student, max_score)

print("Highest Scores:")

for sub, (student, score) in row_dic.items():
    print(f"{sub}: {student} ({score})")
```

---

# Explanation

## 1. Open the file

```python
with open("scores.txt", "r") as f:
```

`open()` opens the `scores.txt` file in **read mode**.

The `"r"` means **read**.

Using `with` ensures that the file is automatically closed after we finish working with it.

---

## 2. Read and process all lines

```python
master = [line.strip().split(",") for line in f.readlines() if line.strip()]
```

This is a **list comprehension** that performs several operations at once.

### `f.readlines()`

Reads all lines from the file.

For example:

```text
Name,Math,Science,History
Alice,85,90,78
Bob,92,78,85
...
```

### `if line.strip()`

This ignores empty lines.

### `line.strip()`

Removes whitespace and the newline character (`\n`) from the beginning and end of each line.

For example:

```python
"Alice,85,90,78\n"
```

becomes:

```python
"Alice,85,90,78"
```

### `.split(",")`

Splits each line wherever a comma appears.

For example:

```python
"Alice,85,90,78".split(",")
```

becomes:

```python
["Alice", "85", "90", "78"]
```

Therefore, `master` becomes:

```python
[
    ["Name", "Math", "Science", "History"],
    ["Alice", "85", "90", "78"],
    ["Bob", "92", "78", "85"],
    ["Carol", "78", "92", "88"],
    ["David", "88", "82", "90"],
    ["Eve", "95", "88", "75"]
]
```

---

## 3. Get the headers

```python
headers = master[0]
```

The first row contains the column names:

```python
["Name", "Math", "Science", "History"]
```

So:

```python
headers[0]  # "Name"
headers[1]  # "Math"
headers[2]  # "Science"
headers[3]  # "History"
```

---

## 4. Get the subjects

```python
subjects = headers[1:]
```

We don't need `"Name"` because it isn't a subject.

`headers[1:]` starts from index `1` and takes everything after it.

The result is:

```python
["Math", "Science", "History"]
```

---

## 5. Get the student rows

```python
rows = master[1:]
```

Again, we don't need the first row because it contains the headers.

`master[1:]` gives us:

```python
[
    ["Alice", "85", "90", "78"],
    ["Bob", "92", "78", "85"],
    ["Carol", "78", "92", "88"],
    ["David", "88", "82", "90"],
    ["Eve", "95", "88", "75"]
]
```

---

## 6. Create a dictionary

```python
row_dic = {}
```

This dictionary will store the highest-scoring student and their score for each subject.

Eventually, it will contain something like:

```python
{
    "Math": ("Eve", 95),
    "Science": ("Carol", 92),
    "History": ("David", 90)
}
```

---

## 7. Loop through the subjects

```python
for col_idx, subject in enumerate(subjects, start=1):
```

`enumerate()` gives us both:

* the **index** of the subject
* the **subject name**

Because we use `start=1`, the indexes match the positions in each student row.

The loop produces:

```text
1 → Math
2 → Science
3 → History
```

This is useful because the score for Math is at index `1`, Science at index `2`, and History at index `3`.

---

## 8. Initialize the highest score

```python
max_score = -1
top_student = ""
```

For every subject, we start with:

```python
max_score = -1
```

This means we haven't found a score yet.

We also start with an empty student name:

```python
top_student = ""
```

As we examine the students, these values will be updated.

---

## 9. Loop through all students

```python
for row in rows:
```

For the Math subject, for example, the program checks every row:

```text
Alice
Bob
Carol
David
Eve
```

---

## 10. Get the student's name

```python
stud_name = row[0]
```

The first item in every row is the student's name.

For example:

```python
row = ["Alice", "85", "90", "78"]
```

Then:

```python
row[0]
```

is:

```text
Alice
```

---

## 11. Get the student's score

```python
score = int(row[col_idx])
```

`col_idx` tells us which subject we're currently processing.

For example, when processing Math:

```python
col_idx = 1
```

So:

```python
row[1]
```

gets the Math score.

Because the value came from a text file, it is initially a string:

```python
"85"
```

`int()` converts it into an integer:

```python
85
```

This allows us to compare scores numerically.

---

## 12. Check for a new highest score

```python
if score > max_score:
    max_score = score
    top_student = stud_name
```

If the current score is greater than the highest score found so far, we update both variables.

For Math, the process is:

```text
Alice → 85
```

Since `85 > -1`:

```python
max_score = 85
top_student = "Alice"
```

Then:

```text
Bob → 92
```

Since `92 > 85`:

```python
max_score = 92
top_student = "Bob"
```

Then:

```text
Carol → 78
```

Since `78 > 92` is false, nothing changes.

Then:

```text
David → 88
```

Again, nothing changes.

Finally:

```text
Eve → 95
```

Since `95 > 92`:

```python
max_score = 95
top_student = "Eve"
```

So the highest Math score is:

```text
Eve (95)
```

---

## 13. Store the result in the dictionary

```python
row_dic[subject] = (top_student, max_score)
```

After finishing all students for a particular subject, the result is stored in the dictionary.

For Math:

```python
row_dic["Math"] = ("Eve", 95)
```

After processing all subjects, the dictionary becomes:

```python
{
    "Math": ("Eve", 95),
    "Science": ("Carol", 92),
    "History": ("David", 90)
}
```

The value for each subject is a **tuple** containing:

```text
(student name, highest score)
```

---

## 14. Display the heading

```python
print("Highest Scores:")
```

This prints:

```text
Highest Scores:
```

---

## 15. Loop through the dictionary

```python
for sub, (student, score) in row_dic.items():
```

`.items()` gives us both the dictionary key and its value.

For example:

```python
"Math", ("Eve", 95)
```

The tuple is unpacked directly into:

```python
student = "Eve"
score = 95
```

So the loop effectively gives us:

```text
sub = "Math"
student = "Eve"
score = 95
```

and then:

```text
sub = "Science"
student = "Carol"
score = 92
```

and:

```text
sub = "History"
student = "David"
score = 90
```

---

## 16. Print the final result

```python
print(f"{sub}: {student} ({score})")
```

An **f-string** allows us to insert the variables directly into the string.

For example:

```python
sub = "Math"
student = "Eve"
score = 95
```

produces:

```text
Math: Eve (95)
```

## Final Output

```text
Highest Scores:
Math: Eve (95)
Science: Carol (92)
History: David (90)
```

## Key Ideas Used

* `open()` — opens the file.
* `readlines()` — reads all lines.
* `strip()` — removes surrounding whitespace and newline characters.
* `split(",")` — separates CSV values.
* List comprehension — processes the file lines concisely.
* Slicing (`[1:]`) — skips the header row.
* `enumerate()` — provides both an index and a subject name.
* `int()` — converts score strings into integers.
* Dictionary — stores the highest result for each subject.
* Tuple unpacking — extracts the student and score from each dictionary value.
* f-string — formats the final output.
