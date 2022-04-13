"""Código adaptado de https://www.youtube.com/watch?v=G8FTDsD9L_g """

from abc import abstractmethod, ABCMeta

#classe abstrata Estado
class Estado(metaclass=ABCMeta):
    @abstractmethod
    def transitar_para(self):
        pass

#nesse exemplo, essa classe representa o contexto (sabe transitar entre estados)
class EstacaoDeRadio(Estado):
    def __init__(self):
        self._estado = None

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    #chama o transitar_para() do estado atual
    def transitar_para(self):
        self.estado = self.estado.transitar_para()


class Ligado(Estado):
    def transitar_para(self):
        print("Ligando o rádio...")
        return self

    def __init__(self):
        self.transitar_para()

class Desligado(Estado):
    def transitar_para(self):
        print("Desligando o rádio...")
        return self

    def __init__(self):
        self.transitar_para()

class AumentoDoVolume(Estado):
    def transitar_para(self):
        print("Aumentando o volume em 10...")
        return self

    def __init__(self):
        self.transitar_para()

class ReducaoDoVolume(Estado):
    def transitar_para(self):
        print("Reduzindo o volume em 10...")
        return self

    def __init__(self):
        self.transitar_para()

Radio = EstacaoDeRadio()
print(f"O estado atual do rádio é: {type(Radio.estado).__name__}")

Radio.estado = Ligado()
print(f"O estado atual do rádio é: {type(Radio.estado).__name__}")

print("Aumentando o volume...")
Radio.estado = AumentoDoVolume()
#Radio.transitar_para()
print(f"O estado atual do rádio é: {type(Radio.estado).__name__}")

print("Desligando o dispositivo...")
Radio.estado = Desligado()
#Radio.transitar_para()
print(f"O estado atual do rádio é: {type(Radio.estado).__name__}")
