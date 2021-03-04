import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


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

for _ in range(m):
    operation, a, b = map(int, input().split())

    if operation == 0:
        union_parent(a, b)
    elif operation == 1:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
