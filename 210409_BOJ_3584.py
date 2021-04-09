t = int(input())
for _ in range(t):
    n = int(input())

    parent = [0] * (n + 1)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a

    x, y = map(int, input().split())

    # x와 y의 루트까지의 경로 구하기
    x_path = [x]
    y_path = [y]

    while parent[x]:
        x_path.append(parent[x])
        x = parent[x]

    while parent[y]:
        y_path.append(parent[y])
        y = parent[y]

    # 루트부터 비교하여 노드가 다를 때까지 반복
    x_depth = len(x_path) - 1
    y_depth = len(y_path) - 1

    while x_path[x_depth] == y_path[y_depth]:
        x_depth -= 1
        y_depth -= 1

    # 노드가 달라지기 직전의 조상 출력
    print(x_path[x_depth + 1])
