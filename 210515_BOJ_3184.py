import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    queue = [(x, y)]
    o, v = 0, 0

    while queue:
        x, y = queue.pop()
        if graph[x][y] == 'v':
            v += 1
        elif graph[x][y] == 'o':
            o += 1
        graph[x][y] = '#'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != '#':
                    queue.append((nx, ny))

    if o <= v:
        o = 0
    else:
        v = 0

    return o, v


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
sheep, wolf = 0, 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'v' or graph[i][j] == 'o':
            o, v = bfs(i, j)
            sheep += o
            wolf += v

print(sheep, wolf)
