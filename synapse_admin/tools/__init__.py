from .hello import HelloCommand


command_routers = {
    HelloCommand.command_str: HelloCommand.run
}