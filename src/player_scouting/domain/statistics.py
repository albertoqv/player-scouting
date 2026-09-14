class Statistics:
    def __init__(self, goals: int, assists: int) -> None:
        if not isinstance(goals, int) or isinstance(goals, bool):
            raise ValueError("Goals must be an integer")
        if not isinstance(assists, int) or isinstance(assists, bool):
            raise ValueError("Assists must be an integer")
        if goals < 0:
            raise ValueError("Goals must be equal to or greater than 0")
        if assists < 0:
            raise ValueError("Assists must be equal to or greater than 0")
        self.goals = goals
        self.assists = assists
