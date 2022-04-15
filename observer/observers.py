"""
Aqui os observadores concretos que implementam a interface Observer são criados
"""

from observer.observer_interface import Observer
from observer.publicadora_interface import PublicadoraInterface
from observer.sujeito1 import Sujeito1


class Observer1(Observer):
    def update(self, sujeito: PublicadoraInterface) -> None:
        if sujeito.estado < 3:
            print("\nObserver1 diz: Identifiquei um evento que me diz respeito!")


class Observer2(Observer):
    def update(self, sujeito: PublicadoraInterface) -> None:
        if sujeito.estado == 0 or sujeito.estado >= 2:
            print("\nObserver2 diz: Identifiquei um evento que me diz respeito!")
