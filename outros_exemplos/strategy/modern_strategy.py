from outros_exemplos.strategy.classical_strategy import Venda


def icms_calc(venda: Venda) -> float:
    return venda.total_venda() * 0.04


def iss_calc(venda: Venda) -> float:
    return venda.total_venda() * 0.02


# --------------------------CÓDIGO CLIENTE ABAIXO-------------------------------

venda = Venda("Caneta", 1.5, 56)
icms = icms_calc(venda)
iss = iss_calc(venda)

print(f"O produto comprado foi {venda.produto}.\n"
      f"A quantidade comprada foi {venda.quantidade}\n"
      f"O total é de {venda.total_venda()}\n"
      f"ICMS: {icms}\n"
      f"ISS: {iss}\n"
      f"Obrigado pela compra!")
