from dataclasses import dataclass


@dataclass
class UserRoom:
    user_id: str
    room_id: str