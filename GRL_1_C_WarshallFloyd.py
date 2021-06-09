import sys
import io
import input_file
input = io.StringIO(input_file._INPUT1).readline

V, E = map(int, input().split())

# ワーシャルフロイド法をするための2次元データの準備
d = [[float("inf")] * V for _ in range(V)]
for i in range(V):
    d[i][i] = 0
for _ in range(E):
    s, t, w = map(int, input().split())
    d[s][t] = w

# warshall_floyd
for k in range(V):
    for i in range(V):
        for j in range(V):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

# 負の経路があれば、d[i][i]が負の値になる
for i in range(V):
    if d[i][i] < 0:
        print('NEGATIVE CYCLE')
        exit()

# infをINFにする
for di in d:
    print(*['INF' if num == float("inf") else num for num in di])
