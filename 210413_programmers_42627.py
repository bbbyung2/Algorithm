import heapq


def solution(jobs):
    answer, now, count = 0, 0, 0
    start = -1
    q = []

    while count < len(jobs):
        for i in jobs:
            if start < i[0] <= now:
                heapq.heappush(q, (i[1], i[0]))

        if len(q) > 0:
            total_time, requested_time = heapq.heappop(q)
            start = now
            now += total_time
            answer += now - requested_time
            count += 1
        else:
            now += 1

    return answer // len(jobs)
