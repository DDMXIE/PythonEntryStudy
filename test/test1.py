import numpy as np
import pandas as pd

if __name__ == '__main__':
    N = 3
    graph = np.matrix([[0]*N]*N)
    # print(graph)
    # graph[2][1] = 1
    # print(graph)
    df_graph = pd.DataFrame(graph)
    df_graph[0][1] = 1
    print(df_graph)