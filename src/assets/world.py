class world:
    def __init__(self):
        self.size = 10
        self.numAnts = 1
        self.numDoodle = 1
        self.data = [[" . " for i in range(self.size)] for j in range(self.size)]
    
    def printWorld(self, step):
        print "Step Number: " + str(step)
        for i in range(self.size):
            for j in range(self.size):
                print self.data[i][j],
            print ""
    