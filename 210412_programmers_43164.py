from collections import defaultdict


def solution(tickets):
    def dfs():
        stack = ['ICN']
        path = []

        while len(stack) > 0:
            recent = stack[-1]

            # 모두 사용한 경우, 출발하는 항공권이 없는 경우
            if len(graph[recent]) == 0 or recent not in graph:
                path.append(stack.pop())
            else:
                stack.append(graph[recent].pop(0))

        return path[::-1]

    graph = defaultdict(list)
    for ticket in tickets:
        departure, arrival = ticket
        graph[departure].append(arrival)

    for airport in graph:
        graph[airport].sort()

    return dfs()
