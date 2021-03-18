class Ficha:

    def __init__(self):
        self.__color = None
        self.__posicion = [None, None]

    def set_color(self, color):
        self.__color = color

    def set_posicion(self, fila, columna):
        self.__posicion = [fila, columna]

    def color(self):
        return self.__color

    def posicion(self):
        return self.__posicion

    def fila(self):
        return self.posicion()[0]

    def columna(self):
        return self.posicion()[1]
