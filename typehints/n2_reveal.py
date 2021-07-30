import os
from pathlib import Path
if __name__ == "__main__":
    os.system(f"mypy {Path(__file__).resolve()}")

from mypy import *
import math
reveal_type(math.pi)

radius = 1
circumference = 2 * math.pi * radius
reveal_locals()

