import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

result = 100000
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += data[end]
        end += 1

    if interval_sum >= s:
        result = min(result, end - start)

    interval_sum -= data[start]

if result == 100000:
    print(0)
else:
    print(result)
