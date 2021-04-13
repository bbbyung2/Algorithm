import heapq


def solution(scoville, K):
    answer = 0

    q = []
    for food in scoville:
        heapq.heappush(q, food)

    while True:
        if q[0] >= K:
            break
        if q[0] < K and len(q) == 1:
            return -1

        first_food = heapq.heappop(q)
        second_food = heapq.heappop(q)
        mixed_food = first_food + 2 * second_food
        heapq.heappush(q, mixed_food)
        answer += 1

    return answer
