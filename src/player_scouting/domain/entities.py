from datetime import date


class Player:
    def __init__(
        self, player_id: int, name: str, position: str, date_of_birth: date
    ) -> None:
        if not isinstance(player_id, int) or isinstance(player_id, bool):
            raise ValueError("The player_id must be an integer")
        if player_id <= 0:
            raise ValueError("The player_id must be a value greater than 0")
        if date_of_birth > date.today():
            raise ValueError("The date cannot be in the future")
        self.player_id = player_id
        self.name = name
        self.position = position
        self.date_of_birth = date_of_birth

    def __eq__(self, other: Player) -> bool:
        return self.player_id == other.player_id
