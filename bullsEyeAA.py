# bullsEye by akhi abdullah
from graphics import *

def draw_cir(cX, cY, size, color, bullWin):
    circle = Circle(Point(cX,cY), size)
    circle.setFill(color)
    circle.draw(bullWin)

cirSz=50
cirCol = "dark red"
cirX = cirSz*5
cirY = cirSz*5

bullWin = GraphWin("BullsEye",cirSz*10, cirSz*10)
bullWin.setCoords(0,0,cirSz*10, cirSz*10)

for i in range(4):
    cirSz -= 10
    draw_cir(cirX, cirY, cirSz, cirCol, bullWin)




bullWin.getMouse()
bullWin.close()
