class world:
    def __init__(self):
        self.size = 10
        self.numAnts = 1
        self.numDoodle = 1
        self.data = [[" . " for i in range(self.size)] for j in range(self.size)]
    
    def printWorld(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == " . ":
                    print " . ",
                else:
                    print self.data[i][j].getType(),
            print ""
    