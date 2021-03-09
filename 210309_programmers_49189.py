import heapq


def solution(n, edge):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for next_node, next_cost in graph[now]:
                cost = dist + next_cost

                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))

    dijkstra(1)

    max_distance = max(distance[1:])

    for index in range(1, len(distance)):
        if distance[index] == max_distance:
            answer += 1

    return answer
