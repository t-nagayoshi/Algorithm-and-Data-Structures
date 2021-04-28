# https://mirucacule.hatenablog.com/entry/2020/05/21/124026
from heapq import heappush, heappop
import sys
import io
import input_file
input = io.StringIO(input_file._INPUT2).readline

INF = float('INF')


def dijkstra(s, n):  # (始点, ノード数)
    # ダイクストラ法をするための date の準備
    dist = [INF] * n  # 現在の始点からの距離
    dist[s] = 0  # 最初の始点の初期化
    hq = [(0, s)]  # (distance, node)
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True  # 最小値は確定済みにする
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            # 確定済みでない and 始点からノード v までの距離 + ノード vから 隣接しているノードまでの距離が現在の始点からの距離未満
            if not seen[to] and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                # 距離が更新されたら、そこからまた探索するためにヒープにpushする→最小値からpopして探索する
                heappush(hq, (dist[to], to))
    return dist


# ノード数, エッジ数, 始点ノード
v, e, r = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(v)]
for i in range(e):
    s, t, d = map(int, input().split())
    adj[s].append((t, d))

d = dijkstra(r, v)
for n in d:
    print(n if n != INF else 'INF')
