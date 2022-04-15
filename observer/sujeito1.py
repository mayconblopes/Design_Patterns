"""
Sujeito é um objeto que possui um estado que será observado.
Sujeito implementa a interface da Publicadora.
"""


from random import randrange
from observer.observer_interface import PublicadoraInterface, Observer


class Sujeito1(PublicadoraInterface):
    """
    O Sujeito1 é um objeto que possui um estado que é de interesse de um ou mais observers.
    Sujeito1 implementa os métodos da PublicadoraInterface, logo ele sabe anexar,
    remover e também notificar os observers.
    """

    # A seguir, os métodos para gerenciar os observadores:
    def anexar_observer(self, observer: Observer) -> None:
        print(f"Sujeito1 diz: anexei o observador {type(observer).__name__}")
        self.observers.append(observer)

    def desanexar_observador(self, observer: Observer) -> None:
        print(f"Sujeito1 diz: desanexei o observador {type(observer).__name__}")
        self.observers.remove(observer)

    def notifica_inscritos(self) -> None:
        """
        Aciona um update em cada inscrito.
        """
        print("Sujeito1 diz: Notificando todos os observadores...")
        for observer in self.observers:
            observer.update(self)

    def logica_de_negocio1(self) -> None:
        """
        Aqui vemos um método que simula uma lógica qualquer do negócio.
        O estado do Sujeito1 é alterado e ele notifica os seus observadores.
        """
        print("\nSujeito1 diz: Estou fazendo algo muito importante agora")
        self._estado = randrange(0, 10)

        print(f"Sujeito1 diz: Meu estado acabou de mudar para {self._estado}")
        self.notifica_inscritos()
