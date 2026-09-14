from __future__ import annotations

from dataclasses import dataclass

from player_scouting.domain.exceptions import InvalidStatisticsError


@dataclass(frozen=True)
class Statistics:
    goals: int
    assists: int

    def __post_init__(self) -> None:
        if not isinstance(self.goals, int) or isinstance(self.goals, bool):
            raise InvalidStatisticsError("Goals must be an integer")
        if not isinstance(self.assists, int) or isinstance(self.assists, bool):
            raise InvalidStatisticsError("Assists must be an integer")
        if self.goals < 0:
            raise InvalidStatisticsError("Goals must be equal to or greater than 0")
        if self.assists < 0:
            raise InvalidStatisticsError("Assists must be equal to or greater than 0")
