# Python Learning

A personal repository for learning Python fundamentals, covering core data types, control flow, and built-in operations.

## 📁 Files Overview

| File | Topic |
|------|-------|
| `data_types.py` | Core Python data types |
| `number_data_type.py` | Numbers, math & the `random` module |
| `strint_data_type.py` | String methods & formatting |
| `list_data_type.py` | List methods & operations |
| `dictionary_data_type.py` | Dictionary methods & iteration |
| `tuple_data_type.py` | Tuple creation, indexing & slicing |
| `function_data_type.py` | Defining & calling functions |
| `conditional_statements.py` | `if`, `elif`, `else` & boolean logic |

---

## Topics

### 1. Data Types (`data_types.py`)

Covers Python's built-in data types with examples:

| Type    | Example                           |
|---------|-----------------------------------|
| `int`   | Whole numbers (e.g. `age = 20`)   |
| `float` | Decimal numbers (e.g. `miles`)    |
| `str`   | Text strings (e.g. `name`)        |
| `dict`  | Key-value pairs (e.g. `studName`) |
| `list`  | Ordered, mutable sequences        |
| `set`   | Unordered, unique elements        |
| `tuple` | Ordered, immutable sequences      |

```bash
python data_types.py
```

---

### 2. Conditional Statements (`conditional_statements.py`)

Covers decision-making in Python with `if`, `elif`, and `else`:

| Concept       | Example                                        |
|---------------|------------------------------------------------|
| `if` / `else` | Compare a value and run different code paths   |
| `elif`        | Chain multiple conditions (e.g. grade bands)   |
| `or`          | True if at least one condition is met          |
| `not`         | Reverse a boolean condition                    |
| Truthiness    | Empty strings are treated as `False`           |

```bash
python conditional_statements.py
```

---

### 3. Numbers & Random (`number_data_type.py`)

Covers numeric operations, type conversion, and the `random` module:

| Concept             | Example                            |
|---------------------|------------------------------------|
| `int()` / `float()` | Convert between number types       |
| `type()`            | Check a variable's data type       |
| `**`                | Exponentiation (e.g. `2 ** 1000`)  |
| `random.randint()`  | Random integer in a range          |
| `random.choice()`   | Pick a random item from a list     |
| `random.shuffle()`  | Shuffle a list in place            |
| Set operations      | `union`, `intersection`, `&`, `\|` |

```bash
python number_data_type.py
```

---

### 4. String Methods (`strint_data_type.py`)

Covers common string operations and formatting:

| Method / Concept                  | Example                               |
|-----------------------------------|---------------------------------------|
| `upper()` / `lower()` / `title()` | Change letter casing                  |
| `count()` / `find()`              | Search within a string                |
| `replace()`                       | Swap one substring for another        |
| `split()`                         | Break a string into a list            |
| `startswith()` / `endswith()`     | Check how a string begins or ends     |
| `format()`                        | Insert values into a template string  |

```bash
python strint_data_type.py
```

---

### 5. List Methods (`list_data_type.py`)

Covers list manipulation methods:

| Method     | Description                                   |
|------------|-----------------------------------------------|
| `insert()` | Insert an element at a specific index         |
| `copy()`   | Create a shallow copy of a list               |
| `remove()` | Remove the first occurrence of a value        |
| `pop()`    | Remove and return the last element            |
| `clear()`  | Remove all elements from the list             |

```bash
python list_data_type.py
```

---

### 6. Dictionary Methods (`dictionary_data_type.py`)

Covers dictionary creation, iteration, and key-based lookups:

| Concept / Method | Description                                          |
|------------------|------------------------------------------------------|
| `dict` literal   | Create a dictionary with key-value pairs             |
| `.items()`       | Iterate over all key-value pairs with a `for` loop   |
| `.get()`         | Safely retrieve a value by key (returns `None` if missing) |
| `in` / `or`      | Check membership or combine conditions               |

```bash
python dictionary_data_type.py
```

---

### 7. Tuples (`tuple_data_type.py`)

Covers tuple creation with mixed types, indexing, and slicing:

| Concept        | Description                                              |
|----------------|----------------------------------------------------------|
| Tuple literal  | Ordered, immutable sequence using `()` with mixed types  |
| Negative index | `mixed_items[-1]` accesses the last element              |
| Slicing        | `mixed_items[2:5]` extracts a sub-sequence               |
| `len()`        | Returns the number of elements in the tuple              |
| Immutability   | Tuple elements cannot be changed after creation          |

```bash
python tuple_data_type.py
```

---

### 8. Functions (`function_data_type.py`)

Covers defining and calling reusable functions with parameters and return values:

| Concept       | Description                                              |
|---------------|----------------------------------------------------------|
| `def`         | Define a named, reusable block of code                   |
| Parameters    | Accept inputs (e.g. `name`, `age`, `address`)            |
| `return`      | Send a value back to the caller                          |
| f-strings     | Embed variables directly into strings with `f"{var}"`    |
| Logic in functions | Use `if`/`else` inside a function (e.g. even/odd)  |

```bash
python function_data_type.py
```

---

## Getting Started

Make sure you have Python installed, then run any file directly:

```bash
python <filename>.py
```

> Requires **Python 3.x**
