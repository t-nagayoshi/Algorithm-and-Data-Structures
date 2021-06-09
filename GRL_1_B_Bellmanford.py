import math
import collections
import sys
import io
import input_file
input = io.StringIO(input_file._INPUT1).readline

INF = float('inf')


def Bellmanford(n, edges, r):  # r: 始点
    d = [INF] * n
    d[r] = 0

    # n巡の更新操作を行う、もし負の経路があれば、n巡目でもまだ更新がされ続ける
    for i in range(n):

        # 各巡（1巡）で全ての辺を見て、最小値であれば、更新を行う
        # アルゴリズム図鑑によれば、更新は各頂点から両方の頂点に対して行う（今回は有向グラフなので片方の更新）
        for (u, v, c) in edges:
            if d[u] != INF and d[u] + c < d[v]:
                d[v] = d[u] + c
                if i == n-1:
                    return ['NEGATIVE CYCLE']

    d = [di if di < INF else 'INF' for di in d]
    return d


V, E, R = map(int, input().split())
Edges = [None] * E

for i in range(E):
    si, ti, di = map(int, input().split())
    Edges[i] = (si, ti, di)

ans = Bellmanford(V, Edges, R)

print(*ans, sep='\n')
