import os
from pathlib import Path
if __name__ == "__main__":
    os.system(f"mypy {Path(__file__).resolve()}")

if __name__ != "__main__":

    import random
    from typing import Sequence, TypeVar

    Choosable = TypeVar("Choosable")

    def choose(items: Sequence[Choosable]) -> Choosable:
        return random.choice(items)

    reveal_type(choose(["Guido", "Jukka", "Ivan"]))
    reveal_type(choose([1, 2, 3]))
    reveal_type(choose([True, 42, 3.14]))
    reveal_type(choose(["Python", 3, 7]))