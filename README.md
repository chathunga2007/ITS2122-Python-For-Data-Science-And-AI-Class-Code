# 🐍 ITS2122 - Python for Data Science & AI

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-2CA5E0?style=for-the-badge&logo=python&logoColor=white)](https://requests.readthedocs.io/)
[![IJSE](https://img.shields.io/badge/IJSE-Semester%2003-E32227?style=for-the-badge)](https://www.ijse.lk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**Comprehensive Class Projects, Lecture Notebooks, Quizzes, and Practical Exercises for ITS2122: Python for Data Science & AI.**  
*Conducted at the Institute of Software Engineering (IJSE) — Semester 03.*

[Explore Modules](#-curriculum--weekly-roadmap) • [Repository Structure](#-repository-structure) • [Getting Started](#-getting-started) • [Running Notebooks](#-running-the-code)

</div>

---

## 📌 Course Overview

This repository contains the complete practical codebase, assignments, algorithmic quizzes, and Jupyter Notebooks developed for **ITS2122: Python for Data Science & AI** under the Bachelor of Science / Graduate Diploma curriculum at **IJSE (Institute of Software Engineering)**.

The course guides students through foundational Python programming into advanced data processing, object-oriented software design, file systems, web service interaction, and industrial debugging workflows required for Data Science and Artificial Intelligence tracks.

---

## 🗺️ Curriculum & Weekly Roadmap

| Week | Focus Area | Key Concepts & Theory | Hands-on Labs / Quizzes | Tools & Libraries |
| :---: | :--- | :--- | :--- | :--- |
| **01** | **Python Foundations** | Syntax, Variables, Dynamic Typing, Type Casting, String Formatting | `Main.py`, `week_01_codes.ipynb` | Standard Library |
| **02** | **Data Structures: Lists** | Indexing, Slicing, Mutability, List Methods, Sorting, Statistics | 3 Practical Tasks, Advanced Python Challenge PDF Quiz | Built-in Collections |
| **03** | **Operators & Expressions** | Arithmetic, Comparison, Logical, Identity, Membership, Bitwise | `week_03_code.ipynb` | Python Expressions |
| **04** | **Control Flow & Logic** | Conditionals (`if-elif-else`), Match-Case (Python 3.10+), Loops, Complex Dicts | Tasks 01–05 (Geometry, Comparisons, Inventory Engine) | Pattern Matching |
| **05** | **Functions & Modularity** | Positional/Default Args, `*args`, `**kwargs`, Scope, Lambdas | Tasks 01–04 (BMI, Score Normalizer, Billing) + 3 Quizzes | Functional Python |
| **06** | **Object-Oriented Programming** | Classes, Objects, `__init__`, Encapsulation, Private Members, Inheritance | Modular Imports, Tasks 01–05 (Car, Employee, Bank Account) | Python OOP |
| **07** | **File Handling & Streams** | Context Managers (`with`), Line Reading, Text Sanitization (`rstrip`) | `hello.ipynb`, CSV & JSON sample stream manipulation | File I/O (`open`, `read`) |
| **08** | **Structured Data & Pandas** | JSON parsing (`dump`/`loads`), CSV Processing, Pandas DataFrames, Matplotlib | Practical Notebook, CSV & JSON data files | `pandas`, `json`, `csv`, `matplotlib` |
| **09** | **Web APIs, Scraping & Debugging** | REST APIs (`GET`, headers, params), BeautifulSoup HTML Parsing, `pdb` Debugger | API integration, Weather client, pdb debugging script | `requests`, `bs4`, `pdb` |

---

## 🔍 Detailed Weekly Breakdown

<details>
<summary><b>Week 01: Python Fundamentals & Environment Setup</b></summary>
<br>

- **Topics Covered:**
  - Python execution model and interpreter basics
  - Declaring variables, constant conventions (`PI_VALUE = 3.14`)
  - Basic data types: `str`, `int`, `float`, `bool`
  - Type inference and dynamic typing
  - Output formatting and standard printing
- **Key Files:**
  - [`Week 01/Main.py`](file:///Week%2001/Main.py): First Python script (`print("Hello World")`)
  - [`Week 01/week_01_codes.ipynb`](file:///Week%2001/week_01_codes.ipynb): Interactive notebook exploring variable types and behaviors
</details>

<details>
<summary><b>Week 02: Python Data Structures & List Manipulation</b></summary>
<br>

- **Topics Covered:**
  - Python list internals: 0-indexed ordering, heterogeneous types, mutability
  - Essential methods: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`
  - Mathematical and statistical operations on sequences: `sum()`, `len()`, `min()`, `max()`, computing averages
  - Element replacement, nested lists, and slicing syntax
- **Key Files & Tasks:**
  - `Task-01.py`: Sales analysis and item insertion at specified indices
  - `Task-02.py`: Student marks evaluation, aggregate total, and average scoring
  - `Task-03.py`: Temperature tracking and data sorting
  - `Quiz/quiz.py` & `Quiz/Advanced Python Challenge.pdf`: Advanced analytical problems on numerical datasets
</details>

<details>
<summary><b>Week 03: Operators & Mathematical Logic</b></summary>
<br>

- **Topics Covered:**
  - **Arithmetic Operators:** Addition, subtraction, multiplication, float division `/`, floor division `//`, modulus `%`, exponentiation `**`
  - **Assignment Operators:** In-place compound operations (`+=`, `-=`, `*=`, `/=`, etc.)
  - **Relational Operators:** Equality `==`, inequality `!=`, strict comparisons (`<`, `>`, `<=`, `>=`)
  - **Logical Operators:** Boolean algebra with `and`, `or`, `not`
  - **Identity vs Equality:** `is` and `is not` vs `==`
  - **Membership Operators:** Testing sequence inclusion with `in` and `not in`
- **Key Files:**
  - [`Week 03/week_03_code.ipynb`](file:///Week%2003/week_03_code.ipynb): Interactive evaluation of all operator classes
</details>

<details>
<summary><b>Week 04: Control Flow, Decision Making & Pattern Matching</b></summary>
<br>

- **Topics Covered:**
  - Conditional branching: `if`, `if-else`, and multi-way `if-elif-else` constructs
  - Pythonic ternary operator syntax (`<val_if_true> if <cond> else <val_if_false>`)
  - Structural Pattern Matching: Using `match-case` (Python 3.10+) for data destruction and multi-pattern evaluations
  - Iteration: `for` loops, range sequences, `while` loops, and loop control statements (`break`, `continue`)
  - Compound structures: Nested dictionaries and inventory state management
- **Key Files & Tasks:**
  - `Task 01/task01.py`: Geometric validation and area calculation for rectangles
  - `Task 02/task02.py`: Finding the largest number among three user inputs
  - `Task 03/task03.py`: Shape processing engine using modern Python `match-case`
  - `Task 04/task04.py`: Factorial computation with validation and iterative loop
  - `Task 05/task05.py`: Inventory tracking dictionary with price and stock management
</details>

<details>
<summary><b>Week 05: Modular Programming with Functions & Dynamic Arguments</b></summary>
<br>

- **Topics Covered:**
  - Function declaration (`def`), parameters, and return signatures
  - Positional arguments vs default argument positioning rules
  - Keyword arguments and keyword-only argument conventions
  - Variadic arguments:
    - Arbitrary positional arguments (`*args`)
    - Arbitrary keyword arguments (`**kwargs`)
  - Scope: Local vs global variable access
  - Pure functions and mathematical modeling
- **Key Files & Tasks:**
  - `Task 01/task_01.py`: Body Mass Index (BMI) calculator with health categorization
  - `Task 02/task_02.py`: Score normalization engine leveraging `*args` and scaling factors
  - `Task 03/task_03.py`: Flexible restaurant billing calculator using `**items` kwargs
  - `Task 04/task_04.py`: Student registration card formatter
  - `Quiz/`: Array updates, student grading logic, and strong password validator
</details>

<details>
<summary><b>Week 06: Object-Oriented Programming (OOP) & Modules</b></summary>
<br>

- **Topics Covered:**
  - Object-Oriented Programming paradigms in Python
  - Classes, instances, and the `self` reference
  - Constructor method (`__init__`) for state initialization
  - Class attributes vs Instance attributes
  - Encapsulation: Private members (e.g. `__balance`) and getter/setter access
  - Single and multi-level inheritance: Parent classes, child overrides, `super()`
  - Modular Python: Module importing (`import ... as ...`), namespace isolation, and `if __name__ == "__main__":` entry point guard
- **Key Files & Tasks:**
  - `addition.py` & `main.py`: Modular code organization and custom module consumption
  - `Task 01/task_01.py`: Random radius generator and circle geometry calculations
  - `Task 02/task_02.py`: `Car` class illustrating class-level attributes (`wheels = 4`)
  - `Task 03/task_03.py`: `Employee` class with instance attributes and greeting methods
  - `Task 04/task_04.py`: `Vehicle` parent class extended into specialized child classes
  - `Task 05/task_05.py`: `BankAccount` class implementing encapsulation with deposits, withdrawals, and balance protection
</details>

<details>
<summary><b>Week 07: File Handling & Stream I/O</b></summary>
<br>

- **Topics Covered:**
  - Standard File I/O operations and file modes (`'r'`, `'w'`, `'a'`, `'+'`)
  - Safe stream handling using Context Managers (`with open(...) as file:`)
  - Reading methods: `read()`, `readline()`, and `readlines()`
  - Line termination sanitization (`.rstrip("\n")`)
  - Working with raw `.txt`, `.csv`, and `.json` data files
- **Key Files:**
  - [`Week 07/hello.ipynb`](file:///Week%2007/hello.ipynb): Interactive lab on file stream reads and writes
  - Sample datasets: `sample_01.txt`, `employees_01.csv`, `employee_01.json`
</details>

<details>
<summary><b>Week 08: Working with Structured Data (JSON & CSV) and Intro to Pandas</b></summary>
<br>

- **Topics Covered:**
  - **JSON Processing:** `json.load()` (stream), `json.loads()` (string), `json.dump()`, `json.dumps()`
  - **CSV Handling:** Reading and writing row arrays and dictionary records
  - **Introduction to Pandas:**
    - Creating and reading tabular datasets with `pd.read_csv()`
    - Inspection methods: `.head()`, `.tail()`, `.info()`, `.describe()`, `.shape`
    - Column selection, boolean filtering, and aggregation
  - **Basic Visualization:** Line plots and bar charts with `matplotlib.pyplot`
- **Key Files:**
  - [`Week 08/week_08.ipynb`](file:///Week%2008/week_08.ipynb): Comprehensive end-to-end data processing notebook
  - Datasets: `employee.json`, `student.json`, `employees_01.csv`, `new_employees.csv`
</details>

<details>
<summary><b>Week 09: Web APIs, Web Scraping & Interactive Debugging</b></summary>
<br>

- **Topics Covered:**
  - **HTTP & REST APIs:** Interacting with web services via the Python `requests` library
    - HTTP methods (`GET`, `POST`), status codes (`200 OK`, `404 Not Found`)
    - Inspecting response headers, MIME types, and parsing JSON payloads
    - Real-world API endpoints: GitHub REST API, Weather services
  - **Web Scraping:** HTML parsing with `BeautifulSoup` (`bs4`)
  - **Error Classification in Python:**
    - Syntax Errors vs Runtime Exceptions vs Logical Bugs
    - Handling common exceptions: `IndexError`, `KeyError`, `ZeroDivisionError`, `NameError`
  - **Interactive Debugging with `pdb`:**
    - Setting breakpoints using `pdb.set_trace()`
    - Stepping through execution (`n` / next, `s` / step into, `c` / continue, `p` / print variable)
    - Inspecting call stacks and live frame states
- **Key Files:**
  - [`Week 09/week_09_code.ipynb`](file:///Week%2009/week_09_code.ipynb): REST API requests, web scraping & error exploration
  - [`Week 09/test.py`](file:///Week%2009/test.py): Standalone terminal script demonstrating `pdb` debugging
  - [`Week 09/week_9.ipynb`](file:///Week%2009/week_9.ipynb): Interactive debugger notebook
</details>

---

## 📂 Repository Structure

```plaintext
ITS2122-Python-For-Data-Science---AI-Class-Code/
│
├── .gitignore
├── README.md
│
├── Week 01/
│   ├── Main.py
│   └── week_01_codes.ipynb
│
├── Week 02/
│   ├── Quiz/
│   │   ├── Advanced Python Challenge.pdf
│   │   └── quiz.py
│   ├── Task-01.py
│   ├── Task-02.py
│   ├── Task-03.py
│   └── week_02_code.ipynb
│
├── Week 03/
│   └── week_03_code.ipynb
│
├── Week 04/
│   ├── Task 01/
│   │   └── task01.py
│   ├── Task 02/
│   │   └── task02.py
│   ├── Task 03/
│   │   └── task03.py
│   ├── Task 04/
│   │   └── task04.py
│   ├── Task 05/
│   │   └── task05.py
│   └── week_04_code.ipynb
│
├── Week 05/
│   ├── Quiz/
│   │   ├── quiz_01.py
│   │   ├── quiz_02.py
│   │   └── quiz_03.py
│   ├── Task 01/
│   │   └── task_01.py
│   ├── Task 02/
│   │   └── task_02.py
│   ├── Task 03/
│   │   └── task_03.py
│   ├── Task 04/
│   │   └── task_04.py
│   └── week_05_code.ipynb
│
├── Week 06/
│   ├── Task 01/
│   │   └── task_01.py
│   ├── Task 02/
│   │   └── task_02.py
│   ├── Task 03/
│   │   └── task_03.py
│   ├── Task 04/
│   │   └── task_04.py
│   ├── Task 05/
│   │   └── task_05.py
│   ├── addition.py
│   ├── main.py
│   └── week_06.ipynb
│
├── Week 07/
│   ├── employee_01.json
│   ├── employees_01.csv
│   ├── hello.ipynb
│   ├── new_sample.text
│   ├── new_sample.text_01
│   └── sample_01.txt
│
├── Week 08/
│   ├── employee.json
│   ├── employees_01.csv
│   ├── new_employees.csv
│   ├── student.json
│   └── week_08.ipynb
│
└── Week 09/
    ├── test.py
    ├── week_09_code.ipynb
    └── week_9.ipynb
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.10** or higher installed on your system. Verify by running:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/chathunga2007/ITS2122-Python-For-Data-Science-And-AI-Class-Code.git
cd ITS2122-Python-For-Data-Science-And-AI-Class-Code
```

### 3. Create a Virtual Environment (Recommended)
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install the required data science, HTTP, and Jupyter development packages:
```bash
pip install jupyterlab ipykernel pandas requests beautifulsoup4 matplotlib
```

---

## 💻 Running the Code

### Launching Jupyter Notebooks
To view and run the interactive weekly notebooks:
```bash
jupyter notebook
```
Navigate to any week folder (e.g. `Week 08/week_08.ipynb` or `Week 09/week_09_code.ipynb`) and execute cells using `Shift + Enter`.

### Running Standalone Python Scripts
You can execute any individual task or quiz directly with Python:
```bash
# Example: Run Week 04 Task 03 (Pattern Matching)
python "Week 04/Task 03/task03.py"

# Example: Run Week 06 Task 05 (OOP Bank Account)
python "Week 06/Task 05/task_05.py"
```

### Running the Python Debugger (`pdb`)
To test interactive debugging in `Week 09`:
```bash
python "Week 09/test.py"
```
When the `(Pdb)` prompt appears:
- Type `p x` or `p y` to inspect variable values.
- Type `n` to step to the next line.
- Type `c` to continue execution.
- Type `q` to quit the debugger.

---

## 💡 Best Practices Demonstrated

- **Safe Resource Management:** Consistent usage of `with` context managers for opening files, preventing file descriptor leaks.
- **Defensive Programming:** Input validation and structured error handling for real-world reliability.
- **Pythonic Idioms:** Leveraging list comprehensions, unpacking (`*args`, `**kwargs`), and modern `match-case` structural pattern matching.
- **Object-Oriented Design:** Encapsulation of private state, clear separation of concerns, and clean class hierarchies.
- **Modular Architecture:** Guarding execution entry points using `if __name__ == "__main__":` to ensure reusable modules.

---

## 👨‍💻 Author

- **Student:** Chathunga Bimsara
- **GitHub:** [@chathunga2007](https://github.com/chathunga2007)
- **Institution:** Institute of Software Engineering (IJSE)
- **Module:** ITS2122 - Python for Data Science & AI

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) - feel free to use this code for academic and learning purposes.
