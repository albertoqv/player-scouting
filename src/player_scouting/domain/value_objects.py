class SimilarityScore:
    def __init__(self, percentage: int) -> None:
        if not isinstance(percentage, int) or isinstance(percentage, bool):
            raise ValueError("The percentage must be an integer")
        if percentage < 0 or percentage > 100:
            raise ValueError("The percentage must be a value between 0 and 100")

        self.percentage = percentage

    def __eq__(self, other: SimilarityScore) -> bool:
        return self.percentage == other.percentage
