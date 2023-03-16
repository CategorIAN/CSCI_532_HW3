from itertools import product
from functools import reduce

class PathSet:
    def __init__(self, paths):
        condition = lambda p: p is not None and p.res != 0
        self.paths = self.filter(condition, paths)

    def __str__(self):
        combine = lambda p1, p2: str(p1) + "," + str(p2)
        return "PathSet{" + reduce(combine, self.paths) + "}"

    def __iter__(self):
        return iter(self.paths)

    def __mult__(self, other):
        return PathSet(set(map(lambda paths: paths[0] * paths[1], product(self.paths, other.paths))))

    def __add__(self, other):
        return PathSet(self.paths.union(other.paths))

    def filter(self, condition, paths = None):
        paths = self.paths if paths is None else paths
        paths_filtered = [{p} if condition(p) else set() for p in paths]
        return reduce(lambda s1, s2: s1.union(s2), paths_filtered)

