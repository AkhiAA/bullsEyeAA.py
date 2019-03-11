# bullsEye by akhi abdullah
from graphics import *

#def draw_cir(Cx, Cy, size, color, bullWin):
#    circle = circle(point(Cx,Cy),point(Cx, Cy))
#    circle.setFill(color)
#    circle.draw(bullWin)

cirSz=50
cirCol = "red"

bullWin = GraphWin("BullsEye",cirSz*10, cirSz*10)
bullWin.setCoords(0,0,900, 900)


rCircle = Circle(Point(450,450), 25.5)
rCircle.setFill(color_rgb(230,10,10))
rCircle.draw(bullWin)









bullWin.getMouse()
bullWin.close()
