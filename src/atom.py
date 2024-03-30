import numpy as np


class Atom:
    def __init__(self, a: float = 0, b: float = 0, c: float = 0, d: float = 0):
        self.position = [a, b, c]
        self.load = d

    def __eq__(self, other):
        return other.position == self.position and other.load == self.load

    def __hash__(self):
        return hash(self.position[0] + self.position[1] + self.position[2])

    def operate(self, rotation):
        new_position = np.dot(self.position, rotation)
        new_load = np.dot(self.load, rotation)
        return Atom(new_position[0], new_position[1], new_position[2], new_load)

