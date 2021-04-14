def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a != b:
        parent[b] = a


n, m, k = map(int, input().split())
parent = [i for i in range(n + 1)]
power_plant = list(map(int, input().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

for i in range(len(power_plant) - 1):
    union_parent(power_plant[i], power_plant[i + 1])

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)
