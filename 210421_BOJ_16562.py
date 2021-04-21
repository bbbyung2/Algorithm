from collections import defaultdict

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


n, m, k = map(int, input().split())
fee_list = list(map(int, input().split()))
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(a, b)

result = 0
visited = set()

for i in range(1, n + 1):
    if i not in visited:
        connection = [i]
        fee = fee_list[i - 1]

        for j in range(1, n + 1):
            if i != j and find_parent(i) == find_parent(j):
                connection.append(j)
                fee = min(fee, fee_list[j - 1])

        visited.update(connection)
        result += fee

if result <= k:
    print(result)
else:
    print('Oh no')
