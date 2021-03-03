from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

# 방향 그래프의 모든 간선 정보 입력 받기
for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1):
        graph[arr[i]].append(arr[i + 1])
        indegree[arr[i + 1]] += 1


# 위상 정렬 함수
def topology_sort():
    q = deque()
    result = []

    # 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 순서를 정하는 것이 불가능한 경우
    if len(result) != n:
        print(0)
    else:
        for singer in result:
            print(singer)

topology_sort()
