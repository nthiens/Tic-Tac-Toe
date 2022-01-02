class Grid:

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        self.i = 9

    def show_grid(self):
        print(f"[{self.a}][{self.b}][{self.c}]")
        print(f"[{self.d}][{self.e}][{self.f}]")
        print(f"[{self.g}][{self.h}][{self.i}]")

    def reset_grid(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        self.i = 9

