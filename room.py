

class Room:

    description = None
    exits = None

    def __init__(self, descriptoon):
        self.description = descriptoon

    def display(self):
        print(self.description)