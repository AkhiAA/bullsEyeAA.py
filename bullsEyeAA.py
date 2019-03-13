# bullsEye by akhi abdullah

from graphics import *

def draw_cir(cX, cY, size, color, bullWin):
    circle = Circle(Point(cX,cY), size)
    circle.setFill(color)
    circle.draw(bullWin)

def draw_be(bX, bY, rings, bSize, bColor1, bColor2, bullWin):
    for i in range (rings):
        if (i) % 2 == 1:
            bColor = bColor1
        else:
            bColor = bColor2

        bSize -= 10
        draw_cir(bX, bY, bSize, bColor, bullWin)
        
cirSz=60
cirCol = "red"
cirX = cirSz*5
cirY = cirSz*5
    
   
bullWin = GraphWin("BullsEye",cirSz*10, cirSz*10)
bullWin.setCoords(0,0,cirSz*10, cirSz*10)


##    draw_cir(cirX, cirY, cirSz, cirCol, bullWin)

draw_be(cirX, cirY, 6, cirSz, cirCol, "blue", bullWin)


bullWin.getMouse()
bullWin.close()
