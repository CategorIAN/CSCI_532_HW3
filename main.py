from RandomFlowNetwork import RandomFlowNetwork
from ResidualNetwork import ResidualNetwork
from ResPath import ResPath
import pandas as pd

def analysis(first, last, step):
    def f(i):
        print("----------------------------------------------------------------------------------------")
        print("Size is {}".format(i))
        G = RandomFlowNetwork(i)
        print("DFS")
        DFS = G.appendtime(G.fordFulkerson)(False, True)
        print("BFS")
        BFS = G.appendtime(G.fordFulkerson)(True, True)
        print("##########")
        print(DFS[1:] + BFS[1:])
        return DFS[1:] + BFS[1:]
    df = pd.DataFrame(index = range(first, last + 1, step), columns = ['DFS_Count', 'DFS_Time', 'BFS_Count', 'BFS_Time'])
    for i in df.index:
        df.loc[i, :] = f(i)
    df.to_csv("Analysis_from_{}_to_{}.csv".format(first, last))




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
    if i == 4:
        G = RandomFlowNetwork(100)
        f = G.initFlow()
        R = ResidualNetwork(G, f)
        resPath = R.augmentingPathBFS()
        R.augmentFlow(resPath)
        G.fordFulkerson()


if __name__ == '__main__':
    analysis(10, 100, 10)

