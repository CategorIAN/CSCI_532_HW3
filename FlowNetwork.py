from ResidualNetwork import ResidualNetwork
from tail_recursive import tail_recursive

class FlowNetwork:
    def __init__(self, n, capacity):
        self.n = n
        self.source = 0
        self.sink = n - 1
        self.intNodes = set(range(1, n - 1))
        self.c = capacity

    def __str__(self):
        return "Network" + str(self.c)

    def initFlow(self):
        return dict(map(lambda e: (e, 0), self.c.keys()))

    def fordFulkerson(self):
        def go(flow):
            resNetwork = ResidualNetwork(self, flow)
            resPath = resNetwork.augmentingPath()
            if resPath is None:
                return flow
            else:
                return go(resNetwork.augmentFlow(resPath, flow))
        return go(self.initFlow())

