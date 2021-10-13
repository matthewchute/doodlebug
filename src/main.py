from assets.insects import ant, doodle
from assets.world import world
import random as r 

def checkIfStarve(row, col):
    if w.data[row][col].getType() == " D ":
        w.data[row][col].incrementStarveCounter()

def moveObj(row_new, col_new, row_old, col_old):
    w.data[row_new][col_new] = w.data[row_old][col_old]
    w.data[row_new][col_new].move()
    w.data[row_new][col_new].incrementBreedCounter()
    checkIfStarve(row_new, col_new)
    w.data[row_old][col_old] = " . " 
    breed(row_new, col_new)
    return False

def restObj(row, col):
    w.data[row][col].move()
    w.data[row][col].incrementBreedCounter()
    checkIfStarve(row, col)
    breed(row, col)

def moveAnt(row, col):
    resting = True
    # 1=right, 2=down, 3=left, 4=up
    whichWay = r.randint(1,4)
    if whichWay == 1:
        if col < w.size - 1 and w.data[row][col+1] == " . ":
            resting = moveObj(row, col+1, row, col)
    elif whichWay == 2:
        if row < w.size - 1 and w.data[row+1][col] == " . ":
            resting = moveObj(row+1, col, row, col)
    elif whichWay == 3:
        if col > 0 and w.data[row][col-1] == " . ":
            resting = moveObj(row, col-1, row, col)
    elif whichWay == 4:
        if row > 0 and w.data[row-1][col] == " . ":
            resting = moveObj(row-1, col, row, col)
    if resting:
        restObj(row, col)

def moveDoodle(row, col):
    if w.data[row][col].shouldStarve():
        w.removeDoodle()
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
        w.addAnt()
        return ant(moved = True)
    else:
        w.addDoodle()
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
    w.spawn()
    w.printWorld(stepCounter)
    while True:
        _ = raw_input()
        stepCounter += 1
        nextStep(stepCounter)

