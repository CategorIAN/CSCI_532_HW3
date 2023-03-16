

class ResPath:
    def __init__(self, path, sign, res):
        self.path = path
        self.sign = sign
        self.res = res
        self.head = self.path[0]
        self.tail = self.path[-1]

    def __str__(self):
        return "Path{{{},{},{}}}".format(self.path, self.sign, self.res)

    def __mult__(self, other):
        if self.tail == other.head and other.tail not in self.path and self.res * other.res > 0:
            path = self.path + other[1:]
            sign = self.sign + other.sign
            res = min(self.res, other.res)
            return ResPath(path, sign, res)




