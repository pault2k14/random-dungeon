import monster

def load():
    monsters = []

    monsters[0] = monster.Monster(
        'Goblin',
        2,
        2,
        2
    )

    monsters[1] = monster.Monster(
        'Rat',
        1,
        1,
        1
    )

    return monsters

