from player_scouting.domain.statistics import Statistics
from player_scouting.domain.value_objects import SimilarityScore


class SimilarityCalculator:
    def similarity_metric(self, value_a: int, value_b: int) -> float:
        if value_a == value_b:
            return 1
        else:
            result = 1 - abs(value_a - value_b) / max(value_a, value_b)
            return result

    def total_similarity(
        self, player1_stats: Statistics, player2_stats: Statistics
    ) -> SimilarityScore:
        goals_similarity = self.similarity_metric(
            player1_stats.goals, player2_stats.goals
        )
        assists_similarity = self.similarity_metric(
            player1_stats.assists, player2_stats.assists
        )
        average = (goals_similarity + assists_similarity) / 2
        percentage = round(average * 100)
        return SimilarityScore(percentage)
