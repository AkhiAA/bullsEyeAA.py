# bullsEye by akhi abdullah

from graphics import *
from random import *

def draw_cir(cX, cY, size, color, bullWin):
    circle = Circle(Point(cX,cY), size)
    circle.setFill(color)
    circle.draw(bullWin)

def draw_be(bX, bY, rings, rSize, bColor1, bColor2, bullWin):
    bSize = rSize * rings
    for i in range (rings):
        if (i) % 2 == 1:
            bColor = bColor1
        else:
            bColor = bColor2
        draw_cir(bX, bY, bSize, bColor, bullWin)
        bSize -= rSize
        
cirSz=60
#cirCol1 = "red"
cirCol2 = "orange"
cirX = cirSz*5
cirY = cirSz*5
    
   
bullWin = GraphWin("BullsEye",cirSz*10, cirSz*10)
bullWin.setCoords(0,0,cirSz*10, cirSz*10)

for j in range (20):
    ranX = randint(cirSz, cirSz * 9)
    ranY = randint(cirSz, cirSz * 9)
    ranRs = randint(3, 20)
    ranRed = randint(0,255)
    ranG = randint(0,255)
    ranB = randint(0,255)
    cirCol1 = color_rgb(ranRed, ranG, ranB)
    draw_be(ranX, ranY, ranRs, 6, cirCol1, cirCol2, bullWin)


bullWin.getMouse()
bullWin.close()
