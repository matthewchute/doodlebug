from assets.insects import ant, doodle
from assets.world import world
import random as r 

def spawn():
    antCount = 0
    doodleCount = 0
    while antCount < w.numAnts:
        row = r.randint(0, w.size-1)
        col = r.randint(0, w.size-1)
        if w.data[row][col] == " . ":
            w.data[row][col] = ant()
            antCount += 1
    while doodleCount < w.numDoodle:
        row = r.randint(0, w.size-1)
        col = r.randint(0, w.size-1)
        if w.data[row][col] == " . ":
            w.data[row][col] = doodle()
            doodleCount += 1

def resetMove():
    for row in range(w.size):
        for col in range(w.size):
            if w.data[row][col] != " . ":
                w.data[row][col].rest()

def move():
    for row in range(w.size):
        for col in range(w.size):
            if w.data[row][col] != " . " and w.data[row][col].didMove() == False:
                # 1=right, 2=down, 3=left, 4=up
                whichWay = r.randint(1,4)
                if whichWay == 1:
                    if col < w.size - 1 and w.data[row][col+1] == " . ":
                        w.data[row][col+1] = w.data[row][col]
                        w.data[row][col+1].move()
                        w.data[row][col] = " . " 
                elif whichWay == 2:
                    if row < w.size - 1 and w.data[row+1][col] == " . ":
                        w.data[row+1][col] = w.data[row][col]
                        w.data[row+1][col].move()
                        w.data[row][col] = " . " 
                elif whichWay == 3:
                    if col > 0 and w.data[row][col-1] == " . ":
                        w.data[row][col-1] = w.data[row][col]
                        w.data[row][col-1].move()
                        w.data[row][col] = " . " 
                elif whichWay == 4:
                    if row > 0 and w.data[row-1][col] == " . ":
                        w.data[row-1][col] = w.data[row][col]
                        w.data[row-1][col].move()
                        w.data[row][col] = " . " 
                else:
                    w.data[row][col].move()
    resetMove()

if __name__ == "__main__":
    w = world()
    spawn()
    w.printWorld()
    while True:
        _ = raw_input()
        move()
        print ""
        w.printWorld()

