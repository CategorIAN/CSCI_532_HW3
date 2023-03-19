from ResPath import ResPath
from PathSet import PathSet
from functools import reduce
from math import pow
from tail_recursive import tail_recursive as tail

class ResidualNetwork:
    def __init__(self, fNetwork, f):
        self.fNetwork = fNetwork
        self.f = f
        res_forward = PathSet(list(map(lambda e: ResPath(e, (0,), fNetwork.c[e] - f[e], fNetwork.sink), fNetwork.c.keys())))
        res_backward = PathSet(list(map(lambda e: ResPath(self.direct(e, True), (1,), f[e], fNetwork.sink), fNetwork.c.keys())))
        condition = lambda p: p.res != 0
        combiner = lambda p1, p2: p1 if p1.res >= p2.res else p2
        self.edges = self.groupBy(lambda p: p.path, combiner, self.filter(condition, res_forward + res_backward))
        print("Residual Edges:")
        print(self.edges)
        add_neighbor = lambda d, edge: d|{edge.path[0]: d.get(edge.path[0], PathSet([])) + PathSet([edge])}
        self.neighbor_edges = reduce(add_neighbor, self.edges, dict([(v, PathSet([])) for v in range(fNetwork.n)]))

    def direct(self, edge, flip):
        return (edge[1], edge[0]) if flip else edge

    def filter(self, condition, paths):
        paths_filtered = [[p] if condition(p) else [] for p in paths]
        return reduce(lambda l1, l2: l1 + l2, paths_filtered, [])

    def groupBy(self, key, combiner, paths):
        add_ResPath = lambda d, path: d | {key(path): d.get(key(path), []) + [path]}
        resPathByPath = reduce(add_ResPath, paths, {})
        return [reduce(combiner, resPathList) for resPathList in resPathByPath.values()]

    def neighbor_paths(self, path):
        return PathSet([path]) * self.neighbor_edges[path.tail]

    def branch(self, pathset):
        return reduce(lambda ps1, ps2: ps1 + ps2, list(map(self.neighbor_paths, pathset.paths)))

    def augmentingPathBFS(self):
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

    def augmentingPathDFS(self):
        @tail
        def go(pathlist):
            #print("%%%%%%%%%%")
            #print("Paths: {}".format(pathlist))
            if len(pathlist) == 0:
                return None
            else:
                path = pathlist[0]
                if path.isDone():
                    return path
                else:
                    return go.tail_call(self.neighbor_paths(path).paths + pathlist[1:])
        return go(self.neighbor_edges[self.fNetwork.source].paths)

    def augmentingPathDFS2(self):
        @tail
        def go(startPath, pathlist, traversed):
            #print("%%%%%%%%%%")
            #print("Paths: {}".format(pathlist))
            if startPath.isDone():
                return startPath
            else:
                neighbors = self.neighbor_paths(startPath).paths
                if len(neighbors) == 0:
                    vertex = startPath.tail
                    newTrav = traversed | {vertex: traversed.get(vertex, []) + [frozenset(startPath.traversed)]}
                    pathList_filtered = self.filterOutOld(pathlist, newTrav)
                    if len(pathList_filtered) == 0:
                        return None
                    else:
                        path = pathList_filtered[0]

            if len(pathlist) == 0:
                return None
            else:
                path = pathlist[0]
                if path.isDone():
                    return path
                else:
                    return go.tail_call(self.neighbor_paths(path).paths + pathlist[1:])
        return go(self.neighbor_edges[self.fNetwork.source].paths)

    def augmentingPathDFS3(self):
        @tail
        def go(startPath, nextPaths, pathList, traversed):

            if len(nextPaths) == 0:
                vertex = startPath.tail
                newTrav = traversed|{vertex:traversed.get(vertex, []) + [frozenset(startPath.traversed)]}
                if len(pathList) == 0:
                    return None
                else:
                    pathList_filtered = self.filterOutOld(pathList, newTrav)
                    path = pathList_filtered[0]
                    if path.isDone():
                        return path
                    else:
                        return go.tail_call(path, self.neighbor_paths(path).paths, pathList_filtered[1:], newTrav)
            else:
                pass
        return go(self.neighbor_edges[self.fNetwork.source].paths)

    def filterOutOld(self, pathList, traversed):
        @tail
        def isNew(path, travList):
            return len(travList) == 0 or (not path.traversed.issuperset(travList[0]) and isNew.tail_call(travList[1:]))
        @tail
        def go(paths):
            return None if len(paths) == 0 else paths if isNew(paths[0], traversed[paths[0].tail]) else go.tail_call(paths[1:])
        return go(pathList)

    def augmentFlow(self, resPath, flow = None):
        flow = self.f if flow is None else flow
        if resPath is None:
            return flow
        else:
            signedPath = zip(resPath.path[1:], resPath.sign)
            augment = lambda f, e, s: f|{self.direct(e, bool(s)): f[self.direct(e, bool(s))] + int(pow(-1, s)) * resPath.res}
            augmentThrough = lambda flow_u, v_s: (augment(flow_u[0], (flow_u[1], v_s[0]), v_s[1]), v_s[0])
            return reduce(augmentThrough, signedPath, (flow, 0))[0]




