"""Para implementar o Strategy, precisei criar uma classe para cada tipo de imposto e os objetos dessas classes sabem
como calcular seus impostos """


from strategy_e_chain_of_resp.imposto.imposto_iterface import Imposto


class Icms(Imposto):

    def calcular(self, orcamento):
        return orcamento.valor * 0.1


class Iss(Imposto):

    def calcular(self, orcamento):
        return orcamento.valor * 0.06
