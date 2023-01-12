
class Categories:

    def __init__(self, id, name, image):
        self.id = id
        self.name = name
        self.image = image

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getImage(self):
        return self.image

    def setImage(self, image):
        self.image = image
