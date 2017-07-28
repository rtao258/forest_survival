from entity import Entity


class Monster(Entity):
    def __init__(self, name, health, damage=float("inf")):
        # Get name
        self._name = name
        # Get health
        self._max_health = health[1]
        self._health = 0; self.health = health[0]
        # Get damage
        self.damage = damage

    def attack(target):
        target.health -= target.damage
