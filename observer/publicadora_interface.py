from abc import ABC, abstractmethod


class PublicadoraInterface(ABC):
    """
    A Publicadora é uma interface que declara os métodos para gerenciar inscritos
    """

    def __init__(self):
        # Esse é o atributo que guarda o estado que será observador:
        self._estado = None

        # Essa é a lista de observadores inscritos:
        self._observers: list = []

    @property
    def estado(self) -> int:
        return self._estado

    @property
    def observers(self) -> list:
        return self._observers

    @abstractmethod
    def anexar_observer(self, observer) -> None:
        """
        Anexa um observer na Publicadora
        """
        pass

    @abstractmethod
    def desanexar_observador(self, observer) -> None:
        """
        Desanexa um observador da Publicadora
        """
        pass

    @abstractmethod
    def notifica_inscritos(self) -> None:
        """
        Notifica todos os observadores inscritos na Publicadora
        """
        pass
