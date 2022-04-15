"""
A interface Observer declara o método update s que será utilizado pelos
sujeitos para notificar os observers.
"""

from abc import ABC, abstractmethod
from observer.publicadora_interface import PublicadoraInterface


class Observer(ABC):

    @abstractmethod
    def update(self, sujeito: PublicadoraInterface) -> None:
        """
        Recebe atualização de um sujeito.
        """
        pass

