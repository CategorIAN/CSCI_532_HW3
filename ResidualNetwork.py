from ResPath import ResPath
from PathSet import PathSet

class ResidualNetwork:
    def __init__(self, fNetwork, f):
        res_forward = set(map(lambda e: ResPath(e, (1,), fNetwork.c[e] - f[e]), fNetwork.c.keys()))
        res_backward = set(map(lambda e: ResPath(self.flip(e), (-1,), f[e]), fNetwork.c.keys()))
        self.edges = PathSet(res_forward.union())


    def flip(self, edge):
        return (edge[1], edge[0])

    def filter(self, res, f):
        filtered = [[()] if random.random() < prob else [] for x in xs]
