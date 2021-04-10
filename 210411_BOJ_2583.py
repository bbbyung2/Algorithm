from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    area = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                area += 1
                queue.append((nx, ny))

    if area == 0:
        area += 1

    return area


m, n, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

count = 0
areas = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            areas.append(bfs(i, j))
            count += 1
areas.sort()

print(count)
print(*areas)
