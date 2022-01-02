from tttgrid import Grid
from tttgame import Game

print("\nWelcome to TicTacToe!\n")
p1 = input("Player 1 enter your name: ")
p2 = input("Player 2 enter your name: ")
print(f"\n{p1} will be 'X'")
print(f"{p2} will be 'O'\n")

g = Grid()

start_game = Game(g)

moves_made = 0

start_game.gamegrid.show_grid()

state = True
state2 = True
state3 = True
play_again = True
p1_score = 0
p2_score = 0
games_played = 0
p1_first = True

while play_again:
    state = True
    state2 = True
    state3 = True
    start_game.gamegrid.reset_grid()
    if games_played > 0:
        print(f"\n{p1} has {p1_score} win(s)!")
        print(f"{p2} has {p2_score} win(s)!\n")
        print("New game has started!\n")
        start_game.gamegrid.show_grid()

    while not p1_first:
        while state2:
            p2_move = input(f"\n{p2}, please place an 'X' by entering in a number on the grid: ")
            if start_game.make_move(p2_move, "X"):
                moves_made = moves_made + 1
                start_game.gamegrid.show_grid()
                if start_game.game_over():
                    print(f"\n{p2} has won!")
                    state = False
                    state2 = False
                    state3 = False
                    p2_score = p2_score + 1
                    games_played = games_played + 1
                    p1_first = True
                    moves_made = 0
                elif (start_game.game_over() == False) and moves_made == 9:
                    print("\nTie!")
                    state = False
                    state2 = False
                    state3 = False
                    games_played = games_played + 1
                    p1_first = True
                    moves_made = 0
                break
        while state3:
            p1_move = input(f"\n{p1}, please place an 'O' by entering in a number on the grid: ")
            if start_game.make_move(p1_move, "O"):
                moves_made = moves_made + 1
                start_game.gamegrid.show_grid()
                if start_game.game_over():
                    print(f"\n{p1} has won!")
                    state = False
                    state2 = False
                    state3 = False
                    p1_score = p1_score + 1
                    games_played = games_played + 1
                    p1_first = True
                    moves_made = 0
                elif (start_game.game_over() == False) and moves_made == 9:
                    print("\nTie!")
                    state = False
                    state2 = False
                    state3 = False
                    games_played = games_played + 1
                    p1_first = True
                    moves_made = 0
                break

    while state and p1_first:
        while state2:
            p1_move = input(f"\n{p1}, please place an 'X' by entering in a number on the grid: ")
            if start_game.make_move(p1_move, "X"):
                moves_made = moves_made + 1
                start_game.gamegrid.show_grid()
                if start_game.game_over():
                    print(f"\n{p1} has won!")
                    state = False
                    state2 = False
                    state3 = False
                    p1_score = p1_score + 1
                    games_played = games_played + 1
                    p1_first = False
                    moves_made = 0
                elif (start_game.game_over() == False) and moves_made == 9:
                    print("\nTie!")
                    state = False
                    state2 = False
                    state3 = False
                    games_played = games_played + 1
                    p1_first = False
                    moves_made = 0
                break
        while state3:
            p2_move = input(f"\n{p2}, please place an 'O' by entering in a number on the grid: ")
            if start_game.make_move(p2_move, "O"):
                moves_made = moves_made + 1
                start_game.gamegrid.show_grid()
                if start_game.game_over():
                    print(f"\n{p2} has won!")
                    state = False
                    state2 = False
                    state3 = False
                    p2_score = p2_score + 1
                    games_played = games_played + 1
                    p1_first = False
                    moves_made = 0
                elif (start_game.game_over() == False) and moves_made == 9:
                    print("\nTie!")
                    state = False
                    state2 = False
                    state3 = False
                    games_played = games_played + 1
                    p1_first = False
                    moves_made = 0
                break
