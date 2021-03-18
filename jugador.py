from ficha import Ficha

class Jugador:

    def __init__(self, nombre):
        __numero = 0
        self.__nombre = nombre
        self.__lista_fichas = []
        while __numero < 12:
            self.__lista_fichas.append(Ficha())
            __numero += 1

    def nombre(self):
        return self.__nombre

    def fichas(self):
        return self.__lista_fichas

"""
    def siguiente_movimiento():

"""
