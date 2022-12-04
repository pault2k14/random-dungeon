

class Monster:

    name = None
    health = None
    armor = None
    attack = None

    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack