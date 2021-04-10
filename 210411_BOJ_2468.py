from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, height):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_height = 0
for row in graph:
    max_height = max(max_height, max(row))

result = 1
for height in range(max_height):
# for height in range(max(map(max, graph))):
    visited = [[False] * n for _ in range(n)]
    safe_zone = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and not visited[i][j]:
                safe_zone += 1
                visited[i][j] = True
                bfs(i, j, height)

    result = max(result, safe_zone)

print(result)
