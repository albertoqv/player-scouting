from __future__ import annotations

from dataclasses import dataclass

from player_scouting.domain.entities import Player
from player_scouting.domain.value_objects import SimilarityScore


@dataclass(frozen=True, eq=False)
class Comparison:
    player1: Player
    player2: Player
    similarity_score: SimilarityScore

    def __eq__(self, other: Comparison) -> bool:
        same_order = self.player1 == other.player1 and self.player2 == other.player2
        reversed_order = self.player1 == other.player2 and self.player2 == other.player1
        return (
            same_order or reversed_order
        ) and self.similarity_score == other.similarity_score

    def __hash__(self) -> int:
        players = frozenset({self.player1.player_id, self.player2.player_id})
        return hash((players, self.similarity_score))
