from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    candidates = []
    for num in range(1, col + 1):
        candidates.extend(combinations(range(col), num))

    # 유일성 검사
    unique = []
    for candidate in candidates:
        temp = [tuple([instance[attr] for attr in candidate]) for instance in relation]

        if len(set(temp)) == row:
            unique.append(candidate)

    # 최소성 검사
    result = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                result.discard(unique[j])

    return len(result)
