import sys
input = sys.stdin.readline


# 부모 노드 번호
def find_parent(node, k):
    return (node + k - 2) // k


# 최소 공통 조상 찾으며 노드 간의 거리 반환
def lca(a, b):
    count = 0

    while a != b:
        while a > b:
            count += 1
            a = find_parent(a, k)
        while a < b:
            count += 1
            b = find_parent(b, k)

    return count


n, k, q = map(int, input().split())

for _ in range(q):
    x, y = map(int, input().split())

    if k == 1:
        print(abs(x - y))
        continue
    print(lca(x, y))
