"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *
import turtle
from freegames import line

arr = []


def grid():  # Aqui definimos los cuadrantes o rejilla del juego
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):  # con esta funcion dibujamos el simbolo (X)
    turtle.color("blue")
    """Draw X player."""
    line(x+25, y+25, x + 117, y + 117,)
    line(x+25, y + 117, x + 117, y+25)


def drawo(x, y):  # con esta funcion dibujamos el simbolo (O)
    turtle.color("green")
    """Draw O player."""
    up()
    goto(x + 70, y + 15)
    down()
    circle(50)


# con esta funcion determinamos los limites de
# cada cuadrante en el que hacemos click
def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
# Aquí se define que jugador esta jugando segun el index 0 = X y 1 = O
players = [drawx, drawo]


# Esta funcion es la que al hacer click o (tap) nos dibuja
# el simbolo de X o de O en el cuadrante que se elija
def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    xy = [x, y]
    player = state['player']
    draw = players[player]
    if xy not in arr:
        arr.append(xy)  # Este arreglo nos permite identificar si un cuadrante
        # esta ocupado o si esta libre para poder dibujar un nuevo simbolo
        draw(x, y)
        update()  # actualiza la ventana del juego
        # para que aparezca el dibujo hecho
        state['player'] = not player
    else:
        return


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
