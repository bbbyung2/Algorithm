def solution(record):
    answer = []
    info = {}

    for r in record:
        string = r.split(' ')
        if string[0] == 'Enter':
            info[string[1]] = string[2]
            answer.append((0, string[1]))
        elif string[0] == 'Leave':
            answer.append((1, string[1]))
        elif string[0] == 'Change':
            info[string[1]] = string[2]

    result = []

    for inst, uid in answer:
        if inst == 0:
            result.append(f'{info[uid]}님이 들어왔습니다.')
        elif inst == 1:
            result.append(f'{info[uid]}님이 나갔습니다.')

    return result
