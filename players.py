from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.ships = []
    
    @abstractmethod
    def shoot_strategy(self, game, x, y):
        pass

class HumanPlayer(Player):
    def shoot_strategy(self, game, x, y):
        # Звичайний постріл
        game.fire(self.name, x, y)

class AIPlayer(Player):
    def shoot_strategy(self, game, x, y):
        # ШІ робить "розумний" постріл
        print(f"AI {self.name} making smart shot")
        game.fire(self.name, x, y)
        # Додатковий постріл з ймовірністю 30%
        import random
        if random.random() < 0.3:
            game.fire(self.name, x + 1, y)

class CheaterPlayer(Player):
    def shoot_strategy(self, game, x, y):
        # Чітер робить постріл по всій лінії
        print(f"Cheater {self.name} shooting line!")
        for i in range(game.map.size):
            game.fire(self.name, i, y)