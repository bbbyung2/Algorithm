def solution(number, k):
    stack = [number[0]]

    for digit in number[1:]:
        while len(stack) > 0 and stack[-1] < digit and k > 0:
            k -= 1
            stack.pop()

        stack.append(digit)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)
