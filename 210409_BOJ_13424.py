import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = next_cost + dist

            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    k = int(input())
    friends = list(map(int, input().split()))

    result = [0] * (n + 1)
    for friend in friends:
        distance = [INF] * (n + 1)
        dijkstra(friend)

        for i in range(1, n + 1):
            result[i] += distance[i]

    min_index = 0
    min_value = INF

    for i in range(1, n + 1):
        if min_value > result[i]:
            min_value = result[i]
            min_index = i

    print(min_index)
