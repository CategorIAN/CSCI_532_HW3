

class FlowNetwork:
    def __init__(self, capacity):
        self.c = capacity

    def __str__(self):
        return "Network" + str(self.c)

    def initFlow(self):
        return dict(map(lambda e: (e, 0), self.c.keys()))

