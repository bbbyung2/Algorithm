def solution(n, results):
    INF = int(1e9)

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for a, b in results:
        graph[a][b] = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    answer = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] != 0 and graph[i][j] != INF:
                answer[i] += 1
                answer[j] += 1

    return answer.count(n - 1)
