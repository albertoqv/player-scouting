from player_scouting.domain.entities import Player
from player_scouting.domain.value_objects import SimilarityScore


class Comparison:
    def __init__(
        self,
        player1: Player,
        player2: Player,
        similarity_score: SimilarityScore,
    ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.similarity_score = similarity_score

    def __eq__(self, other: Comparison) -> bool:
        same_order = self.player1 == other.player1 and self.player2 == other.player2
        reversed_order = self.player1 == other.player2 and self.player2 == other.player1
        return (
            same_order or reversed_order
        ) and self.similarity_score == other.similarity_score
