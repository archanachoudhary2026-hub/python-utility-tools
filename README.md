# Assignment 5: Importing, Creating Modules & Packages

## Problem Statement
You are working as a Python Developer for a small utility tools team.  
The company wants to organize code into **modules** and **packages** to make the project reusable and scalable.  
Your task is to create simple modules, import them, and organize them into a package.

---

## 📂 Folder Structure
Assignment-5/
│
├── math_utils.py
├── string_utils.py
├── main.py (or main.ipynb)
│
└── shop_package/
├── init.py
├── discount.py
└── billing.py


---

## Task 1: `math_utils.py`
Functions:
- `add(a, b)` → returns `a + b`
- `subtract(a, b)` → returns `a - b`
- `square(n)` → returns `n²`

**Example usage in `main.py`:**
```python
import math_utils
from math_utils import square

print(math_utils.add(2, 3))        # 5
print(math_utils.subtract(300, 30)) # 270
print(square(10))                   # 100

---


## Task 2: string_utils.py

Functions:

capitalize_words(text) → returns text with each word capitalized

reverse_string(text) → returns reversed string

word_count(text) → returns number of words in the text

Example usage in main.py:

from string_utils import capitalize_words, reverse_string, word_count

print(capitalize_words("I am a dedicated learner"))
# "I Am A Dedicated Learner"

print(reverse_string("I am a happy soul"))
# "luos yppah a ma I"

print(word_count("Please ensure you are consistent with your actions"))
# 8



##  Task 3: shop_package
discount.py
apply_discount(price, percent) → applies percentage discount

flat_discount(price) → subtracts 50 from price

billing.py
calculate_total(prices) → returns sum of all prices

apply_tax(amount) → adds 5% tax

__init__.py
Can be left empty OR used to expose shortcuts.
For simplicity, leave it empty.##


Task 4: Using the Package in main.py

import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

print(disc.apply_discount(1000, 10))   # 900.0
print(disc.flat_discount(2000))        # 1950
print(calculate_total([100, 200, 300])) # 600
print(apply_tax(3000))                  # 3150.0


## Key Concepts Learned

Modules: Separate .py files containing reusable functions (math_utils.py, string_utils.py).

Packages: A folder with __init__.py that groups related modules (shop_package).

Imports:

Absolute imports (from shop_package.billing import calculate_total)

Module imports (import math_utils)

Function imports (from math_utils import square)

Testing functions: Printing outputs to verify correctness.
