from RandomFlowNetwork import RandomFlowNetwork


def f(i):
    if i == 1:
        F = RandomFlowNetwork(6)
        print(F)
        print("Initial Flow is {}".format(F.initFlow()))

if __name__ == '__main__':
    f(1)

