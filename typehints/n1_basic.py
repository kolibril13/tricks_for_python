from typing import List


def g(x:List):
    print(x)


g(2)
g([1,2])


import os
from pathlib import Path
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"mypy {script_name}")