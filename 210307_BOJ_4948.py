import math

n = int(input())

while n != 0:
    array = [True for _ in range(2 * n + 1)]

    for i in range(2, int(math.sqrt(2 * n)) + 1):
        if array[i]:
            j = 2
            while i * j <= 2 * n:
                array[i * j] = False
                j += 1

    count = 0

    for i in range(n + 1, 2 * n + 1):
        if array[i]:
            count += 1

    print(count)

    n = int(input())
