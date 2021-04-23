from collections import deque


def bfs(start):
    queue = deque()
    visited = [False] * (n + 1)
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()

        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                result[next] = result[now] + 1
                queue.append(next)


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
result = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)

if not result[b]:
    print(-1)
else:
    print(result[b])
