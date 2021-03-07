import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 측정이 이루어진 경우 1로 설정
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    count = 0

    for b in range(1, n + 1):
        # 양쪽 모두 연결이 되지 않았을 경우 카운트
        if graph[a][b] == INF and graph[b][a] == INF:
            count += 1

    print(count)
    