"""
Create a class called "Monster" that will keep track 
of the following information:

- Health Points
- Attack Points
- Method to "Fight"

The Monster class should also have a `fight()` 
method which will allow the monster to attack another monster.
"""


class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def fight(self, target):
        target.hp -= self.attack
        print(f"{self.name} attacked {target.name} for {self.attack} damage!")
        print(f"{target.name} has {target.hp} HP left.")


# Test the code
centaur = Monster("Centaur", 100, 10)
goblin = Monster("Goblin", 50, 5)
centaur.fight(goblin)
goblin.fight(centaur)
