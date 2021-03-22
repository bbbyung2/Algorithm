import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e, p = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (v + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, next_dist in graph[now]:
            cost = dist + next_dist

            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance

distance_mj = dijkstra(1)
distance_gw = dijkstra(p)

if distance_mj[v] == distance_mj[p] + distance_gw[v]:
    print('SAVE HIM')
else:
    print('GOOD BYE')
