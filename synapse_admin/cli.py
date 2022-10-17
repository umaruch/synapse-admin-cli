from synapse_admin.utils import args_parser
from synapse_admin.tools import command_routers


def main():
    parser = args_parser.get()
    parser.add_argument("command", choices=command_routers.keys(), help="admin cli commands")

    args, unknown_args = parser.parse_known_args()
    command_routers[args.command](unknown_args)


if __name__ == "__main__":
    main()