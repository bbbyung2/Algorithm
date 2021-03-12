import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 8X8 영역에 x를 둘러 10X10 배열로 변환
board = [['x'] * 10] + [['x'] + list(input().strip()) + ['x'] for _ in range(8)] + [['x'] * 10]
answer = 0

for x in range(1, 9):
    for y in range(1, 9):
        if board[x][y] != '.':
            continue

        total_count = 0

        # 8가지 방향 탐색
        for i in range(8):
            partial_count = 0
            nx = x + dx[i]
            ny = y + dy[i]

            # 흰 돌이 연이어 있으면 계속 같은 방향으로 탐색
            while board[nx][ny] == 'W':
                nx += dx[i]
                ny += dy[i]
                partial_count += 1

            # 연속된 흰 돌 이후에 검은 돌이 오는 경우 총 개수에 합산
            if board[nx][ny] == 'B':
                total_count += partial_count

        answer = max(answer, total_count)

print(answer)
