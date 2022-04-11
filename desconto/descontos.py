from abc import ABCMeta, abstractmethod


# classe abstrata
class Desconto(metaclass=ABCMeta):
    def __init__(self, proximo):
        self.__proximo = proximo

    @property
    def proximo(self):
        return self.__proximo

    @abstractmethod
    def calcular(self, orcamento):
        pass


class DescontoMaisDe5Itens(Desconto):

    def __init__(self, proximo):
        super().__init__(proximo)

    def calcular(self, orcamento):
        if orcamento.qtd_itens > 5:
            return orcamento.valor * 0.1
        else:
            return super().proximo.calcular(orcamento)


class DescontoMaisDe500Reais(Desconto):

    def __init__(self, proximo):
        super().__init__(proximo)

    def calcular(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.05
        else:
            return super().proximo.calcular(orcamento)


class SemDesconto(Desconto):
    def __init__(self):
        super().__init__(None)

    def calcular(self, orcamento):
        return 0
