print("--------------------------CLASSICAL STRATEGY-------------------------------")
from outros_exemplos.strategy.classical_strategy import Venda, CalculadoraIcms, CalculadoraIss

venda = Venda("Caneta", 1.5, 26)
icms = CalculadoraIcms(venda).total_imposto
iss = CalculadoraIss(venda).total_imposto

print(f"O produto comprado foi {venda.produto}.\n"
      f"A quantidade comprada foi {venda.quantidade}\n"
      f"O total é de {venda.total_venda()}\n"
      f"ICMS: {icms}\n"
      f"ISS: {iss}\n"
      f"Obrigado pela compra!")


print("--------------------------MODERN STRATEGY-------------------------------")
from outros_exemplos.strategy.modern_strategy import icms_calc, iss_calc

venda = Venda("Caneta", 1.5, 56)
icms = icms_calc(venda)
iss = iss_calc(venda)

print(f"O produto comprado foi {venda.produto}.\n"
      f"A quantidade comprada foi {venda.quantidade}\n"
      f"O total é de {venda.total_venda()}\n"
      f"ICMS: {icms}\n"
      f"ISS: {iss}\n"
      f"Obrigado pela compra!")