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


while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    parent = [i for i in range(m + 1)]
    edges = []
    total_cost = 0

    for _ in range(n):
        x, y, cost = map(int, input().split())
        edges.append((cost, x, y))
        # 모든 경로의 거리 합산
        total_cost += cost

    edges.sort()

    for edge in edges:
        cost, x, y = edge
        if find_parent(x) != find_parent(y):
            union_parent(x, y)
            # 경로로 선택되면 total_cost에서 제외
            total_cost -= cost

    print(total_cost)
