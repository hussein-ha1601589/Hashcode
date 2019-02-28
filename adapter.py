class Adapter :
    def __init__(self,nparray,id):
        self.arr = nparray
        self.id = id

    def __str__(self):
        return str(self.id)
