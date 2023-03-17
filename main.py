from RandomFlowNetwork import RandomFlowNetwork
from ResidualNetwork import ResidualNetwork
from ResPath import ResPath


def f(i):
    if i == 1:
        G = RandomFlowNetwork(5)
        print("G: {}".format(G))
        f = G.initFlow()
        R = ResidualNetwork(G, f)
        print(R.edges)
        print(R.neighbor_edges)
        resPath = R.augmentingPathBFS()
        print(resPath)
        print(R.augmentFlow(resPath))
        print(G.fordFulkerson())
    if i == 2:
        G = RandomFlowNetwork(5)
        print("G: {}".format(G))
        f = G.initFlow()
        R = ResidualNetwork(G, f)
        resPath1 = R.augmentingPathBFS()
        print(resPath1)
        resPath2 = R.augmentingPathDFS()
        print(resPath2)
        print(G.fordFulkerson(DFS = True))
    if i == 4:
        G = RandomFlowNetwork(100)
        f = G.initFlow()
        R = ResidualNetwork(G, f)
        resPath = R.augmentingPathBFS()
        R.augmentFlow(resPath)
        G.fordFulkerson()


if __name__ == '__main__':
    f(2)

