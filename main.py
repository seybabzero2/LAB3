from game_master import MasterClass
from ships import Destroyer, Submarine, AircraftCarrier
import os

def ask_ship(game, player):
    ship_types = ['destroyer', 'submarine', 'carrier']
    ship_names = ['Destroyer (2)', 'Submarine (3)', 'Aircraft Carrier (4)']
    
    for i, (ship_type, ship_name) in enumerate(zip(ship_types, ship_names)):
        print(f"\n{player}, place {ship_name}")
        
        while True:
            try:
                s = input("Enter x y horizontal(1)/vertical(0): ").strip()
                x, y, h = map(int, s.split())
                horizontal = True if h == 1 else False

                if game.place_ship(player, ship_type, x, y, horizontal):
                    print(f"{ship_name} placed successfully!")
                    break
                else:
                    print("Cannot place ship. Try different coordinates.")
            except Exception as e:
                print(f"Invalid input: {e}")

def main():
    game = MasterClass()
    
    # Вибір типів гравців
    print("Select player types:")
    print("1. Human")
    print("2. AI")
    print("3. Cheater")
    
    p1_type = input("Player A type (1/2/3): ").strip()
    p2_type = input("Player B type (1/2/3): ").strip()
    
    type_map = {'1': 'human', '2': 'ai', '3': 'cheater'}
    game.set_players(type_map[p1_type], type_map[p2_type])

    print("\nPlacing ships...")
    ask_ship(game, "A")
    ask_ship(game, "A")
    ask_ship(game, "A")
    
    ask_ship(game, "B")
    ask_ship(game, "B")
    ask_ship(game, "B")

    print("\nStarting game!")

    attacker = "A"

    while not game.winner:
        try:
            s = input(f"Player {attacker} move (x y) or 'save' to save game: ").strip()
            
            if s.lower() == 'save':
                filename = input("Enter filename: ").strip()
                game.save_game(filename)
                print("Game saved!")
                continue
                
            x_move, y_move = list(map(int, s.split()))
            if not (0 <= x_move <= 9 and 0 <= y_move <= 9):
                print("Coordinates must be between 0 and 9")
                continue
        except Exception as e:
            print(f"Error: {e}")
            continue

        os.system('clear')

        game.fight(attacker, x_move, y_move)
        game.print_maps_by_moves(attacker)
        print("\n-------------------------------\n")

        if game.winner:
            print(f"Player {game.winner} wins!")
            break

        attacker = "B" if attacker == "A" else "A"

if __name__ == "__main__":
    main()