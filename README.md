# Tablicate
Tablicate - Python library for easy table creation and output to terminal

## Features
- Column-wise justification alignment (left, right, center)

## Installation
**Tablicate** is implemented in pure Python code so installation is super easy. There is no additional library required.

Simply clone using the step below to get `tablicate.py`. 

```bash
$> git clone https://github.com/dhanoosu/Tablicate.git
```

## Usage

To use it, import `Table` from the `tablicate` module.

```python
from tablicate import Table

# Initialise the Table instance
table = Table()

# Adding column headings
table.add_column("Heading 1")
table.add_column("Heading 2")

# Adding row content
table.add_row(["Content1", "Content2"])

# Print table
table.print_table()

```
Output:

```
+-------------+-------------+
|  Heading 1  |  Heading 2  |
+-------------+-------------+
|  Content1   |  Content2   |
+-------------+-------------+
```

You can also print table directly with

```python
table = Table()
table.print_table(
    [
        ["Name", "Age", "Occupation"],
        ["John", 40, "Doctor"],
        ["Alice", 27, "Nurse"]
    ]
)
```

Output:
```
+---------+-------+--------------+
|  Name   |  Age  |  Occupation  |
+---------+-------+--------------+
|  John   |  40   |  Doctor      |
|  Alice  |  27   |  Nurse       |
+---------+-------+--------------+
```

## Justification alignment

The `.add_column()` method can be fed with an additional `justify` option to align all cells in the column independently.

Format: `table.add_column(text, justify="")`

| Justify  | Description |
|----------|-------------|
| *"left"*   | Left justify (Default) |
| *"right"*  | Right justify |
| *"center"* | Center justify |
