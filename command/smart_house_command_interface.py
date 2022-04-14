"""
SmartHouseCommandInterface é a interface, isto é, que definirá o contrato para
os comandos concretos implementarem.
"""

from abc import ABCMeta, abstractmethod


class SmartHouseCommandInterface(metaclass=ABCMeta):

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass
