class Game:

    def __init__(self, TTTGrid):
        self.gamegrid = TTTGrid

    def game_over(self):
        if (((self.gamegrid.a == "X") and (self.gamegrid.b == "X") and (self.gamegrid.c == "X")) or
                ((self.gamegrid.a == "O") and (self.gamegrid.b == "O") and (self.gamegrid.c == "O"))):
            return True
        elif (((self.gamegrid.d == "X") and (self.gamegrid.e == "X") and (self.gamegrid.f == "X")) or
              ((self.gamegrid.d == "O") and (self.gamegrid.e == "O") and (self.gamegrid.f == "O"))):
            return True
        elif (((self.gamegrid.g == "X") and (self.gamegrid.h == "X") and (self.gamegrid.i == "X")) or
              ((self.gamegrid.g == "O") and (self.gamegrid.h == "O") and (self.gamegrid.i == "O"))):
            return True
        elif (((self.gamegrid.c == "X") and (self.gamegrid.e == "X") and (self.gamegrid.g == "X")) or
              ((self.gamegrid.c == "O") and (self.gamegrid.e == "O") and (self.gamegrid.g == "O"))):
            return True
        elif (((self.gamegrid.a == "X") and (self.gamegrid.e == "X") and (self.gamegrid.i == "X")) or
              ((self.gamegrid.a == "O") and (self.gamegrid.e == "O") and (self.gamegrid.i == "O"))):
            return True
        elif (((self.gamegrid.a == "X") and (self.gamegrid.d == "X") and (self.gamegrid.g == "X")) or
              ((self.gamegrid.a == "O") and (self.gamegrid.d == "O") and (self.gamegrid.g == "O"))):
            return True
        elif (((self.gamegrid.b == "X") and (self.gamegrid.e == "X") and (self.gamegrid.h == "X")) or
              ((self.gamegrid.b == "O") and (self.gamegrid.e == "O") and (self.gamegrid.h == "O"))):
            return True
        elif (((self.gamegrid.c == "X") and (self.gamegrid.f == "X") and (self.gamegrid.i == "X")) or
              ((self.gamegrid.c == "O") and (self.gamegrid.f == "O") and (self.gamegrid.i == "O"))):
            return True
        else:
            return False

    def make_move(self, move, x_or_o):

        while True:
            if move == "1" and (self.gamegrid.a == 1):
                self.gamegrid.a = x_or_o
                return True
            elif move == "2" and (self.gamegrid.b == 2):
                self.gamegrid.b = x_or_o
                return True
            elif move == "3" and (self.gamegrid.c == 3):
                self.gamegrid.c = x_or_o
                return True
            elif move == "4" and (self.gamegrid.d == 4):
                self.gamegrid.d = x_or_o
                return True
            elif move == "5" and (self.gamegrid.e == 5):
                self.gamegrid.e = x_or_o
                return True
            elif move == "6" and (self.gamegrid.f == 6):
                self.gamegrid.f = x_or_o
                return True
            elif move == "7" and (self.gamegrid.g == 7):
                self.gamegrid.g = x_or_o
                return True
            elif move == "8" and (self.gamegrid.h == 8):
                self.gamegrid.h = x_or_o
                return True
            elif move == "9" and (self.gamegrid.i == 9):
                self.gamegrid.i = x_or_o
                return True
            else:
                print("\nInvalid Move. Choose another square!")
                self.gamegrid.show_grid()
                return False


