# What Is The Terminal

The **terminal** is a powerful text-based interface that lets you communicate directly with your computer's operating system.

Instead of clicking buttons and icons, you type commands to navigate files, run programs, and manage your system. Learning the terminal is an essential skill for any developer.

## Your First Command

### Challenge

**Beginner**

Use the `echo` command to print `Hello World!` to the terminal.

> *Remember that the output is **case sensitive**. Make sure your text matches exactly.*

Use the `echo` command followed by your text in double quotes.

#### Hints

**Hint 1**

A command line has two parts: the program you run and the argument you pass it. Here the program is `echo` and the argument is your text.

**Hint 2**

Type `echo`, a space, then your text inside double quotes, and press Enter. The text is **case sensitive**, so it has to match the task exactly.

### Solution

    echo "Hello World!"

### Explanation

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

## **Comments**

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

## **Print Working Directory**

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

## **List Files**

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

## **Change Directory**

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

## **Absolute vs Relative Paths**

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

## **Create A File**

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

## **Read A File**

The **`cat`** command is short for **concatenate**, which means to link things together. While its original purpose was to join files, its most common use today is to **read and display the contents of a file** directly in the terminal.

Simply type **`cat`** followed by the filename:

```bash
cat readme.txt

```

The contents of the file will be printed to the terminal immediately.

**Other useful ways to read files:**

**`head`**: displays only the **first 10 lines** of a file:

```bash
head readme.txt

```

**`tail`**: displays only the **last 10 lines** of a file:

```bash
tail readme.txt

```

You can control how many lines to show with the **`-n`** option:

```bash
head -n 5 readme.txt   # show first 5 lines
tail -n 3 readme.txt   # show last 3 lines

```

**`less`**: opens the file in a **scrollable viewer**. Press **`q`** to quit:

```bash
less readme.txt

```

**Note:** **`cat`** is best for short files. For long files, **`less`** is more comfortable to read.

## **Copy A File**

The **`cp`** command stands for **copy**. It lets you create a copy of a file in a new location or with a new name.

The basic format is:

```bash
cp source destination

```

For example, to copy **`readme.txt`** and name the copy **`backup.txt`**:

```bash
cp readme.txt backup.txt

```

The original file stays in place and a new copy is created.

**Copy a file into a folder:**

You can copy a file directly into another directory:

```bash
cp readme.txt documents/readme.txt

```

Or simply pass the folder as the destination and the filename will be kept:

```bash
cp readme.txt documents/

```

**Copy a folder and all its contents:**

To copy an entire directory, use the **`-r`** flag (recursive):

```bash
cp -r documents backup_documents

```

The **`-r`** flag is only **required** for directories. It is still accepted on a single file, where it simply copies that file.

**Note:** **`cp`** will **overwrite** the destination file if it already exists.

Use the **`-i`** flag to get a confirmation prompt before overwriting:

```bash
cp -i readme.txt backup.txt
```
## **Move And Rename A File**

The **`mv`** command stands for **move**. It is used to **move a file to a different location** or to **rename a file**: both actions use the exact same command.

The basic format is:

```python
mv source destination

```

**Renaming a file:**

To rename **`readme.txt`** to **`info.txt`**:

```python
mv readme.txt info.txt

```

The file stays in the same directory but now has a new name.

**Moving a file to another directory:**

To move **`readme.txt`** into the **`documents`** folder:

```python
mv readme.txt documents/

```

The original file is removed from the current directory and placed inside **`documents`**.

**Moving and renaming at the same time:**

You can move a file to a new location and give it a new name in one command:

```python
mv readme.txt documents/info.txt

```

**Note:** Unlike **`cp`**, **`mv`** does **not** keep the original file. It is moved, not copied.

Use **`-i`** to get a prompt before overwriting an existing file:

```python
mv -i readme.txt documents/
```

## **Delete A File**

The **`rm`** command stands for **remove**. It permanently **deletes a file** from the filesystem.

Simply type **`rm`** followed by the filename:

```python
rm readme.txt

```

The file is deleted immediately. You can confirm it is gone with **`ls`**.

**Deleting multiple files at once:**

```python
rm file1.txt file2.txt file3.txt

```

