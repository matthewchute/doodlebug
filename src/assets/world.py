from assets.insects import ant, doodle
import random as r

class world:
    def __init__(self):
        self.size = 10
        self.startingAnts = 1
        self.startingDoodles = 1
        self.numAnts = 0
        self.numDoodle = 0
        self.data = [[" . " for i in range(self.size)] for j in range(self.size)]

    def addAnt(self):
        self.numAnts += 1

    def addDoodle(self):
        self.numDoodle += 1

    def spawn(self):
        while self.numAnts < self.startingAnts:
            row = r.randint(0, self.size-1)
            col = r.randint(0, self.size-1)
            if self.data[row][col] == " . ":
                self.data[row][col] = ant()
                self.addAnt()
        while self.numDoodle < self.startingDoodles:
            row = r.randint(0, self.size-1)
            col = r.randint(0, self.size-1)
            if self.data[row][col] == " . ":
                self.data[row][col] = doodle()
                self.addDoodle()
    
    def printWorld(self, step):
        print "Step Number: " + str(step)
        for i in range(self.size):
            for j in range(self.size):
                print self.data[i][j],
            print ""
    