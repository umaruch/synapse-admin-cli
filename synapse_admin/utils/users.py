from pathlib import Path

from . import dirs
from synapse_admin.types.users import User


def get_users_from_file(file):
    if not Path(file).is_file():
        print("File not found")
        exit(1)

    users = []
    with open(file, "r") as f:
        for line in f:
            data = line.rstrip("\n").split(";")
            users.append(User(username=data[0], displayname=data[1], admin=True if data[2]==1 else False))

    return users


def print_users_to_file(users):
    with open(dirs.get_homedir()+"/registered_user.txt", "w") as f:
        for user in users:
            # id, displayname, username, password, admin 
            f.write("{:<30}|{:<20}|{:<12}|{:<16}|{}\n".format(
                user.id, user.displayname, user.username, user.password, user.admin
            ))
    