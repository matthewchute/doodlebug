class insect:
    def __init__(self):
        self.type = None 
        self.moved = False
        self.breedCounter = 0
    
    def getType(self):
        return self.type
    
    def didMove(self):
        return self.moved 

    def move(self):
        self.moved = True

    def resetMoved(self):
        self.moved = False

    def incrementBreedCounter(self):
        self.breedCounter += 1

    def resetBreedCounter(self):
        self.breedCounter = 0

class ant(insect):
    def __init__(self, moved = False):
        self.type = " A "
        self.moved = moved
        self.breedCounter = 0

    def shouldBreed(self):
        return self.breedCounter == 3

class doodle(insect):
    def __init__(self, moved = False):
        self.type = " D "
        self.moved = moved
        self.breedCounter = 0
        self.starveCounter = 0

    def shouldBreed(self):
        return self.breedCounter == 8

    def shouldStarve(self):
        return self.starveCounter == 3

    def incrementStarveCounter(self):
        self.starveCounter += 1

    def resetStarveCounter(self):
        self.starveCounter = 0
        