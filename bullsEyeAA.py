# bullsEye by akhi abdullah

from graphics import *

cirSz=50
cirCol = "red"
cirX = cirSz*5
cirY = cirSz*5


def draw_cir(cX, cY, size, color, bullWin):
    circle = Circle(Point(cX,cY), size)
    circle.setFill(color)
    circle.draw(bullWin)

def draw_be(bX, bY, rings, bSize, bColor, bullWin):
    for i in range (rings):
        if (i) % 2 == 1:
            bColor = "white"
        else:
            bColor = "red"

        bSize -= 10
        draw_cir(bX, bY, bSize, bColor, bullWin)
        
    
    


bullWin = GraphWin("BullsEye",cirSz*10, cirSz*10)
bullWin.setCoords(0,0,cirSz*10, cirSz*10)

##for i in range(4):
##    if (i) % 2 == 1:
##        cirCol = "white"
##    else:
##        cirCol = "red"
##    
##    cirSz -= 10
##    draw_cir(cirX, cirY, cirSz, cirCol, bullWin)

draw_be(cirX, cirY, 6, cirSz, cirCol, bullWin)


bullWin.getMouse()
bullWin.close()
