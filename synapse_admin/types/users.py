from dataclasses import dataclass


@dataclass
class User:
    id: str = None
    displayname: str = None
    username: str = None
    admin: bool = False
    password: str = None