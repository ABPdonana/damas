from ficha import Ficha
from jugador import Jugador

class Tablero:

    def __init__(self, jugador1, jugador2):
        self.__jugador1 = jugador1
        self.__jugador2 = jugador2
        self.__lista_fichas = []
        self.__inicio_ficha_blanca(jugador1)
        self.__inicio_ficha_negra(jugador2)

    def jugador1(self):
        return self.__jugador1

    def jugador2(self):
        return self.__jugador2

    def __inicio_ficha_blanca(self, jugador):
        __fila = 1
        __columna = 1
        for x in jugador.fichas():
            x.set_color("B")
            x.set_posicion(__fila, __columna)
            __fila += 2
            if __fila > 8:
                __columna += 1
                if __columna % 2 == 0:
                    __fila = 2
                else:
                    __fila = 1
            self.__lista_fichas.append(x)

    def __inicio_ficha_negra(self, jugador):
        __fila = 2
        __columna = 6
        for x in jugador.fichas():
            x.set_color("N")
            x.set_posicion(__fila, __columna)
            __fila += 2
            if __fila > 8:
                __columna += 1
                if __columna % 2 == 0:
                    __fila = 2
                else:
                    __fila = 1
            self.__lista_fichas.append(x)

    def ficha(self, fila, columna):
        for x in self.__lista_fichas:
            if x.fila() == fila and x.columna() == columna:
                return x
        return None

    @staticmethod
    def mover(obj_ficha, direccion):
        #if direccion != "DER" or direccion != "IZQ":
        #    raise ValueError("Dirección no válida")
        if obj_ficha.color() == "B":
            if direccion == "DER":
                obj_ficha.set_posicion(obj_ficha.fila() + 1, obj_ficha.columna() + 1)
            else:
                obj_ficha.set_posicion(obj_ficha.fila() - 1, obj_ficha.columna() + 1)
        else:
            if direccion == "DER":
                obj_ficha.set_posicion(obj_ficha.fila() + 1, obj_ficha.columna() - 1)
            else:
                obj_ficha.set_posicion(obj_ficha.fila() - 1, obj_ficha.columna() - 1)
"""
    def siguiente_turno(self):
        siguiente_movimiento()
"""
