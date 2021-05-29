# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random

import game
from game import GameState, Player

c = math.sqrt(2)


class Node:
    children: list
    wins: (int, int, int)
    simuls: int
    parent = None
    activePlayer: GameState.PLAYER_ORDER
    state: GameState

    def __init__(self, state=GameState()):
        wins = {0, 0, 0}
        simuls = 0
        game.state = state

    def is_leaf(self) -> bool:
        return self.children.len == 0

    def add_win(self, winner):
        if winner == Player.BLACK:
            self.wins[0] += 1
        if winner == Player.WHITE:
            self.wins[1] += 1
        if winner == Player.RED:
            self.wins[2] += 1
        self.simuls += 1

    def add_child(self, state=GameState()):
        node = Node(state)
        node.parent = self
        self.children.append(node)

    def calc_usb(self) -> float:
        return self.wins / self.simuls + c * math.sqrt(math.log(self.parent.simuls) / self.simuls)

    def simulate(self) -> Player:
        return random.choice(Player)
        # returns winner_id (TODO)


def choose_node(node) -> Node:
    if node.is_leaf():
        return node
    max_node = None
    for nod in node.children:
        if node.is_leaf():
            return nod
        if max_node is None or nod.calc_usb() > max_node.calc_usb():
            max_node = nod
    return choose_node(max_node)


def make_turn(root, n):  # n - number of simulations
    parent = choose_node(root)
    parent.add_child()
    child = parent.children[0]
    for ind in (0, n):
        winner_id = child.simulate()
    p = child
    while p is not None:
        p.add_win(winner_id)
        p = p.parent
    pass


def main():
    root = Node()
    print('Hello')
    for i in (0, 1000):
        make_turn(root, 10)
    print(root.wins)
