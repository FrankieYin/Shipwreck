from colorama import init, Fore, Style

class TestServer:

    def __init__(self, player):
        init()
        _ = self.empty = 0
        X = self.occupied = 1
        O = self.islands = 2
        self.hit = 4

        self.player = player
        self.board = [[_, _, _, _, _, _, _, _, _, _, _, _],
                      [_, _, _, _, _, _, _, X, X, _, _, _],
                      [_, X, _, _, O, _, X, X, X, X, _, _],
                      [X, X, O, _, _, _, _, _, _, _, _, _],
                      [X, X, O, _, _, _, _, O, _, _, _, _],
                      [_, X, _, _, _, _, O, O, O, _, _, _],
                      [_, _, _, _, X, _, _, _, _, _, _, _],
                      [_, _, _, _, X, X, _, _, _, _, _, _],
                      [_, _, _, X, O, _, X, _, O, _, _, _],
                      [_, _, _, X, X, X, X, _, O, _, _, _],
                      [_, _, _, X, _, _, X, _, _, _, _, _],
                      [_, _, _, _, _, _, _, _, _, _, _, _]]

        self.game =  [[_, _, _, _, _, _, _, _, _, _, _, _],
                      [_, _, _, _, _, _, _, _, _, _, _, _],
                      [_, _, _, _, O, _, _, _, _, _, _, _],
                      [_, _, O, _, _, _, _, _, _, _, _, _],
                      [_, _, O, _, _, _, _, O, _, _, _, _],
                      [_, _, _, _, _, _, O, O, O, _, _, _],
                      [_, _, _, _, _, _, _, _, _, _, _, _],
                      [_, _, _, _, _, _, _, _, _, _, _, _],
                      [_, _, _, _, O, _, _, _, O, _, _, _],
                      [_, _, _, _, _, _, _, _, O, _, _, _],
                      [_, _, _, _, _, _, _, _, _, _, _, _],
                      [_, _, _, _, _, _, _, _, _, _, _, _]]

    def start(self):
        print("Starting a mock game...")
        print("initialised game board:")
        self.__display(self.board)

        count = 1
        print("Press return to fire.")
        c = input()
        while c != "q":
            print("Round {}:".format(count), end=" ")
            self.fire(self.player.getMove())
            self.__display(self.game)
            count += 1
            c = input()

    def fire(self, coords):
        x = coords[0]
        y = coords[1]
        assert 0 <= x < 12
        assert 0 <= y < 12

        if self.board[x][y] == self.empty:
            print(Fore.MAGENTA + "Miss" + Style.RESET_ALL)
            self.game[x][y] = self.occupied
        elif self.board[x][y] == self.occupied:
            print(Fore.GREEN + "Hit" + Style.RESET_ALL)
            self.game[x][y] = self.hit
        elif self.board[x][y] == self.islands:
            print(Fore.RED + "Island" + Style.RESET_ALL)


    def __display(self, board):
        print("  1 2 3 4 5 6 7 8 9 A B C")
        for i in range(12):
            self.__display_row(i, board[i])
        print()

    def __display_row(self, i, row):
        print(self.__to_str(i + 1), end=" ")
        for cell in row:
            if cell == self.empty:
                print("_", end=" ")
            elif cell == self.occupied:
                print("X", end=" ")
            elif cell == self.islands:
                print("O", end=" ")
            elif cell == self.hit:
                print(Fore.GREEN + "X" + Style.RESET_ALL, end=" ")
            else:
                print("unexpected cell: {}".format(cell))
                exit(-1)

        print()

    def __to_str(self, i):
        if i == 10:
            return "A"
        elif i == 11:
            return "B"
        elif i == 12:
            return "C"
        else:
            return i
