from .init import InitCommand
from .register import RegisterCommand
from .users import UsersCommand


command_routers = {
    InitCommand.command_str: InitCommand.run,
    RegisterCommand.command_str: RegisterCommand.run,
    UsersCommand.command_str: UsersCommand.run
}