

class Orcamento:

    def __init__(self, valor, qtd_itens):
        self.__valor = valor
        self.__qtd_itens = qtd_itens

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def qtd_itens(self):
        return self.__qtd_itens

    @qtd_itens.setter
    def qtd_itens(self, qtd_itens):
        self.__qtd_itens = qtd_itens



