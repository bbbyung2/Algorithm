import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    applicants = [list(map(int, input().split())) for _ in range(n)]
    applicants.sort()

    count = 0
    min_score = applicants[0][1]

    for i in range(1, n):
        if applicants[i][1] > min_score:
            count += 1
        else:
            min_score = applicants[i][1]

    print(n - count)
