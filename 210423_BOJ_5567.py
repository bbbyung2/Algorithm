from collections import deque
import sys

input = sys.stdin.readline


def bfs(start):
    queue = deque()
    visited = [0] * (n + 1)
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()

        for next in graph[now]:
            if not visited[next]:
                visited[next] = visited[now] + 1
                queue.append(next)

    return visited[1:]


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
result = [0] * (m + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count_list = bfs(1)
result = 0
for count in count_list:
    if count == 2 or count == 3:
        result += 1

print(result)
