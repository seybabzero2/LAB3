from abc import ABC, abstractmethod

class Ship(ABC):
    def __init__(self, length, symbol, health=None):
        self.length = length
        self.symbol = symbol
        self.health = health if health is not None else length
        self.coordinates = []

    def place(self, x, y, horizontal):
        self.coordinates = []
        if horizontal:
            for i in range(self.length):
                self.coordinates.append((x + i, y))
        else:
            for i in range(self.length):
                self.coordinates.append((x, y + i))

    @abstractmethod
    def special_ability(self, game, x, y):
        pass

    def hit(self):
        self.health -= 1
        return self.health <= 0

class Destroyer(Ship):
    def __init__(self, symbol):
        super().__init__(2, symbol)
    
    def special_ability(self, game, x, y):
        # Дезстроєр не має спеціальної здібності
        pass

class Submarine(Ship):
    def __init__(self, symbol):
        super().__init__(3, symbol)
    
    def special_ability(self, game, x, y):
        # Підводний човен може зробити додатковий постріл
        print("Submarine special: extra shot!")
        game.fire('A' if self.symbol == 'A' else 'B', x, y)

class AircraftCarrier(Ship):
    def __init__(self, symbol):
        super().__init__(4, symbol)
    
    def special_ability(self, game, x, y):
        # Авіаносець робить постріл по площі 3x3
        print("Aircraft carrier area attack!")
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                game.fire('A' if self.symbol == 'A' else 'B', x + dx, y + dy)