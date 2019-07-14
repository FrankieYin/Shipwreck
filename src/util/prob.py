from util.ship import *
import numpy as np

_ = 0
X = 1
O = -2

board = [[_, _, _, _, _, _, _, _, _, _, _, _],
         [_, _, _, _, _, _, _, _, _, _, _, _],
         [_, _, _, _, O, O, _, _, _, _, _, _],
         [_, O, O, _, O, O, _, _, _, _, _, _],
         [_, O, O, _, _, _, _, O, O, _, _, _],
         [_, _, _, _, _, _, _, O, O, _, _, _],
         [_, _, _, _, _, _, _, _, _, _, _, _],
         [_, _, _, _, _, _, _, _, _, _, _, _],
         [_, _, _, _, _, _, _, _, O, O, _, _],
         [_, _, _, _, _, _, _, _, O, O, _, _],
         [_, _, _, _, _, _, _, _, _, _, _, _],
         [_, _, _, _, _, _, _, _, _, _, _, _]]

# for every ship in the 5 ship types
# check the possible ways of placing the ship in the board
# and record the number of times that a cell contains a ship

# for ship_type in ship_types:
#     for orientation in ship_orientations:
#         ship = Ship(ship_type, orientation)

speedboat = np.array([[X, X],
                      [X, _]]) # 2x2

jetboat = np.array([[X],
                    [X]]) # 2x1

battleship = np.array([[X],
                       [X],
                       [X],
                       [X]]) # 4x1

oilrig = np.array([[X, _, _, X],
                   [X, X, X, X],
                   [X, _, _, X]]) # 3x4

platform = np.array([[_, X],
                     [X, X],
                     [X, X],
                     [_, X]]) # 2x4

ships = [speedboat, jetboat, battleship, oilrig, platform]
entropy = np.array(board)

for ship in ships:
    r_len, c_len = ship.shape
    for r in range(13 - r_len):
        for c in range(13 - c_len):
            if -1 not in (entropy[r:r+r_len, c:c+c_len] + ship):
                # then ship is not overlapping with any islands
                entropy[r:r+r_len, c:c+c_len] += ship

print(entropy)