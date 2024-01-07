# Week 1 - Day 1: Introduction to Python for Large Language Models (LLM)

## Agenda

1. **Introduction to Python:** Understanding the basics of Python programming language.
2. **Python for Large Language Models:** Exploring the application of Python in Large Language Models.
3. **Hands-on Session:** Practical exercises to apply the concepts learned.

## Learning Objectives

By the end of this session, you should be able to:

- Understand and apply the basic syntax rules of Python programming.
- Understand and utilize Python's essential data structures such as Strings, Lists, and Dictionaries.
- Understand and implement advanced Python features like List Comprehensions, Generators, and Lambda functions.
- Understand the role of Python in Large Language Models and be able to apply Python programming to solve problems in this domain.

---

## Introduction to Python

### What is Python?

- **High-Level Language:** Python is known for its readability and simplicity. Unlike lower-level languages (like C or C++), Python code often reads similar to English, making it more accessible to beginners.
- **Interpreted Language:** Python is an interpreted language, which means that Python code is executed line by line. This is different from compiled languages, where code is first converted into a machine-readable format before being run.
- **Dynamically Typed:** In Python, you don't need to declare the type of a variable (like integer, string, etc.) when you create one. The Python interpreter infers the data type automatically, which makes coding faster and easier.

### Why Python?

- **Ease of Learning and Use:** Python's simple syntax allows new programmers to focus more on problem-solving rather than complex syntax rules.
- **Versatility:** Python is used in various fields, from web development to data science, machine learning, artificial intelligence, scientific and numeric computing.
- **Rich Ecosystem:** Python has a vast ecosystem of libraries and frameworks, making it easier to perform a wide range of tasks without having to write a lot of code from scratch.
- **Community and Support:** Python has a large, active community. This means plenty of resources, guides, and help are available.
- **Platform Independent:** Python code can generally be run on any operating system with little to no modification.

---

## Python Coding Conventions

### Naming Conventions

- **Variables and Functions:** Use `snake_case` for naming variables and functions (e.g., `my_variable`, `calculate_interest`).
- **Classes:** Use `PascalCase` for class names (e.g., `BankAccount`, `DataProcessor`).
- **Constants:** Use all uppercase with underscores for constants (e.g., `MAX_SIZE`, `DEFAULT_COLOR`).
- **Readability:** Choose descriptive, clear names that reflect the purpose of the variable, function, or class.

### Python Scripts

- **What Are They:** A Python script is a file containing Python code. Typically, these files have a .py extension. You can run a Python script from the command line, an IDE, or a Python interpreter.
- **Structure:** A script can contain function definitions, classes, and executable code. Python executes scripts from top to bottom.

---

## Working with Multiple Python Scripts

### When to Create Multiple Python Scripts

- **Complexity and Length:** If your program is becoming too long or complex, splitting it into multiple scripts can make it more manageable.
- **Reusability:** If you have code that can be reused in different parts of your application or in different projects, it's good to separate it into its own script.
- **Functionality Segregation:** Separate scripts based on functionality. For instance, if you're building a web application, you might have one script for database interactions, another for handling requests, and another for utility functions.

### Managing Multiple Scripts

- **Main Script:** Usually, there's a main script that serves as the entry point of the application. This script will import and use functions or classes from other scripts.
- **Importing:** You can import code from one script into another using the import statement. Python treats each script as a module, so you can access functions, classes, and variables from one script in another.
- **Folder Structure:** Organize your scripts into a logical folder structure. For larger projects, you might have a directory for database-related scripts, another for data processing, etc.
- **Package Initialization:** In a directory with multiple scripts, you can add an `__init__.py` file to let Python treat the directory as a package. This allows for easier imports.

#### Example Structure

```css
project/
│   main.py
│   __init__.py
│
└───database/
    │   db_connect.py
    │   db_operations.py
    │   __init__.py
    │
    └───models/
        │   user.py
        │   product.py
        │   __init__.py
```

#### Example main.py

```python
from database.db_operations import add_user, delete_user

def main():
    print("Hello world")

if __name__ == "__main__":
    main()
```

- The `if __name__ == "__main__":` line checks if `main.py` is the script being run. If it is, it calls the `main()` function. This is a common Python idiom to ensure that the `main()` function runs only when the script is executed directly (not when imported as a module).
  - This statement is used to check whether the script is being run directly or being imported.
  - When you run a Python script directly (like python script_name.py), Python sets the **name** variable to "**main**" in that script.

---

## Basic Data Types

In Python, you don't need to declare the type of a variable. It's dynamically typed.

### Creating Variables

**Example:**

```python
x = 10 # An integer assignment
y = 3.14 # A floating-point number assignment
name = "John" # A string assignment
is_active = True # A boolean assignment
```

Variables in Python:

- Must start with a letter or an underscore.
  - Variables starting with an underscore are meant for internal uses.
- Can only contain letters, numbers, and underscores.
- Are case-sensitive (e.g., `myVar` and `myvar` are different variables).
- Should follow the naming conventions mentioned earlier for readability.

---

## Everything is an Object in Python

In Python, everything is an object. This includes numbers, words, functions, and even classes. This has several benefits:

- **Uniformity:** Because everything is an object, you can interact with all data in the same way. This makes Python easier to learn and use.
- **Attributes and Methods:** All objects have attributes and methods. So, even simple things like numbers and words have methods you can use. This is not the case in some other languages.
- **Dynamic Typing:** In Python, you can change the type of a variable anytime. This flexibility comes from Python's object-oriented design and makes it great for quick development.
- **Memory Management:** Python automatically manages memory for you. In some languages, you have to manage memory differently for different types of data. But in Python, everything is treated the same way, which makes things simpler.

---

## Control Structures

### If-Elif-Else Statements

Used for decision making.

**Example:**

```python
if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a warm day.")
else:
    print("It's not a hot day.")
```

### Loops

#### For Loops

Iterate over a sequence (like a list, a tuple, a dictionary, a set, or a string).

**Example:**

```python
for x in range(5):
    print(x)
```

#### While Loops

Repeat as long as a certain boolean condition is met.

**Example:**

```python
count = 5
while count > 0:
    print(count)
    count -= 1
```

---

## Functions

Functions are defined using the def keyword. They allow for code reuse and organization. Use arguments for inputs and return to provide outputs.

**Example:**

```python
def add(a, b):
    """Add two numbers and return the sum."""
    return a + b
```

---

## Data Structures

### Lists

Lists in Python are very flexible. They are ordered, which means the items have a definite order that will not change. They are mutable, which means you can change their content without changing their identity. You can also count the number of certain values in a list or even sort the values.

**Usage:** Lists are used when you have a collection of items in a specific order, and you might need to add, remove, or change items.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
```

### Tuples

Tuples are ordered and immutable (unchangeable). They are similar to lists but can't be modified after creation.

**Usage:** Useful when you want an ordered collection that shouldn't change.

**Example:**

```python
coordinates = (10.0, 20.0)
```

### Dictionaries

Dictionaries store key-value pairs. They are unordered (as of Python 3.7, they maintain insertion order, but it's best not to rely on this). They are mutable, and keys must be unique.

**Usage:** Use them when you need to associate values with keys (like a real-life dictionary) to quickly retrieve data without knowing the index.

**Example:**

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
```

### Strings

Strings are sequences of characters. They are immutable.

**Usage:** Use them to store and manipulate textual data.

**Example:**

```python
greeting = "Hello, World!"
```

---

## Resources

- Python Documentation: [Official Python Docs](https://docs.python.org/3/)
- Large Language Models: [LLMS Practical Guide](https://github.com/Mooler0410/LLMsPracticalGuide)
