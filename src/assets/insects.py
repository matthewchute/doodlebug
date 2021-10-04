class insect:
    def __init__(self):
        self.type = None 
        self.moved = False
    
    def getType(self):
        return self.type

class ant(insect):
    def __init__(self):
        self.type = " A "
        self.moved = False

class doodle(insect):
    def __init__(self):
        self.type = " D "
        self.moved = False
