# color-print

Tiny Python package to format and print colored text using ANSI escape sequences.

Usage

```python
from color_print import color_print, format_text

color_print("Hello", "green")
# or
s = format_text("Hello", "red")
print(s)
```

Install

```bash
pip install .
```

Run tests

```bash
pip install -e .[test]
pytest
```
