#Checkers by JoshGara

from graphics import*

def draw_sq(sX, sY,size, color , win):
    square = Rectangle(Point(sX, sY), Point(sX + size, sY + size ))
    square.setFill(color)
    square.draw(win)

sqSz = 50
sqCol = "red"

chWin = GraphWin("Checkers", sqSz *10 ,sqSz *10)
chWin.setCoords(0, 0, sqSz * 10 , sqSz *10)

for j in range (8):
    for i in range (8):
        if (i + j) % 2 == 0:
            sqCol = "black"
        else:
            sqCol = "red"
        draw_sq(sqSz * (i +1) , sqSz * (j + 1), sqSz, sqCol, chWin)

chWin.getmouse()
chWin.close()
