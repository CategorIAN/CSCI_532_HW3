from ResPath import ResPath
from PathSet import PathSet
from functools import reduce

class ResidualNetwork:
    def __init__(self, fNetwork, f):
        self.fNetwork = fNetwork
        self.f = f
        res_forward = PathSet(list(map(lambda e: ResPath(e, (1,), fNetwork.c[e] - f[e], fNetwork.sink), fNetwork.c.keys())))
        res_backward = PathSet(list(map(lambda e: ResPath(self.flip(e), (-1,), f[e], fNetwork.sink), fNetwork.c.keys())))
        self.edges = res_forward + res_backward
        add_neighbor = lambda d, edge: d|{edge.path[0]: d[edge.path[0]] + PathSet([edge])}
        self.neighbor_edges = reduce(add_neighbor, self.edges, dict([(v, PathSet([])) for v in range(fNetwork.n)]))

    def flip(self, edge):
        return (edge[1], edge[0])

    def neighbor_paths(self, path):
        return PathSet([path]) * self.neighbor_edges[path.tail]

    def branch(self, pathset):
        return reduce(lambda ps1, ps2: ps1 + ps2, list(map(self.neighbor_paths, pathset.paths)))

    def augmentingPath(self):
        def go(pathset):
            if len(pathset.paths) == 0:
                return None
            else:
                finished = pathset.finishedPath()
                if finished is not None:
                    return finished
                else:
                    return go(self.branch(pathset))
        return go(self.neighbor_edges[self.fNetwork.source])

    def augmentFlow(self, resPath, flow = None):
        flow = self.f if flow is None else flow
        if resPath is None:
            return flow
        else:
            signedPath = zip(resPath.path[2:], resPath.sign[1:])
            augment = lambda f, e, s: f|{e: f[e] + s * resPath.res}
            augmentThrough = lambda flow_u, v_s: (augment(flow_u[0], (flow_u[1], v_s[0]), v_s[1]), v_s[0])
            return reduce(augmentThrough, signedPath, (augment(flow, resPath.path[0:2], resPath.sign[0]), resPath.path[1]))[0]




