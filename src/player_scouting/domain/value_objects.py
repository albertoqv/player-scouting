from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SimilarityScore:
    percentage: int

    def __post_init__(self) -> None:
        if not isinstance(self.percentage, int) or isinstance(self.percentage, bool):
            raise ValueError("The percentage must be an integer")
        if self.percentage < 0 or self.percentage > 100:
            raise ValueError("The percentage must be a value between 0 and 100")
