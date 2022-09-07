from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    username: str
    first_name: str
    last_name: str
    patronymic: Optional[str]
