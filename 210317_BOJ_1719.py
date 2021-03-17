import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = next_cost + dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                # 최단거리일 때마다 result 정보 업데이트
                result[next_node][start] = now


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 경로표 완성을 위해 모든 노드에 대하여 다익스트라 알고리즘 수행
for i in range(1, n + 1):
    dijkstra(i)

# 경로표 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print('-', end=' ')
        else:
            print(result[i][j], end=' ')
    print()
    