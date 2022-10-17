import getpass
from re import U
from synapse_admin.utils import config

from .base import AbstractCommand
from synapse_admin.utils.api import auth

class InitCommand(AbstractCommand):
    """
        Init synapse admin config and login 
        TODO Доделать проверку URL по регулярке
        TODO Возможно какие-то ветвления логики в зависимости от ввода пользователем
    """
    command_str = "init"

    def run(args):
        synapse_url = input("Enter Synapse Matrix server URL:")
        synapse_username = input("Enter server admin username:")
        synapse_password = getpass.getpass("Enter password:")

        server_url = synapse_url
        user_id, access_token = auth.login(synapse_url, synapse_username, synapse_password)
        print("Successfully login")

        config.save(server_url, user_id, access_token)
        print("New configuration saved")
