from loja.imposto.impostos import Icms
from loja.orcamento import Orcamento
from loja.desconto.calculadora_desconto_chain_of_resp import CalculadoraDeDescontos

o = Orcamento(200, 5)
calc_imposto = Icms().calcular(o)
calc_desc = CalculadoraDeDescontos().calcular(o)

print("Imposto: ", calc_imposto)
print("Desconto: ", calc_desc)
