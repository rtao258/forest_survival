from settings import SETTINGS


class Entity:
    def __init__(self, name, health):
        # Get name
        self.name = self.name_validate(name)
        # Get health (tuple)
        self._max_health = health
        self._health = self._max_health

    @staticmethod
    def name_validate(name):
        if not(name is None):
            max_length = SETTINGS["NAME"]["MAX_LENGTH"]
            if len(name) <= max_length:
                return name
            else:
                return name[:max_length]
                # print("[DEBUG] Entity name was over {} characters and was truncated to {}".format(max_length, self.name))
        else:
            # TODO: Not working currently - maybe enter key not(is None)?
            return SETTINGS["NAME"]["DEFAULT"]

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new):
        if new < 0:
            # TODO: Do something when entity dies
            # print("[DEBUG] Entity {} died".format(self._name))
            pass
        elif new > self._max_health:
            # print("[DEBUG] The new health, {}, is greater than the max health, {}".format(new, self._max_health))
            self._health = self._max_health
            # print("[DEBUG] Health has been set to the max health, " + str(self._max_health))
        else:
            self._health = new

        return self._health

    def introduce(self):
        print("A new entity hath been born unto this world.")
        print("It is {}!".format(self.name, self.name))
        print("{} has {} health.".format(self.name, self.health))
        print()
