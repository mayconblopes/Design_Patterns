"""
Aqui é definido o Invoker, também conhecido como controle.
É o objeto que vai entregar o pedido ao objeto que vai executá-lo.
"""

from command.smart_house_command_interface import SmartHouseCommandInterface


# essa classe é o invoker
class SmartHouseApp:
    def __init__(self) -> None:
        self._commands = {}

    def add_command(self, key: str, command: SmartHouseCommandInterface) -> None:
        self._commands[key] = command

    def execute_command(self, key: str) -> None:
        # delega a execução ao objeto que está na posição key
        self._commands[key].execute()

    def undo_command(self, key: str) -> None:
        # delega a execução ao objeto que está na posição key
        self._commands[key].undo()
