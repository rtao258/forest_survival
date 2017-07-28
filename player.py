from entity import Entity


class Player(Entity):
    def __init__(self):
        # Inherited from Entity class
        name = input("What is your name? ")
        health = 100
        super().__init__(name, health)
        # Not inherited from Entity class

        # Introduce the player
        self.introduce()

    def introduce(self):
        print("A new player hath been born unto this world.")
        print("It is {}! Hurrah, {}!".format(self.name, self.name))
        print("How will {} survive with only {} health?".format(self.name, self.health))
        print()

    def move(self):
        print("{} moved to a new location.".format(self.name))
