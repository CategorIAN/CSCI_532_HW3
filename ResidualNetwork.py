from ResPath import ResPath
from PathSet import PathSet
from functools import reduce

class ResidualNetwork:
    def __init__(self, fNetwork, f):
        self.fNetwork = fNetwork
        self.f = f
        res_forward = PathSet(list(map(lambda e: ResPath(e, (1,), fNetwork.c[e] - f[e]), fNetwork.c.keys())))
        res_backward = PathSet(list(map(lambda e: ResPath(self.flip(e), (-1,), f[e]), fNetwork.c.keys())))
        self.edges = res_forward + res_backward
        add_neighbor = lambda d, edge: d|{edge.path[0]: d[edge.path[0]] + PathSet([edge])}
        self.neighbor_edges = reduce(add_neighbor, self.edges, dict([(v, PathSet([])) for v in range(fNetwork.n)]))

    def flip(self, edge):
        return (edge[1], edge[0])

    def neighbor_paths(self, path):
        return PathSet([path]) * self.neighbor_edges[path.tail]

    def branch(self, pathset):
        return reduce(lambda ps1, ps2: ps1 + ps2, list(map(self.neighbor_paths, pathset.paths)))




