"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *  #importa la librería random
from turtle import *  # importa la librería turtle

from freegames import path  #importa la función path de la librería freegames

car = path('car.gif')       #guarda una imagen de un carro en la variable car
tiles = list(range(32)) * 2   
state = {'mark': None}
hide = [True] * 64


def square(x, y):  #Esta funcion se encarga de crear los cuadrados del juego 
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):  
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 
                50 + ((y + 200) // 
                50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return ((count % 8) * 5
             0 - 200, 
            (count // 8) * 50 - 200)

def tap(x, y):   "Devuelve el comportamiento del juego dependiendo del cuadro que se escoga
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    cuentatap= 0;

    if (mark is None or mark == spot or 
        tiles[mark] != tiles[spot]):
        state['mark'] = spot
	cuentatap=cuentatap+1
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
	cuentatap=cuentatap+1


def draw():     #Esta funcion dibuja el cuandro en cuanto se haya detectado una respuesta correcta
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)  #Esta función se encarga de darle la figura de el  nombre que se le introduzca 
    stamp()     

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30,
                                 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()