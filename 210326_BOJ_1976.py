## 유니온 파인드 알고리즘 풀이

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


n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]
graph = []

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(i + 1, n):
        if row[j]:
            union_parent(i + 1, j + 1)

path = list(map(int, input().split()))
check = True
start = find_parent(path[0])

for i in range(m):
    if find_parent(path[i]) != start:
        check = False
        break

print('YES' if check else 'NO')



## 플로이드 워셜 알고리즘 풀이

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 1
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

path = list(map(int, input().split()))
check = True

for i in range(m - 1):
    if graph[path[i] - 1][path[i + 1] - 1] != 1:
        check = False
        break

print('YES' if check else 'NO')
