"""
Código adaptado de https://refactoring.guru/pt-br/design-patterns/state/python/example
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Contexto:
    """
    O Contexto define a interface para os clientes. Também possui a referência
    para a instância do Estado, que representa o corrente estado do Contexto.
    """

    _estado = None
    """
    Essa é a referência para o estado atual do Contexto.
    """

    def __init__(self, estado: Estado) -> None:
        self.transitar_para(estado)

    def transitar_para(self, estado: Estado):
        """
        O Contexto permite a mudança de estado em tempo de execução.
        """

        print(f"Contexto: Transição para {type(estado).__name__}")
        self._estado = estado
        self._estado.contexto = self

    """
    O Contexto delega uma parte de seu comportamento para o Estado atual do objeto.
    """

    def requisicao1(self):
        self._estado.handle1()

    def requisicao2(self):
        self._estado.handle2()


class Estado(ABC):
    """
    A superclasse Estado declara métodos que devem ser implementados
    por todos os Estados Concretos e também provê referência para o
    objeto Contexto do Estado. Essa referência pode ser utilizada
    pelo Estado para fazer transição do Contexto para outro Estado.
    """

    @property
    def contexto(self) -> Contexto:
        return self._contexto

    @contexto.setter
    def contexto(self, contexto: Contexto) -> None:
        self._contexto = contexto

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Os Estados Concretos implementam vários comportamentos, associados
com o estado do Contexto.
"""


class EstadoConcretoA(Estado):
    def handle1(self) -> None:
        print("EstadoConcretoA lida com requisição 1.")
        print("EstadoConcretoA quer mudar o estado atual do contexto.")
        self.contexto.transitar_para(EstadoConcretoB())

    def handle2(self) -> None:
        print("EstadoConcretoA lida com requisição 2.")


class EstadoConcretoB(Estado):
    def handle1(self) -> None:
        print("EstadoConcretoB lida com requisição 1.")

    def handle2(self) -> None:
        print("EstadoConcretoB handles lida com requisição 2.")
        print("EstadoConcretoB quer mudar o estado atual do contexto.")
        self.contexto.transitar_para(EstadoConcretoA())


if __name__ == "__main__":

    contexto = Contexto(EstadoConcretoA())
    contexto.requisicao1()
    contexto.requisicao2()
