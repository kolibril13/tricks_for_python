import os
from pathlib import Path
if __name__ == "__main__":
    os.system(f"mypy {Path(__file__).resolve()}")

from typing import Callable

def do_twice(func: Callable[[str], str], argument: str) -> None:
    print(func(12))
    print(func(argument))

def create_greeting(name: str) -> str:
    return f"Hello {name}"

do_twice(create_greeting, "he")