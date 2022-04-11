from imposto.impostos import Iss, Icms
from imposto.calculadora_impostos_strategy import CalculadoraDeImpostos
from loja.orcamento import Orcamento
from desconto.calculadora_desconto_chain_of_resp import CalculadoraDeDescontos
from desconto.descontos import DescontoMaisDe500Reais, DescontoMaisDe5Itens

o = Orcamento(200, 5)
calc_imposto = Icms().calcular(o)
calc_desc = CalculadoraDeDescontos().calcular(o)

print("Imposto: ", calc_imposto)
print("Desconto: ", calc_desc)
