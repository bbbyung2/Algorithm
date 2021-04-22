import sys

input = sys.stdin.readline

n, d = map(int, input().split())
graph = [[] for _ in range(10001)]
distance = [i for i in range(d + 1)]

for _ in range(n):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])

for now in range(d + 1):
    if now != 0:
        distance[now] = min(distance[now], distance[now - 1] + 1)

    for next_cost, next_node in graph[now]:
        if next_node <= d and distance[next_node] > next_cost + distance[now]:
            distance[next_node] = next_cost + distance[now]

print(distance[d])
