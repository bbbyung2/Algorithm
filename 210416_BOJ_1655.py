import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []

for _ in range(n):
    number = int(input())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-number, number))
    else:
        heapq.heappush(min_heap, (number, number))

    if len(max_heap) >= 1 and len(min_heap) >= 1 and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(min_heap, (max_value, max_value))
        heapq.heappush(max_heap, (-min_value, min_value))

    print(max_heap[0][1])
