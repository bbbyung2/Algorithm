t = int(input())
result = [1, 2, 4]

for i in range(3, 10):
    result.append(result[i - 3] + result[i - 2] + result[i - 1])

for _ in range(t):
    n = int(input())
    print(result[n - 1])
    