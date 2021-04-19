from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count_list = [[0] * w for _ in range(l)]
    count_list[x][y] = 1
    max_value = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < w:
                if graph[nx][ny] == 'L' and not count_list[nx][ny]:
                    count_list[nx][ny] = count_list[x][y] + 1
                    max_value = max(max_value, count_list[nx][ny])
                    queue.append((nx, ny))

    return max_value - 1

l, w = map(int, input().split())
graph = [list(input()) for _ in range(l)]

result = 0
for i in range(l):
    for j in range(w):
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
