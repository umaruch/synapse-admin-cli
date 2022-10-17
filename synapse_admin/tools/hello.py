from .base import AbstractCommand


class HelloCommand(AbstractCommand):
    command_str = "hello"

    @staticmethod
    def run():
        print("Hello World")