import math


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

positions = []
for _ in range(n):
    x, y = map(int, input().split())
    positions.append([x, y])

edges = []
for i in range(len(positions) - 1):
    for j in range(i + 1, len(positions)):
        cost = math.sqrt((positions[i][0] - positions[j][0])**2 + (positions[i][1] - positions[j][1])**2)
        edges.append((cost, i + 1, j + 1))

edges.sort()

for _ in range(m):
    x, y = map(int, input().split())
    union_parent(x, y)

result = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print('%0.2f' % result)