**Deleting a folder and all its contents:**

To delete an entire directory including everything inside it, use the **`-r`** flag (recursive):

```python
rm -r documents

```

**Safety flags:**

**`-i`**: asks for confirmation before deleting each file:

```python
rm -i readme.txt

```

**`-f`**: force delete without any prompts (use with caution!):

```python
rm -f readme.txt

```

> ***Warning:** The terminal has **no recycle bin**. Files deleted with **`rm`** are gone permanently and cannot be recovered. Always double-check before running **`rm`**.*

## **Recap - File Operations**



### **Challenge**

Easy

Put all your file operation skills together! You must execute the following commands in order to complete the task:

1. Create a new file called **`newfile.txt`** using **`touch`**
2. Copy **`newfile.txt`** to **`backup.txt`** using **`cp`**
3. Move **`backup.txt`** into the **`documents`** folder using **`mv`**
4. Delete **`newfile.txt`** using **`rm`**
5. List the contents of the current directory using **`ls`**
6. List the contents of the **`documents`** folder using **`ls documents`**

> ***Note:** The check lists the home directory and the **`documents`** folder itself, so an extra command of your own does not break it.*

#### **Hints**

**Hint 1**



Step 1: Use **`touch newfile.txt`** to create a new file.



**Hint 2**





Step 2: Use **`cp newfile.txt backup.txt`** to copy it.



**Hint 3**



Step 3: Use **`mv backup.txt documents/backup.txt`** to move the copy into the documents folder.



**Hint 4**



Step 4: Use **`rm newfile.txt`** to delete the original file.



**Hint 5**



Step 5: Use **`ls`** and **`ls documents`** to confirm the final state.

### **Solution**

```bash
touch newfile.txt
cp newfile.txt backup.txt
mv backup.txt documents/backup.txt
rm newfile.txt
ls
ls documents
```

### **Explanation**

The commands are executed in the required order:

1. **`touch newfile.txt`** creates the new file.
2. **`cp newfile.txt backup.txt`** creates a copy named `backup.txt`.
3. **`mv backup.txt documents/backup.txt`** moves the copy into the `documents` folder.
4. **`rm newfile.txt`** deletes the original file.
5. **`ls`** displays the contents of the current directory.
6. **`ls documents`** displays the contents of the `documents` folder and confirms that `backup.txt` is there.

At the end, **`newfile.txt`** is deleted, while **`backup.txt`** exists inside the **`documents`** folder.

## **Create A Directory**

The **`mkdir`** command stands for **make directory**. It creates a new folder in your current location.

Simply type **`mkdir`** followed by the name of the folder you want to create:
```python
mkdir projects

```

You can confirm it was created by running **`ls`**:
```python
ls
documents
projects
readme.txt

```

**Creating multiple directories at once:**

You can create several folders in a single command by listing them separated by spaces:
```python
mkdir projects documents backups

```

**Creating nested directories:**

Use the **`-p`** flag to create a directory and all its parent directories at once:
```python
mkdir -p projects/app/src

```

Without **`-p`**, this would fail if **`projects`** or **`app`** don't already exist. With **`-p`**, all three folders are created automatically.

**Note:** Directory names follow the same rules as file names: avoid spaces and special characters. Use hyphens or underscores instead:
```python
mkdir my-project    # ✅ good
mkdir my_project    # ✅ good
mkdir my project    # ❌ creates two folders: my and project
```

## **Copy A Directory**

Just like copying a file with **`cp`**, you can also copy an entire directory. However, to copy a directory and **all of its contents**, you must use the **`-r`** flag, which stands for **recursive**.

The basic format is:
```python
cp -r source destination

```

For example, to copy the **`documents`** folder and name the copy **`documents_backup`**:
```python
cp -r documents documents_backup

```

Both the original folder and the copy will now exist. You can verify with **`ls`**:
```python
ls
documents
documents_backup
readme.txt

```

**Copying a directory into another directory:**

If the destination already exists as a directory, the source folder will be placed **inside** it:
```python
cp -r documents projects/

```

This creates **`projects/documents`** with all the original contents.

**Note:** Without the **`-r`** flag, **`cp`** will refuse to copy a directory and show an error. Always use **`-r`** when copying folders.

