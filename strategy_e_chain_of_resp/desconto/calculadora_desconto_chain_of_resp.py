from strategy_e_chain_of_resp.desconto.descontos import DescontoMaisDe500Reais, DescontoMaisDe5Itens, SemDesconto

class CalculadoraDeDescontos:

    def calcular(self, orcamento):
        #aqui está acontecendo o Chain of Responsability
        desc = DescontoMaisDe5Itens(DescontoMaisDe500Reais(SemDesconto())).calcular(orcamento)
        return desc
