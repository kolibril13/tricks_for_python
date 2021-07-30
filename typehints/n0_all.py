name: str = "Guido"
pi: float = 3.142
centered: bool = False
names: list = ["Guido", "Jukka", "Ivan"]
version: tuple = (3, 7, 1)
options: dict = {"centered": False, "capitalize": True}

from typing import Dict, List, Tuple

names2: List[str] = ["Guido", "Jukka", "Ivan"]
version2: Tuple[int, int, int] = (3, 7, 1)
options2: Dict[str, bool] = {"centered": False, "capitalize": True}