## **Move And Rename A Directory**

Just like with files, the **`mv`** command is used to **move or rename a directory**. The great thing about **`mv`** is that it works the same way for both files and folders: no extra flags needed.

The basic format is:
```python
mv source destination

```

**Renaming a directory:**

To rename the **`documents`** folder to **`files`**:
```python
mv documents files

```

The folder stays in the same location but now has a new name.

**Moving a directory into another directory:**

To move the **`documents`** folder into a folder called **`projects`**:
```python
mv documents projects/

```

The **`documents`** folder is now located at **`projects/documents`**.

**Moving and renaming at the same time:**

You can move a directory to a new location and give it a new name in one command:
```python
mv documents projects/files

```

**Note:** Unlike **`cp -r`**, **`mv`** does **not** keep the original directory. It is moved entirely. Always double-check your source and destination before running **`mv`**.

## **Delete A Directory**

To delete a directory in the terminal, you have two options depending on whether the directory is empty or not.

**Deleting an empty directory:**

The **`rmdir`** command stands for **remove directory**. It can only delete a directory that is **completely empty**:
```python
rmdir empty_folder

```

If the folder contains any files or subdirectories, **`rmdir`** will fail with an error.

**Deleting a directory and all its contents:**

To delete a directory along with everything inside it, use **`rm`** with the **`-r`** flag (recursive):
```python
rm -r documents

```

This removes the **`documents`** folder and every file and subfolder inside it.

You can also combine it with **`-f`** to force delete without any confirmation prompts:
```python
rm -rf documents

```

> ***Warning:** **`rm -rf`** is one of the most powerful and dangerous commands in the terminal. It permanently deletes everything without asking. Always double-check your path before running it. There is no undo.*
# **Wildcards and Patterns**
## **The Star Wildcard**

A **wildcard** is a special character that acts as a placeholder to match one or more characters in filenames. Wildcards let you work with multiple files at once without typing every name.

The **star wildcard** **`*`** matches **any number of characters** (including zero). It is the most powerful and commonly used wildcard.

For example, to list all files ending in **`.txt`**:
```bash
ls *.txt

```

This matches any filename that ends with **`.txt`**, no matter how long the name is.

**More examples:**

Match all files starting with **`photo`**:
```bash
ls photo*

```

Match all files containing **`report`** anywhere in the name:
```bash
ls *report*

```

Match all files of any name or extension:
```bash
ls *

```

You can use **`*`** with any command, not just **`ls`**. For example, copy all **`.jpg`** files into a folder:
```bash
cp *.jpg photos/

```

Or delete all **`.log`** files at once:
```bash
rm *.log

```

> ***Tip:** Always run **`ls`** with your wildcard pattern first before using it with **`rm`** or **`mv`**. This way you can see exactly which files will be affected before making any changes.*

## **The Question Mark Wildcard**

The **question mark wildcard** **`?`** matches **exactly one character**. Unlike **`*`**, which matches any number of characters, **`?`** is more precise: each **`?`** represents a single character position.

For example, if you have these files:
```bash
file1.txt
file2.txt
file3.txt
file10.txt
notes.txt

```

Using **`?`** to match files with exactly one character after **`file`**:
```bash
ls file?.txt

```

Output:
```bash
file1.txt
file2.txt
file3.txt

```

Notice that **`file10.txt`** is **not** matched because **`10`** is two characters, not one.

**Using multiple question marks:**

Each **`?`** matches exactly one character, so you can chain them:
```bash
ls file??.txt  # matches file10.txt, file23.txt, etc.

```

**Mixing with other characters:**
```bash
ls ???.txt     # matches any .txt file with exactly a 3-character name
ls img_?.jpg   # matches img_1.jpg, img_2.jpg but NOT img_10.jpg

```

**When to use `?` vs `*`:**

- Use **`?`** when you know exactly how many characters vary.
- Use **`*`** when the number of varying characters is unknown.

## Bracket Wildcards

The bracket wildcard `[]` matches exactly one character from a specific set or range of characters that you define inside the brackets.

For example, if you have these files:

```text
file1.txt
file2.txt
file3.txt
file4.txt
file5.txt
```

