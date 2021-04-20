from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 섬마다 라벨링해주는 작업
def labeling(x, y, label):
    queue = deque()
    queue.append((x, y))
    label_graph[x][y] = label

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and label_graph[nx][ny] == 0:
                    label_graph[nx][ny] = label
                    queue.append((nx, ny))


# 각각의 섬 크기를 늘려가며 다른 섬에 도달할 때까지의 거리 계산
def bfs(label):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and label_graph[nx][ny] != label:
                    return count_graph[x][y] - 1

                if graph[nx][ny] == 0 and count_graph[nx][ny] == 0:
                    count_graph[nx][ny] = count_graph[x][y] + 1
                    queue.append((nx, ny))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
label_graph = [[0] * n for _ in range(n)]
label_number = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and label_graph[i][j] == 0:
            labeling(i, j, label_number)
            label_number += 1

result = int(1e9)
for l in range(1, label_number):
    queue = deque()
    count_graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and label_graph[i][j] == l:
                queue.append((i, j))
                count_graph[i][j] = 1

    result = min(result, bfs(l))

print(result)
