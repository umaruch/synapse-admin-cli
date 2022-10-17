import argparse

from .tools import command_routers


def main():
    parser = argparse.ArgumentParser(
        prog="Synapse Admin by neko",
        description="Synapse local server administration tools"
    )
    parser.add_argument("command", choices=command_routers.keys(), help="admin cli commands")

    args, unknown_args = parser.parse_known_args()
    command_routers[args.command]()


if __name__ == "__main__":
    main()