### Matching specific characters

Match only files with `1`, `2`, or `3`:

```bash
ls file[123].txt
```

**Output:**

```text
file1.txt
file2.txt
file3.txt
```

- `[]`: Matches exactly one character from the set of characters inside the brackets.
- `[123]`: Matches one character that is either `1`, `2`, or `3`.
- `ls`: A command that lists files and directories.

### Using ranges inside brackets

Instead of listing every character, you can use a range with a hyphen `-`:

```bash
ls file[1-3].txt    # same as [123]
ls file[a-z].txt    # matches any lowercase letter
ls file[A-Z].txt    # matches any uppercase letter
ls file[0-9].txt    # matches any single digit
```

- `-`: Defines a range between two characters.
- `[1-3]`: Matches one digit from `1` to `3`.
- `[a-z]`: Matches one lowercase letter from `a` to `z`.
- `[A-Z]`: Matches one uppercase letter from `A` to `Z`.
- `[0-9]`: Matches one digit from `0` to `9`.
- **Lowercase:** Letters from `a` to `z`.
- **Uppercase:** Letters from `A` to `Z`.
- **Digit:** A numeric character from `0` to `9`.

### Negating a bracket pattern

Use `!` or `^` at the start of the bracket expression to match any character **not** in the specified set:

```bash
ls file[!45].txt    # matches file1, file2, file3 but NOT file4 or file5
ls file[^45].txt    # same result
```

- `!`: When placed immediately after `[`, it excludes the listed characters in Bash and many other shells.
- `^`: Also indicates negation in many shells, including Bash, when placed immediately after `[`.
- **Negating:** Excluding specified characters from a match.
- `[!45]` or `[^45]`: Matches one character other than `4` or `5`.

**Note:** These patterns match filenames only if the corresponding files exist. For example, `file[!45].txt` can match `file1.txt`, `file2.txt`, or `file3.txt` among the example files, but it can also match other single-character filenames such as `filea.txt` if they exist.

### Combining character sets

You can combine individual characters and ranges in the same bracket expression:

```bash
ls file[1-3a-c].txt
```

This matches:

- `file1.txt`
- `file2.txt`
- `file3.txt`
- `filea.txt`
- `fileb.txt`
- `filec.txt`

- `[1-3a-c]`: Matches exactly one character that is either a digit from `1` to `3` or a lowercase letter from `a` to `c`.
- **Character set:** A collection of characters that a pattern is allowed to match.
- **Wildcard pattern:** A pattern used by the shell to find filenames that match specified rules.

**Key takeaway:** Bracket wildcards match **exactly one character** from a set or range. They are useful when you want to match specific characters, character ranges, or everything except certain characters.

## Combining Wildcards

The real power of wildcards comes when you **combine them together**. You can mix `*`, `?`, and `[]` in a single pattern to create very precise file matching.

Given this filesystem:

```text
photo_1.jpg
photo_2.jpg
photo_10.jpg
photo_1.png
photo_2.png
report_1.txt
report_2.txt
notes.txt
```

### Combining `*` and `[]`

List image files with the extensions `.jpg` and `.png`:

```bash
ls *.[jp]*
```

This matches filenames containing a dot followed by `j` or `p`, then any number of additional characters. For the example files, it matches `.jpg` and `.png` files.

You can also use **brace expansion** to list files with specific extensions:

```bash
ls *.{jpg,png}
```

- `*`: Matches zero or more characters.
- `[jp]`: Matches exactly one character, either `j` or `p`.
- `.{jpg,png}`: Brace expansion generates separate patterns, `*.jpg` and `*.png`, before the shell runs `ls`.
- **Brace expansion:** A shell feature that generates multiple strings from a pattern containing braces and comma-separated alternatives.

**Note:** `*.[jp]*` can also match other extensions beginning with `j` or `p`, such as `.jpeg`. It is broader than matching only `.jpg` and `.png`.

### Combining `?` and `[]`

List only single-digit photo files ending in `.jpg`:

```bash
ls photo_[0-9].jpg
```

This matches:

```text
photo_1.jpg
photo_2.jpg
```

It does not match `photo_10.jpg` because `[0-9]` matches exactly one digit.

