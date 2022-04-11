""" a interface consiste em uma estrutura da linguagem que garante que todos que a implementarem terão a obrigação de
implementar todos os métodos abstratos nela. """

from abc import ABCMeta, abstractmethod

class Imposto(metaclass = ABCMeta):

    @abstractmethod
    def calcular (orcamento):
        pass
