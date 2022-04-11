# Calculadora de Impostos sem Strategy
"""
class CalculadoraDeImpostos:

    def calcular(self, orcamento, tipo_imposto):
        if tipo_imposto == "ISS":
            return orcamento.valor * 0.06
        elif tipo_imposto == "ICMS":
            return  orcamento.valor * 0.1
        else:
            return 0"""


# Calculadora de Impostos usando Strategy
class CalculadoraDeImpostos:

    def calcular(self, imposto, orcamento):
        return imposto.calcular(orcamento)
