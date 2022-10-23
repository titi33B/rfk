from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):

    def __init__(self):
        super().__init__()
        #self._message = ""
        self.shape = ""

    def get_shape(self): 
        return self.shape

    def give_shape(self, shape):
        self.shape = shape
    #def set_message(self, message):
        #self._message = message

    #def get_message(self):
        #return self._mesz
