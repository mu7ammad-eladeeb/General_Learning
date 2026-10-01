# What Is The Terminal

The **terminal** is a powerful text-based interface that lets you communicate directly with your computer's operating system.

Instead of clicking buttons and icons, you type commands to navigate files, run programs, and manage your system. Learning the terminal is an essential skill for any developer.

# Your First Command

## Challenge

**Beginner**

Use the `echo` command to print `Hello World!` to the terminal.

> *Remember that the output is **case sensitive**. Make sure your text matches exactly.*

Use the `echo` command followed by your text in double quotes.

## Hints

**Hint 1**

A command line has two parts: the program you run and the argument you pass it. Here the program is `echo` and the argument is your text.

**Hint 2**

Type `echo`, a space, then your text inside double quotes, and press Enter. The text is **case sensitive**, so it has to match the task exactly.

## Solution

    echo "Hello World!"

## Explanation

The `echo` command is used to print text to the terminal.

A command line has two parts:

- `echo` → the **program/command** you run.
- `"Hello World!"` → the **argument** you pass to the command.

The text is written inside **double quotes**, as required by the challenge.

When you run:

    echo "Hello World!"

the terminal prints:

    Hello World!

The output is **case sensitive**, so the capitalization, spaces, and exclamation mark must match the required text exactly.

# **Comments**

**Comments** are lines in your shell script that are ignored by the shell. They are used to add notes and explanations to your code for human understanding.

In the shell, a comment starts with the `#` symbol. Everything after `#` on that line is ignored:

    # This is a comment
    echo "Hello!"  # This also prints Hello!

When you run the above, only `Hello!` is printed: the comments are completely invisible to the shell.

**Common uses for comments:**

**1. Explaining what a command does:**

    # Print a welcome message
    echo "Welcome to the terminal!"

**2. Disabling a command temporarily:**

    # echo "This line is disabled"
    echo "This line will execute"

**3. The Shebang line:**

A special comment at the very top of a shell script tells the system which shell to use:

    #!/bin/bash
    echo "This script runs with Bash"

This line starts with `#!` (called a **shebang**) followed by the path to the shell. It is always the first line of a script.

**4. TODO Comments: mark future tasks:**

    # TODO: Add error handling here
    echo "Processing files..."

# **Print Working Directory**

The `pwd` command stands for **Print Working Directory**. It shows you the **full path** of the directory you are currently in.

When you open a terminal, you start in your **home directory**. The `pwd` command helps you confirm exactly where you are in the filesystem at any moment.

Simply type `pwd` and press Enter:

```bash
pwd

```

The output will look something like this:

```bash
/home

```

This is called a **path**. It shows the full location of your current directory, starting from the **root** of the filesystem (`/`).

**Understanding paths:**

- `/`: the root of the entire filesystem
- `/home`: the home directory

* `/home/documents`: the documents folder inside home

`pwd` is especially useful when you have navigated deep into different folders and need to remember where you are.

# **List Files**

The `ls` command stands for **list**. It shows you all the files and folders inside your current directory.

Simply type `ls` and press Enter:


```python
ls

```

The output will show everything in your current location:


```python
documents
readme.txt

```

**Useful options you can add to `ls`:**

`ls -l`: shows a **detailed list** with file sizes, permissions, and dates:


```python
ls -l

```

`ls -a`: shows **all files**, including hidden files that start with a `.`:


```python
ls -a

```

`ls -la`: combines both options, showing a detailed list of all files including hidden ones:


```python
ls -la

```

You can also list the contents of a **specific folder** by passing its name:


```python
ls documents

```

This shows the contents of the `documents` folder without having to navigate into it first.

# **Change Directory**

The **`cd`** command stands for **Change Directory**. It lets you navigate from one folder to another in the filesystem.

To move into a folder, type **`cd`** followed by the folder name:

```python
cd documents

```

