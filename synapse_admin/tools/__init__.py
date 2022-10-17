from .init import InitCommand


command_routers = {
    InitCommand.command_str: InitCommand.run
}