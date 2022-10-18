from synapse_admin.tools.base import AbstractCommand
from synapse_admin.utils import args_parser

from .add_room import AddRoomCommand

command_routers = {
    AddRoomCommand.command_str: AddRoomCommand.run
}


class UsersCommand(AbstractCommand):
    command_str = "users"

    @staticmethod
    def run(args):
        parser = args_parser.get()
        parser.add_argument("command", choices=command_routers.keys(), help="User query")
        
        req_args,  unknown_args = parser.parse_known_args(args)
        command_routers[req_args.command](unknown_args)