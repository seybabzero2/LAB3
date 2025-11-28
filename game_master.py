from game_map import Map
from game_logger import GameLogger
from ships import Destroyer, Submarine, AircraftCarrier
from players import HumanPlayer, AIPlayer, CheaterPlayer
import pickle

PLAYER_A = 'A'
PLAYER_B = 'B'

PLAYER_MARKER_A = "X"
PLAYER_MARKER_B = "Y"

class MasterClass:
    def __init__(self, winner=0, move=0):
        self.winner = winner
        self.move = move
        self.map = Map(10, 3, 3)  # 3 кораблі на гравця
        self.logger = GameLogger()
        self.players = {}

    def set_players(self, playerA_type, playerB_type):
        player_classes = {
            'human': HumanPlayer,
            'ai': AIPlayer,
            'cheater': CheaterPlayer
        }
        
        self.players['A'] = player_classes[playerA_type]('A')
        self.players['B'] = player_classes[playerB_type]('B')

    def place_ship(self, player, ship_type, x, y, horizontal):
        ship_classes = {
            'destroyer': Destroyer,
            'submarine': Submarine,
            'carrier': AircraftCarrier
        }
        
        ship = ship_classes[ship_type](player)
        return self.map.place_ship(player, ship, x, y, horizontal)

    def fire(self, attacker, x, y):
        if not (0 <= x < self.map.size and 0 <= y < self.map.size):
            return

        target_map = self.map.mapB if attacker == PLAYER_A else self.map.mapA
        target_ships = self.map.shipsB if attacker == PLAYER_A else self.map.shipsA
        hit_marker = PLAYER_MARKER_A if attacker == PLAYER_A else PLAYER_MARKER_B

        if target_map[y][x] not in ('.', 'o', 'X', 'Y'):
            # Влучання в корабель
            ship_symbol = target_map[y][x]
            target_map[y][x] = hit_marker
            
            # Знаходимо корабель і застосовуємо спеціальну здібність
            for ship in target_ships:
                if ship.symbol == ship_symbol:
                    ship.special_ability(self, x, y)
                    if ship.hit():
                        target_ships.remove(ship)
                        if attacker == PLAYER_A:
                            self.map.counterOfShipsB -= 1
                        else:
                            self.map.counterOfShipsA -= 1
                    break
            
            self.logger.log_shot(attacker, x, y, True, ship_symbol)
        else:
            # Промах
            if target_map[y][x] == '.':
                target_map[y][x] = 'o'
            self.logger.log_shot(attacker, x, y, False)

    def fight(self, attacker, x, y):
        player = self.players[attacker]
        player.shoot_strategy(self, x, y)
        winner = self.map.winners()
        if winner:
            self.winner = winner
            self.logger.log_winner(winner)

    def print_maps_by_moves(self, player):
        self.map.print_maps(player)

    def save_game(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    
    @staticmethod
    def load_game(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)