After running this, you are now inside the **`documents`** folder. You can confirm this with **`pwd`**:

```python
/home/documents

```

**Useful ways to use `cd`:**

**`cd ..`**. Move **up one level** to the parent directory:

```python
cd ..

```

**`cd ~`**: go directly to your **home directory** from anywhere:

```python
cd ~

```

**`cd /`**: go to the **root directory**, the very top of the filesystem:

```python
cd /

```

**`cd -`**: go back to the **previous directory** you were in:

```python
cd -

```

**Tip:** You can combine **`cd`** with **`ls`** and **`pwd`** to explore your filesystem confidently: list what's there, move into it, and confirm where you are.

# **Absolute vs Relative Paths**

When navigating the filesystem, you can refer to a location in two ways: using an **absolute path** or a **relative path**.

**Absolute Path**: starts from the **root** of the filesystem (**`/`**). It always points to the same location no matter where you currently are:

```python
cd /home/documents

```

An absolute path always begins with **`/`**.

**Relative Path**: starts from your **current directory**. It depends on where you are right now:

```python
cd documents

```

If you are currently in **`/home`**, this will take you to **`/home/documents`**.

**Comparing the two:**

- If you are in **`/home`** and want to go to **`/home/documents`**:
  Absolute: **`cd /home/documents`**
  Relative: **`cd documents`**

* If you are in **`/home/documents`** and want to go up one level:
  Absolute: **`cd /home`**
  Relative: **`cd ..`**

**Special relative path symbols:**

- **`.`**. Refers to your **current directory**

* **`..`**. Refers to the **parent directory** (one level up)

```python
cd ./documents   # same as: cd documents
cd ..            # go up one level
```

# **Home And Root Directory**

Two of the most important directories in any Unix-based filesystem are the **root directory** and the **home directory**. Understanding the difference between them is important because they represent two very different locations in the filesystem.

**Root Directory (`/`)**

The root directory is the **top of the entire filesystem**. Every file and folder on your system lives somewhere inside it. It is represented by a single forward slash:

```bash
cd /

```

From the root, you can reach any location on the system using an absolute path.

**Home Directory (`~`)**

The home directory is your **personal space** in the filesystem. It is where you normally start when you open a new terminal session. It is represented by the tilde symbol:

```bash
cd ~

```

You can always return to your home directory from anywhere using **`cd ~`** or simply **`cd`** with no arguments:

```bash
cd

```

Your home directory usually contains your personal files and folders, such as documents, downloads, and configuration files.

**Comparing root and home:**

- **`/`**: the root of the whole system. It contains all files and directories on the system.
- **`~`**: your personal home directory. It usually points to **`/home/username`**.

Think of the root as the **entire building**, and your home directory as **your own room inside it**.

You can always check where **`~`** points to by running:

```bash
echo ~

```

For example, if your username is `username`, the command might output:

```bash
/home/username
```

# **Create A File**

The **`touch`** command is used to **create a new empty file** in your current directory.

Simply type **`touch`** followed by the name of the file you want to create:

```bash
touch hello.txt

```

This creates a new empty file called **`hello.txt`**. You can confirm it was created by running **`ls`**:

```bash
ls
hello.txt

```

The `ls` command lists the files and folders in your current directory, so seeing `hello.txt` in the output confirms that the file was created.

**Creating multiple files at once:**

You can create several files in a single command by listing their names separated by spaces:

```bash
touch file1.txt file2.txt file3.txt

```

This creates three empty files: `file1.txt`, `file2.txt`, and `file3.txt`.

**Creating a file inside a folder:**

You can create a file directly inside another directory without navigating into it first:

```bash
touch documents/notes.txt

```

This creates `notes.txt` inside the `documents` directory. The `documents` directory must already exist; otherwise, the command will fail.

**Note:** If the file already exists, **`touch`** will not overwrite its contents. Instead, it updates the file's **last modified timestamp**, which records when the file's contents were last changed.
