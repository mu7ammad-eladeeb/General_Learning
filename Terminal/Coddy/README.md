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
