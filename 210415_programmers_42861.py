def solution(n, costs):
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

    parent = [i for i in range(n + 1)]
    costs.sort(key=lambda x: x[2])
    answer = 0

    for cost in costs:
        a, b, c = cost
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            answer += c

    return answer