- `?`: Matches exactly one character of any kind.
- `[0-9]`: Matches exactly one digit from `0` to `9`.
- **Single-digit:** A number represented by one digit, such as `1` or `7`.

### Combining all three wildcards

Match report files with a single digit before `.txt`:

```bash
ls *_[0-9].txt
```

This matches:

```text
report_1.txt
report_2.txt
```

Explanation:

- `*`: Matches zero or more characters before the underscore.
- `_`: Matches a literal underscore.
- `[0-9]`: Matches exactly one digit.
- `.txt`: Matches the literal `.txt` extension.

Now match files that start with `p` or `r`, followed by any characters, an underscore, exactly one character, and `.txt`:

```bash
ls [pr]*_?.txt
```

This matches:

```text
report_1.txt
report_2.txt
```

Explanation:

- `[pr]`: Matches exactly one character, either `p` or `r`.
- `*`: Matches zero or more characters after the first character.
- `_`: Matches a literal underscore.
- `?`: Matches exactly one character after the underscore.
- `.txt`: Matches the literal `.txt` extension.

**Important:** In the example filesystem, `notes.txt` does not match because its name does not contain the required underscore and extra character before `.txt`.

### Using wildcards with other commands

Wildcards work with many shell commands, not just `ls`.

#### Move single-digit JPG photos into a folder

```bash
mv photo_[0-9].jpg archive/
```

This moves files such as `photo_1.jpg` and `photo_2.jpg` into the `archive/` directory.

- `mv`: Moves files or directories, and can also rename them.
- `archive/`: The destination directory. It must already exist for this command to work as intended.

#### Delete `.log` files from immediate subfolders

```bash
rm */*.log
```

This removes `.log` files located one directory level below the current directory.

- `rm`: Removes files.
- `*/*.log`: Matches files whose parent directory is one level below the current directory and whose names end in `.log`.
- **Subfolder:** A directory inside another directory.
- **Immediate subfolder:** A directory directly inside the current directory, rather than a deeper nested directory.

**Warning:** `rm` deletes files without moving them to a recycle bin in typical command-line environments. Check what a wildcard matches before running a deletion command. You can preview matching paths with:

```bash
ls */*.log
```

### Key takeaway

- `*` matches zero or more characters.
- `?` matches exactly one character.
- `[]` matches exactly one character from a specified set or range.
- `{a,b}` uses brace expansion to generate alternatives; it is not a wildcard itself.

Combining these patterns lets you select files precisely for listing, moving, copying, or deleting.

## Head And Tail

When working with large files, you often don't need to read the entire file. You just need to see the beginning or the end. The **`head`** and **`tail`** commands let you do exactly that.

### The `head` command

The **`head`** command shows the **first lines** of a file. By default, it shows the first 10 lines:

```bash
head log.txt
```

To specify how many lines to show, use the **`-n`** flag:

```bash
head -n 3 log.txt   # show first 3 lines
head -n 1 log.txt   # show only the first line
```

- **`head`**: Displays the beginning of a file.
- **`-n`**: Specifies the number of lines to display.
- **`log.txt`**: The name of the file being read.
- **Flag (option):** An argument that changes how a command behaves.

### The `tail` command

The **`tail`** command shows the **last lines** of a file. By default, it shows the last 10 lines:

```bash
tail log.txt
```

To specify how many lines to show:

```bash
tail -n 3 log.txt   # show last 3 lines
tail -n 1 log.txt   # show only the last line
```

- **`tail`**: Displays the end of a file.
- **`-n`**: Specifies the number of lines to display.
- **Log file:** A file that records events, activities, or messages produced by a program or system.

### When to use each

- Use **`head`** to preview the structure or header of a file.
- Use **`tail`** to check the most recent entries in a log file.

### A useful trick: combining both

You can use both commands together to see the start and end of a file at the same time:

```bash
head -n 2 log.txt
tail -n 2 log.txt
```

- `head -n 2 log.txt` displays the first two lines.
- `tail -n 2 log.txt` displays the last two lines.

**Note:** These are two separate commands, so they display their results one after the other.

**Key takeaway:** Use `head` to inspect the beginning of a file and `tail` to inspect its end without displaying the entire contents.
