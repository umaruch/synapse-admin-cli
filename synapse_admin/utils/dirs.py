from pathlib import Path

from synapse_admin.types.users_rooms import UserRoom


def get_homedir():
    return str(Path.home())

def get_users_rooms_from_file(file):
    if not Path(file).is_file():
        print("File not found")
        exit(1)

    users_rooms = []
    with open(file, "r") as f:
        for line in f:
            data = line.rstrip("\n").split(";")
            users_rooms.append(UserRoom(data[0], data[1]))

    return users_rooms