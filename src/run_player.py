#!/usr/local/bin/python3.6
import argparse
import sys, json
from players.random import RandomPlayer
from util.test_server import TestServer

def process_input(player, input_line):
    parts = input_line.split(" ")
    action = parts[0]

    if action == "move":
        coords = player.getMove()

    else:
        print("unexpected instruction: {}".format(action))


if __name__ == "__main__":
    player = RandomPlayer()

    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    test = parser.parse_args().test


    if test:
        server = TestServer(player)
        server.start()

    else:
        line = sys.stdin.readline()
        while line:
            process_input(player, line.strip())