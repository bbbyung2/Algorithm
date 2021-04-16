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


g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]

parent = {i: i for i in range(g + 1)}
result = 0

for plane in planes:
    p = find_parent(plane)

    # 도킹할 자리가 없는 경우
    if p == 0:
        break

    union_parent(p, p - 1)
    result += 1

print(result)
