from jugador import Jugador
from tablero import Tablero

j1 = Jugador("Pepe")
j2 = Jugador("María")
t = Tablero(j1, j2)

#print(t.ficha(1, 1) in j1.fichas())
#print(t.ficha(1, 1) in j1.fichas() == True)

print(t.mover(t.ficha(3, 3), "IZQ") == t.ficha(2, 4))

#print(t.ficha(4, 8).color() != t.ficha(4, 2).color())
#print(j1.fichas()[0].color() == j1.fichas()[1].color())
