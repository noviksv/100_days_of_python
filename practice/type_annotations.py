age: int

age = "qwertyt"

# Type annotations are used to inform developers and tools about the expected types of data, making code easier to understand and statically check for type-related errors using tools like Mypy, Pyright, or Pyre.

# Here's a brief overview of how type annotations can be used:

# Variable Annotations:
age: int = 30
name: str = "Alice"
# 1. Function Argument and Return Type Annotations:
def greet(name: str) -> str:
    return f"Hello, {name}"

greet(name=123)

# 2. For Lists, Dictionaries, and Other Collections (using the typing module for Python versions < 3.9):
from typing import List, Dict

names: List[str] = ["Alice", "Bob"]
age_map: Dict[str, int] = {"Alice": 30, "Bob": 25}
# 3. In Python 3.9 and later, you can use built-in collection types directly:
names: list[str] = ["Alice", "Bob"]
age_map: dict[str, int] = {"Alice": 30, "Bob": 25}

#Type annotations are optional and do not affect the runtime behavior of the code. 
# They are primarily used as hints for type checkers, IDEs, and other tools to provide better support for developers.