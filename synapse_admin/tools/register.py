from .base import AbstractCommand
from synapse_admin.utils import args_parser, users, config, security
from synapse_admin.utils.api import auth, users as users_api
from synapse_admin.types.users import User


def _register_single_user(server_url, secret_key, access_token, set_display_name):
    user = User(
        username=input("Enter user username:"),
        displayname=input("Enter user displayname:"),
        admin=True if input("Is admin(1-yes/0-no(default):") else False
    )
    user.password = security.generate_password()

    auth.register(server_url, user, secret_key)
    print("Registration complete")
    if set_display_name:
        users_api.set_display_name(server_url, access_token, user)  
        print("Set display name complete")

    print(user)


def _register_multiple_users(server_url, secret_key, access_token, users_file, set_display_name):
    users_list = users.get_users_from_file(users_file)
    users_count = len(users_list)

    print("Get {} entries from file".format(users_count))

    for i in range(0, users_count):
        users_list[i].password = security.generate_password()

        auth.register(server_url, users_list[i], secret_key)
        print("({}/{}) Registration complete".format(i+1, users_count))

        if set_display_name:
            users_api.set_display_name(server_url, access_token, users_list[i])  
            print("({}/{}) Set display name complete".format(i+1, users_count))

    users.print_users_to_file(users_list)


class RegisterCommand(AbstractCommand):
    """
        Work with registration API
    """
    command_str = "register"

    @staticmethod
    def run(args):
        parser = args_parser.get()
        parser.add_argument("--file", default=None, help="path to file with users list")

        parser.add_argument('--setdisplayname', action='store_true')
        parser.add_argument('--no-setdisplayname', dest='setdisplayname', action='store_false')
        parser.set_defaults(setdisplayname=False)

        reg_args = parser.parse_args(args)

        shared_secret = input("Enter shared secret from synapse config:")

        config_data = config.load()

        if reg_args.file:
            _register_multiple_users(config_data.server_url, shared_secret, config_data.loged_as.access_token, reg_args.file, reg_args.setdisplayname)
        else:
            _register_single_user(config_data.server_url, shared_secret, config_data.loged_as.access_token, reg_args.setdisplayname)