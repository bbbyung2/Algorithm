def solution(people, limit):
    people.sort()
    answer, i, j = 0, 0, len(people) - 1

    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

    return answer
