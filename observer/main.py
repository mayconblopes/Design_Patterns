from observer.observers import Observer1, Observer2
from observer.sujeito1 import Sujeito1

sujeito = Sujeito1()
observador1 = Observer1()
observador2 = Observer2()

sujeito.anexar_observer(observador1)
sujeito.anexar_observer(observador2)

sujeito.logica_de_negocio1()
