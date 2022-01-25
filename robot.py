class robot:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.dir = 90

    def changeDir(self, dir):
        if dir >= 0 and dir <= 360:
            self.dir = dir
        else:
            print("La direction doit être comprise entre 0 et 360 degrés")
            
            
