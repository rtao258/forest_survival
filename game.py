class Game:

    def __init__(self):
        print("\nGame #" + str(id(self)) + " has begun!")
        self.turn = 0

    def intro(self):
        print("Welcome to FOREST SURVIVAL")
        print("By RAYMOND TAO")
        print("Press [ENTER <--/] to PLAY!")
        input()
        print("\n"*1000)

    def outro(self):
        print("The Game #" + str(id(self)) + " hath ended!")
