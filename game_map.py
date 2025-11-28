class Map:
    def __init__(self, size, counterOfShipsA, counterOfShipsB):
        self.size = size
        self.mapA = [['.' for _ in range(size)] for _ in range(size)]
        self.mapB = [['.' for _ in range(size)] for _ in range(size)]
        self.shipsA = []
        self.shipsB = []
        self.counterOfShipsA = counterOfShipsA
        self.counterOfShipsB = counterOfShipsB

    def place_ship(self, player, ship, x, y, horizontal):
        board = self.mapA if player == 'A' else self.mapB
        ships_list = self.shipsA if player == 'A' else self.shipsB

        # Перевірка можливості розміщення
        if horizontal:
            if x + ship.length > self.size:
                return False
            for i in range(ship.length):
                if board[y][x + i] != '.':
                    return False
        else:
            if y + ship.length > self.size:
                return False
            for i in range(ship.length):
                if board[y + i][x] != '.':
                    return False

        # Розміщення корабля
        ship.place(x, y, horizontal)
        ships_list.append(ship)

        if horizontal:
            for i in range(ship.length):
                board[y][x + i] = ship.symbol
        else:
            for i in range(ship.length):
                board[y + i][x] = ship.symbol

        return True

    def winners(self):
        if self.counterOfShipsA == 0:
            return 'B'
        if self.counterOfShipsB == 0:
            return 'A'
        return 0

    def print_maps(self, player):
        print("\nYOUR MAP")
        if player == 'A':
            board_self = self.mapA
            board_enemy = self.mapB
        else:
            board_self = self.mapB
            board_enemy = self.mapA

        for row in board_self:
            print(" ".join(row))

        print("\nENEMY MAP")
        for row in board_enemy:
            masked = []
            for cell in row:
                if cell in ('X', 'Y', 'o'):
                    masked.append(cell)
                else:
                    masked.append('.')
            print(" ".join(masked))
