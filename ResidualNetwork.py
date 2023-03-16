from ResPath import ResPath
from PathSet import PathSet

class ResidualNetwork:
    def __init__(self, fNetwork, f):
        res_forward = PathSet(list(map(lambda e: ResPath(e, (1,), fNetwork.c[e] - f[e]), fNetwork.c.keys())))
        res_backward = PathSet(list(map(lambda e: ResPath(self.flip(e), (-1,), f[e]), fNetwork.c.keys())))
        self.edges = res_forward + res_backward

    def flip(self, edge):
        return (edge[1], edge[0])

