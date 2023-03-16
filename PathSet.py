from itertools import product
from functools import reduce

class PathSet:
    def __init__(self, paths):
        condition = lambda p: p is not None and p.res != 0
        self.paths = sorted(self.filter(condition, paths))

    def __str__(self):
        combine = lambda p1, p2: str(p1) + "," + str(p2)
        return "PathSet" + str(self.paths)

    def __repr__(self):
        return "PathSet" + str(self.paths)

    def __hash__(self):
        return self.paths

    def __iter__(self):
        return iter(self.paths)

    def __mul__(self, other):
        if self.isDone():
            return self
        else:
            return PathSet(list(map(lambda paths: paths[0] * paths[1], product(self.paths, other.paths))))

    def __add__(self, other):
        return PathSet(self.paths + other.paths)

    def filter(self, condition, paths = None):
        paths = self.paths if paths is None else paths
        paths_filtered = [[p] if condition(p) else [] for p in paths]
        return reduce(lambda l1, l2: l1 + l2, paths_filtered, [])

    def finishedPath(self):
        go = lambda paths: None if len(paths) == 0 else paths[0] if paths[0].isDone() else go(paths[1:])
        return go(self.paths)

    def isDone(self):
        return len(self.paths) == 0 or reduce(lambda b1, b2: b1 or b2.isDone(), self.paths, False)

