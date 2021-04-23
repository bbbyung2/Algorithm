from collections import deque
import sys

input = sys.stdin.readline


def bfs(root):
    queue = deque()
    visited = [0] * (n + 1)
    queue.append((root, 0))
    visited[root] = 1
    result = [0, 0]

    while queue:
        now, weight = queue.popleft()

        for next_weight, next_node in tree[now]:
            if not visited[next_node]:
                new_weight = weight + next_weight
                visited[next_node] = 1
                queue.append((next_node, new_weight))

                if result[1] < new_weight:
                    result = [next_node, new_weight]

    return result


n = int(input())
tree = {i: [] for i in range(n + 1)}

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((weight, child))
    tree[child].append((weight, parent))

print(bfs(bfs(1)[0])[1])
