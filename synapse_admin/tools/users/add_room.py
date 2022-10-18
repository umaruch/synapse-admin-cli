from synapse_admin.tools.base import AbstractCommand
from synapse_admin.utils import args_parser, config, dirs
from synapse_admin.utils.api import users
from synapse_admin.types.users_rooms import UserRoom


def _add_single_user(server_url, access_token):
    user_room = UserRoom(
        user_id=input("Enter user id:"),
        room_id=input("Enter room id:")
    )

    users.add_to_room(server_url, access_token, user_room.user_id, user_room.room_id)
    print("Add to room complete")

def _add_multiple_users(server_url, access_token, users_rooms_file):
    users_rooms = dirs.get_users_rooms_from_file(users_rooms_file)
    count = len(users_rooms)
    
    print("Get {} entries from file".format(count))
    for i in range(0, count):
        users.add_to_room(server_url, access_token, users_rooms[i].user_id, users_rooms[i].room_id)
        print("({}/{}) Add to room complete".format(i+1, count))


class AddRoomCommand(AbstractCommand):
    command_str = "addroom"

    @staticmethod
    def run(args):
        parser = args_parser.get()
        parser.add_argument("--file", default=None, help="path to file with user;room list")
        
        req_args = parser.parse_args(args)

        config_data = config.load()

        if req_args.file:
            _add_multiple_users(config_data.server_url, config_data.loged_as.access_token, req_args.file)
        else:
            _add_single_user(config_data.server_url, config_data.loged_as.access_token)
