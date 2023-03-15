from itertools import product


class PathSet:
    def __init__(self, set):
        self.set = set

    def __mult__(self, other):
        return PathSet(set(map(lambda paths: paths[0] * paths[1], product(self.set, other.set))))
