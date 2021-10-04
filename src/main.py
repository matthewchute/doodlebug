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

if __name__ == "__main__":
    w = world()
    spawn()
    w.printWorld()
    
