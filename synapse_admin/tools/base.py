from abc import ABC, abstractstaticmethod

class AbstractCommand(ABC):
    command_str = None

    @abstractstaticmethod
    def run():
        """
            Abstract method 
        """
        pass
