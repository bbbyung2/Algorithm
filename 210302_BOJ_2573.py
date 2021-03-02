from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 빙산 주변 바다의 개수 세기
def count_ocean(x, y):
    count = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and temp_graph[nx][ny] == 0:
            count += 1

    return count


# BFS로 빙산 덩어리 개수 세기
def count_iceberg(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 1

while True:
    visited = [[False] * m for _ in range(n)]
    piece = 0

    # 빙산이 다 녹을 때까지 분리되지 않은 경우
    flag = True
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                flag = False

    if flag:
        print(0)
        break

    # 빙산이 녹은 이후로 업데이트
    temp_graph = deepcopy(graph)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if temp_graph[i][j] != 0:
                graph[i][j] = max(0, graph[i][j] - count_ocean(i, j))

    # 빙산 덩어리 개수 세기
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if not visited[i][j] and graph[i][j] != 0:
                count_iceberg(i, j)
                piece += 1

    if piece >= 2:
        print(answer)
        break

    answer += 1
