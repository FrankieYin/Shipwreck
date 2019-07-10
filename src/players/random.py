import json
import random
from math import *

class RandomPlayer:

    def __init__(self):
        print("init game")

    def getMove(self):
        return random.randint(0, 11), random.randint(0, 11)
