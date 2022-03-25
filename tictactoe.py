"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from tkinter import CENTER
from turtle import *
import turtle

from freegames import line

arr= []

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    turtle.color("blue")
    """Draw X player."""
    line(x+25, y+25, x + 117, y + 117,)
    line(x+25, y + 117, x + 117, y+25)
 


def drawo(x, y):
    turtle.color("green")
    """Draw O player."""
    up()
    goto(x + 70, y + 15)
    down()
    circle(50)

def drawp(x, y):
    turtle.color("red")
    """Draw O player."""
    up()
    goto(x + 30, y + 60)
    down()
    circle(50)

def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo, drawp] # Aquí se define que jugador esta jugando segun el index 0 = x y 1 = o 


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    xy= [x,y]
    player = state['player']
    draw = players[player]
    if xy not in arr:
        arr.append(xy) 
        draw(x, y)
        update()
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
