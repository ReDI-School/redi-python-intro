class: title-slide

# Introduction to programming with Python

## ReDI School of Digital Integration

.left-column[
.center[
![redi-logo](img/redi-logo.png)
]]

.right-column[
.left[
![python-logo](img/python-logo.png)
]]

---

class: title-slide

# Who are we?

---

class: title-slide

# Who are you?

## (Time to introduce yourself)

---

# What is this course about?

## What will you learn?
* Basic programming concepts
  * Same for many modern programming languages (Python, Java, C++, PHP, Javascript etc.)
  * Words like: loop, variable, function, parameter, library etc.

--
* Programming skills
  * Problem analysis
  * Problem decomposition
  * Design and implementation
  * Testing and debugging

--

* Python syntax
  * Essential subset of Python3 features

---

# What is this course about?

.right-column[
![studying-girl](img/studying-girl.jpg)
]

* Don’t worry, it’s not a theoretical computers science course

--

* Learning skills requires practicing

--

* We will have to code
![coding-fire](img/coding-fire-big.gif)



---

# What is this course about?

## What will you be capable of at the end of the course?

* Continue learning programming by yourself

--

* Convert an idea into a working program

--

* Examples of projects
  * Chat bot
  * Dictionary
  * Simple console game
  * Data analysis/plot

.bottom-right-fixed[
![projects-examples](img/projects-examples.png)
]

---

# How will we learn?

* Class work: Theory + Programming tasks
  * **Please ask questions**
  * Slides and code samples are published

--

* Homework
  * Based on the previous class
  * Published after the lesson
  * Not mandatory but we highly recommend you to do it - programming is a skill and requires practice

--

