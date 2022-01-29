class environment:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.objects = [] #liste des objets présents dans l'environnement

    def addObject(self, obj):
        self.objects.append(obj)

    def removeObject(self, obj):
        self.objects.remove(obj)
