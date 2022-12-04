import room

def load():
    rooms = []

    rooms[0] = room.Room(
        "A bright room."
    )

    rooms[1] = room.Room(
        "A dark room."
    )

    return rooms