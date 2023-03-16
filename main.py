from RandomFlowNetwork import RandomFlowNetwork
from ResidualNetwork import ResidualNetwork


def f(i):
    if i == 1:
        F = RandomFlowNetwork(6)
        print(F)
        print("Initial Flow is {}".format(F.initFlow()))
    if i == 2:
        G = RandomFlowNetwork(6)
        print("G: {}".format(G))
        f = G.initFlow()
        R = ResidualNetwork(G, f)
        print(R.edges)
        for path in R.edges:
            print(path)


if __name__ == '__main__':
    f(2)

