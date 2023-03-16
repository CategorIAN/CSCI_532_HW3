from RandomFlowNetwork import RandomFlowNetwork
from ResidualNetwork import ResidualNetwork
from ResPath import ResPath


def f(i):
    if i == 1:
        F = RandomFlowNetwork(6)
        print(F)
        print("Initial Flow is {}".format(F.initFlow()))
    if i == 2:
        G = RandomFlowNetwork(100)
        print("G: {}".format(G))
        f = G.initFlow()
        R = ResidualNetwork(G, f)
        print(R.edges)
        print(R.neighbor_edges)
        resPath = R.augmentingPath()
        print(resPath)
        print(R.augmentFlow(resPath))
        print(G.fordFulkerson())
    if i == 3:
        p = ResPath((0, 4), (1,), 1, 4)
        q = ResPath((1, 2), (1,), 1, 4)
        print(p * q)


if __name__ == '__main__':
    f(2)

