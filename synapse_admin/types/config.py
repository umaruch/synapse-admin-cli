from dataclasses import dataclass


@dataclass
class LogedUser:
    user_id: str
    access_token: str


@dataclass
class Config:
    server_url: str = None
    loged_as: LogedUser = None