from collections import deque


def topology_sort():
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            # 먼저 지어져야 하는 건물 때문에 최댓값 적용
            dp[i] = max(dp[now] + times[i], dp[i])

            if indegree[i] == 0:
                q.append(i)

    print(*dp[1:])


n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
times = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    input_list = list(map(int, input().split()))
    times[i] = input_list[0]
    dp[i] = input_list[0]
    buildings = input_list[1:-1]

    if buildings:
        for building in buildings:
            graph[building].append(i)
            indegree[i] += 1

topology_sort()
