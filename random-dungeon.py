import random
import room_data
import monster_data

loot = []
rooms = []
monsters = []
room_exits = [
    {
        "key": "W",
        "description": "W - West"
    },
    {
        "key": "E",
        "description": "E - East"
    },
    {
        "key": "N",
        "description": "N - North"
    },
    {
        "key": "S",
        "description": "S - South"
    },
    {
        "key": "X",
        "description": "X - Exit"
    }
]
npc = []
inventory = []
score = 0
player_hp = 5
name = ""

def game_loop():

    while True:
        current_room = get_room()
        display_room(current_room)
        current_monster = get_monster()

        if(current_monster != None):
            battle_loop(current_monster)
        if(player_hp <= 0):
            print("You were slain by a", current_monster.name)
            game_over()
            break
        movement_loop()

def movement_loop():
    pass

def battle_loop(monster):
    pass

def loot_loop():
    pass

def display_exits():
    pass

def get_exits():
    rand_int = random.randint(1, len(room_exits))
    rand_sample = random.sample(range(0, len(room_exits)), rand_int)
    rand_exits = []

    for i in range(rand_sample):
        rand_exits[i] = room_exits[rand_sample[i]]

    return rand_exits


def get_room():
    rand_int = random.randint(0, len(rooms))
    return rooms[rand_int]

def get_loot():
    pass

def get_monster():
    pass

def get_npc():
    pass

def display_room(room):
    pass

def game_over():
    pass

def entry():
    rooms = room_data.load()
    monsters = monster_data.load()
    print("Welcome To the Caves of Illusion!")
    name = input("What is your name? ")
    game_loop()

if __name__ == "__main__":
    entry()