* Feedback
  * **Please complain**
  * [Link to the feedback form](https://goo.gl/forms/0vzhNp7qLigY84Wq2)

--

* Attendance tracking
  * You have to attend at least 80% of lessons to get the confirmation letter from ReDI

---

# What is a program?

* “Lives” inside a “computer”
* Performs some task

--

![program](img/program.png)

---

# Algorithm

You have distance (S) and time (t), how to calculate the average speed?

.bottom-right[
![bicycle](img/bicycle.png)
]

--

* 1st attempt: “Divide S by t”
  * Computer doesn’t know, what S and t is

--

* 2nd attempt:
  * Request and remember a number for S
  * Request and remember a number for t
  * Divide S by t and remember the result
  * Print the result

--

* 3rd attempt: ...

---

# How to explain an algorithm to a computer?

.center[
![curious](img/curious.png)
]

--

* Physical hardware (CPU) has a set of commands (100-500 commands) - instruction set

--

  * Those commands are not really readable for a human: “move 16 bytes from address xxx to address yyy”

--

* Natural human language is not formal enough - hard for computer to understand (yet)

---

# How to explain an algorithm to a computer?

* High-level programming languages (Python, C++, Java, Javascript etc)
  * Formal
  * Can be read and written by humans
  * Can be compiled as or interpreted to instruction set

--

.center[
![interpreter](img/interpreter.png)
]

---

# Why Python?

* 1994: Version 1
  * Not young (But is actively developed)
  * Mature

--

* Goals (some of them)
  * Easy and intuitive but as powerful as those of the major competitors
  * Suitable for everyday tasks allowing for short development times
  * Open-source (free)

--

* Many areas of application
  * Web-development (backend)
  * Automation (e.g. automated testing)
  * Robotics (prototyping)
  * Artificial Intelligence
  * Data Science

---

# Why Python?

.right[
![python-success](img/python-success.png)
]

* Python in Web:
  * Youtube
  * Dropbox
  * Google
  * Quora
  * Instagram
  * BitTorrent (Earlier Version)
  * Spotify
  * Reddit
  * Pinterest
  * BitBucket
  * EVE Online MMOPG
  * Mercurial Source Control
* Other areas: [Python success story](https://www.python.org/about/success/)

---

# Setting up Python3

**Linux**: Should be installed: open Terminal (Ctrl+Alt+T on Ubuntu) and type **python3**:
```bash
$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**Windows & MacOSx**: If not installed (nothing with the word "Python" in start menu), go to https://www.python.org/downloads/ , download and install latest 3.x version
.center[
![download-python](img/download-python.png)
]

---

# You’re almost good to go

* You have have the interpreter installed (Python3)

--

* You can use any text editor to create a python source file and “feed it to the interpreter”

--

 ## But…

--

* We’ll be using IDE (Integrated development environment) in this course
  * Very convenient code editor
  * Has button “Run”
  * ...

---

# Installing PyCharm

## Ubuntu

In Terminal type:
```bash
sudo snap install pycharm-community --classic
```

---

# Installing PyCharm

## Not Ubuntu:
* Go to: https://www.jetbrains.com/pycharm/download/
* Choose Community Edition
* Windows:
  * Install the downloaded file
* Other Linux:
  * Uncompress the downloaded file
  * In Terminal type:
  ```bash
  cd <path of bin folder inside the extracted folder>
  sh pycharmXXX.sh
  ```

---

# Running your first program

* Open PyCharm
* Click "Create new project"
.center[
![pycharm](img/pycharm-welcome.png)
]

---

# Running your first program

* Set the location and the name of the project (this is the location where your programs will be stored)
* Click "Create"
.center[
![pycharm](img/pycharm-create-project.png)
]

---

# Running your first program

* Right-click on the project-name
* Select "New" -> "Python File"
.center[
![pycharm](img/pycharm-create-file.png)
]


---

# Running your first program

* Give your file a name
* Click "OK"
.center[
![pycharm](img/pycharm-file-name.png)
]

---

# Running your first program

* Type the following code in your file

```python
# This is my first program in Python
# It prints the line 'Hello world' to
# the console output

print('Hello world!')
```

* Save and click Run -> Run... and select your project
.center[
![pycharm](img/pycharm-select-project.png)
]

---

# Running your first program

Check the result at the bottom of the window

```bash
/home/grafov/venv/tmp/bin/python /tmp/tmp/hello.py
Hello world

Process finished with exit code 0
```

---

# Understanding your first program

* Built-in functions:
```python
print(...)
```
  * Part of the language
  * Sub-program
  * Has unique name, effect or result, list of arguments (parameters)
  * Available functions: https://docs.python.org/3/library/functions.html

--

* Literals:
```python
'Hello world!'
```
  * Represent  fixed values in code
  * Different types: numbers (also floating-point),  boolean, string and some others

---

# Understanding your first program

One more very important thing for your first program

```python
# This is my first program in Python
# It prints the line 'Hello world' to
# the console output

print('Hello world!')
```
--

* Comments:
  * Ignored by interpreter
  * Write it for yourself or for somebody else who is supposed to read your code in future
  * You can use it to disable lines of code in your program without deleting them

---

#Breaking your first program

```python
# This is my first program in Python
# It prints the line 'Hello world' to
# the console output

Print('Hello world!')
```

--

```bash
/home/grafov/venv/tmp/bin/python /tmp/tmp/hello.py
Traceback (most recent call last):
  File "/tmp/tmp/hello.py", line 1, in <module>
    Print('Hello world')
NameError: name 'Print' is not defined

Process finished with exit code 1
```
If you can’t understand it right away, usually it’s enough to search for the text of an error:
[GO!](https://duckduckgo.com/?q=python3+NameError%3A+name+%27Print%27+is+not+defined&t=canonical&ia=web)

---

# Multi-instruction program

```python
# This is my first multi-instruction
#  program in Python: It prints two
# lines to the console output

print('Hello world!')
print("My name is Denis")

```
--

* Only one instruction per line
* Empty lines are allowed
* Instructions are executed one after another
* Look at the quotes (both ways work with string literals)

---

# Additional materials and where to find help

* https://automatetheboringstuff.com/ - Online book, covers all the basics of Python and how to use it

--

* https://docs.python.org/3/index.html - Python3 documentation (including Tutorial)

--

* Internet search - community is big, many questions were already posted somewhere
  * Pay special attention to the information at stackoverflow.com



