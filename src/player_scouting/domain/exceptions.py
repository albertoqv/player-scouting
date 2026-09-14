class DomainError(ValueError):
    pass


class InvalidSimilarityScoreError(DomainError):
    pass


class InvalidStatisticsError(DomainError):
    pass


class InvalidPlayerError(DomainError):
    pass
