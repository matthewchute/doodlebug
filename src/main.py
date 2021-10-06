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

def moveObj(row_new, col_new, row_old, col_old):
    w.data[row_new][col_new] = w.data[row_old][col_old]
    w.data[row_new][col_new].move()
    w.data[row_new][col_new].incrementBreedCounter()
    w.data[row_old][col_old] = " . " 
    breed(row_new, col_new)

def moveAnt(row, col):
    # 1=right, 2=down, 3=left, 4=up
    whichWay = r.randint(1,4)
    if whichWay == 1:
        if col < w.size - 1 and w.data[row][col+1] == " . ":
            moveObj(row, col+1, row, col)
    elif whichWay == 2:
        if row < w.size - 1 and w.data[row+1][col] == " . ":
            moveObj(row+1, col, row, col)
    elif whichWay == 3:
        if col > 0 and w.data[row][col-1] == " . ":
            moveObj(row, col-1, row, col)
    elif whichWay == 4:
        if row > 0 and w.data[row-1][col] == " . ":
            moveObj(row-1, col, row, col)

def moveDoodle(row, col):
    if w.data[row][col].shouldStarve():
        w.data[row][col] = " . "
    else:
        moveAnt(row,col)

def move(row, col):
    if w.data[row][col] != " . " and not w.data[row][col].didMove():
        if w.data[row][col].getType() == " A ":
            moveAnt(row, col)
        else:
            moveDoodle(row, col)

def breed(row, col):
    if w.data[row][col].shouldBreed() == True:
        w.data[row][col].resetBreedCounter()
        # 1=right, 2=down, 3=left, 4=up
        whichWay = r.randint(1,4)
        if whichWay == 1:
            if col < w.size - 1 and w.data[row][col+1] == " . ":
                w.data[row][col+1] = breedWhich(w.data[row][col])
        elif whichWay == 2:
            if row < w.size - 1 and w.data[row+1][col] == " . ":
                w.data[row+1][col] = breedWhich(w.data[row][col])
        elif whichWay == 3:
            if col > 0 and w.data[row][col-1] == " . ":
                w.data[row][col-1] = breedWhich(w.data[row][col])
        elif whichWay == 4:
            if row > 0 and w.data[row-1][col] == " . ":
                w.data[row-1][col] = breedWhich(w.data[row][col])

def breedWhich(obj):
    if obj.getType() == " A ":
        return ant(moved = True)
    else:
        return doodle(moved = True)
        
def reset():
    for row in range(w.size):
        for col in range(w.size):
            if w.data[row][col] != " . ":
                w.data[row][col].resetMoved()

def nextStep(step):
    for r in range(w.size):
        for c in range(w.size):
            move(r, c)
    reset()
    w.printWorld(step)
            
if __name__ == "__main__":
    stepCounter = 0
    w = world()
    spawn()
    w.printWorld(stepCounter)
    while True:
        _ = raw_input()
        stepCounter += 1
        nextStep(stepCounter)

