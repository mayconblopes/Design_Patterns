from abc import ABC, abstractmethod


class Venda:
    """
    Classe que representa o objeto venda, que contem um produto, o seu preço unitário e a quantidade vendida
    """

    def __init__(self, produto: str, preco_unidade: float, quantidade: int) -> None:
        self._produto: str = produto
        self._preco_unidade: float = preco_unidade
        self._quantidade: int = quantidade

    # abaixo os métodos 'gets'
    @property
    def produto(self) -> str:
        return self._produto

    @property
    def preco_unidade(self) -> float:
        return self._preco_unidade

    @property
    def quantidade(self) -> int:
        return self._quantidade

    # método para retornar o total da venda com base no preço unitário do produto e quantidade
    def total_venda(self) -> float:
        return self._preco_unidade * self._quantidade


class CalculadoraImposto(ABC):
    """
    Interface para calcular os impostos concretos.
    Possui um atributo imposto que contém o resultado do cálculo do imposto.
    """

    _total_imposto: float

    # o próprio construtor já chama a calculadora
    def __init__(self, venda: Venda):
        self._total_imposto = self.calcular_imposto(venda)
        print(f"Construtor calculou o imposto em {self._total_imposto}")

    @abstractmethod
    def calcular_imposto(self, venda: Venda) -> float:
        return self._total_imposto

    @property
    def total_imposto(self):
        return self._total_imposto


class CalculadoraIcms(CalculadoraImposto):
    """
    Classe que criará uma calculadora concreta para elaborar o cálculo do ICMS
    """

    def calcular_imposto(self, venda: Venda) -> float:
        # Neste exemplo, o ICMS representa 4% do valor da venda
        self._total_imposto = venda.total_venda() * 0.04
        return self._total_imposto


class CalculadoraIss(CalculadoraImposto):
    """
    Classe que criará uma calculadora concreta para elaborar o cálculo do ISS
    """

    def calcular_imposto(self, venda: Venda) -> float:
        # Neste exemplo, o ISS representa 2% do valor da venda
        self._total_imposto = venda.total_venda() * 0.02
        return self._total_imposto


# --------------------------CÓDIGO CLIENTE ABAIXO-------------------------------

venda = Venda("Caneta", 1.5, 26)
icms = CalculadoraIcms(venda).total_imposto
iss = CalculadoraIss(venda).total_imposto

print(f"O produto comprado foi {venda.produto}.\n"
      f"A quantidade comprada foi {venda.quantidade}\n"
      f"O total é de {venda.total_venda()}\n"
      f"ICMS: {icms}\n"
      f"ISS: {iss}\n"
      f"Obrigado pela compra!")
