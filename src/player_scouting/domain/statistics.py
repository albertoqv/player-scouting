from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Statistics:
    goals: int
    assists: int

    def __post_init__(self) -> None:
        if not isinstance(self.goals, int) or isinstance(self.goals, bool):
            raise ValueError("Goals must be an integer")
        if not isinstance(self.assists, int) or isinstance(self.assists, bool):
            raise ValueError("Assists must be an integer")
        if self.goals < 0:
            raise ValueError("Goals must be equal to or greater than 0")
        if self.assists < 0:
            raise ValueError("Assists must be equal to or greater than 0")
