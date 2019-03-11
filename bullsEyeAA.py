# bullsEye by akhi abdullah
from graphics import *

def draw_cir(cX, cY, size, color, bullWin):
    circle = Circle(Point(cX,cY), size)
    circle.setFill(color)
    circle.draw(bullWin)

cirSz=50
cirCol = "dark red"

bullWin = GraphWin("BullsEye",cirSz*10, cirSz*10)
bullWin.setCoords(0,0,cirSz*10, cirSz*10)

draw_cir(cirSz*5, cirSz*5, cirSz, cirCol, bullWin)




bullWin.getMouse()
bullWin.close()
