class Item:
    def consume(self):
        pass


class Consumable:
    def consume(self):
        super.consume()
        del self


class Tool:
    pass
