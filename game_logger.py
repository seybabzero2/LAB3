import logging
from datetime import datetime


class GameLogger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, filename="game_res.log", filemode="w")
        self.logger = logging.getLogger('SeaBattle')
        self.shots_history = []

    def log_shot(self, player, x, y, hit_success, ship_type=None):
        shot_data = {
            'player': player,
            'x': x,
            'y': y,
            'hit': hit_success,
            'ship_type': ship_type,
            'timestamp': datetime.now()
        }
        self.shots_history.append(shot_data)

        if hit_success:
            self.logger.info(f"Player {player} hit at ({x},{y}) - ship {ship_type}")
        else:
            self.logger.info(f"Player {player} missed at ({x},{y})")

    def log_winner(self, winner):
        self.logger.info(f"Player {winner} won the game!")

    def log_error(self, message):
        self.logger.error(f"Error: {message}")

    # Функції пошуку та сортування
    def find_shots_by_player(self, player):
        return [shot for shot in self.shots_history if shot['player'] == player]

    def find_shots_by_result(self, hit_success):
        return [shot for shot in self.shots_history if shot['hit'] == hit_success]

    def sort_shots_by_coordinates(self):
        return sorted(self.shots_history, key=lambda x: (x['x'], x['y']))

    def sort_shots_by_time(self):
        return sorted(self.shots_history, key=lambda x: x['timestamp'])
