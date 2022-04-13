"""
Código adaptado de https://refactoring.guru/design-patterns/template-method/python/example
"""

from abc import ABCMeta, abstractmethod


class ClasseAbstrata(metaclass=ABCMeta):
    """
    A Classe Abstrata cria o Template Method que vai conter o esqueleto de algum código,
    que vai chamar métodos abstratos a serem implementados pelas classes filhas.

    As classes filhas implementam esses métodos que lhe dizem respeito, sem tocar no
    restante do template method, que continua sendo implementado pela classe mãe.
    """

    def template_method(self) -> None:
        """
        Aqui vamos criar o esqueleto do código com o template method.
        """

        self.operacao_mae1()
        self.operacao_delegada1()
        self.operacao_mae2()
        self.gancho1()
        self.operacao_delegada2()
        self.operacao_mae3()
        self.gancho2()

    # os métodos (ou operações) abaixo jã possuem implementação:

    def operacao_mae1(self) -> None:
        print("Classe abstrata diz: eu estou fazendo a maior parte do trabalho")

    def operacao_mae2(self) -> None:
        print("Classe abstrata diz: mas eu permito que minhas filhas sobrescrevam algumas operações")

    def operacao_mae3(self) -> None:
        print("Classe abstrata diz: mas eu continuo fazendo a maior parte do trabalho")

    # Esses métodos abaixo precisam ser implementados nas classes filhas:

    @abstractmethod
    def operacao_delegada1(self) -> None:
        pass

    @abstractmethod
    def operacao_delegada2(self) -> None:
        pass

    # Existem "ganchos". As classes filhas podem sobrescrevê-los, mas isso não é obrigatório
    # já que os ganchos possuem implementações padrões, embora vazias. Os ganchos garantem
    # a possibilidade de fazer extensões em pontos cruciais do algoritmo:

    def gancho1(self) -> None:
        pass

    def gancho2(self) -> None:
        pass


class ClasseConcreta1(ClasseAbstrata):
    """
    As classes concretas devem implementar todos os métodos da classe mãe.
    Podem também sobcrescrever alguns métodos que foram implementados como padrão.
    """

    def operacao_delegada1(self) -> None:
        print("ClasseConcreta1 diz: Sobrescrevi a operacao_delegada1()")

    def operacao_delegada2(self) -> None:
        print("ClasseConcreta1 diz: Sobrescrevi a operacao_delegada2()")


class ClasseConcreta2(ClasseAbstrata):
    """
    Normalmente as classes filhas sobrescrevem apenas parte das implementações padrões.
    """

    def operacao_delegada1(self) -> None:
        print("ClasseConcreta2 diz: Sobrescrevi a operacao_delegada1()")

    def operacao_delegada2(self) -> None:
        print("ClasseConcreta2 diz: Sobrescrevi a operacao_delegada2()")

    def gancho1(self) -> None:
        print("ClasseConcreta2 diz: Sobrescrevi o gancho1()")


def cliente(classe_abstrata: ClasseAbstrata) -> None:
    """
    O código do cliente chama o template method para executar o algoritmo. O Cliente
    não precisa conhecer a classe concreta de um objeto com o qual trabalha.
    """

    # ...
    classe_abstrata.template_method()
    # ...


if __name__ == "__main__":
    print("O mesmo código cliente pode funcionar com diferentes subclasses:")
    cliente(ClasseConcreta1())
    print("")

    print("O mesmo código cliente pode funcionar com diferentes subclasses:")
    cliente(ClasseConcreta2())
