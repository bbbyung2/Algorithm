from collections import deque


def topology_sort():
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = times[i - 1]

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + times[i - 1], dp[i])

            if indegree[i] == 0:
                q.append(i)


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    topology_sort()

    w = int(input())
    print(dp[w])
