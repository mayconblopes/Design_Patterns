from outros_exemplos.strategy.classical_strategy import Venda


def icms_calc(venda: Venda) -> float:
    return venda.total_venda() * 0.04


def iss_calc(venda: Venda) -> float:
    return venda.total_venda() * 0.02



