expression = input()
stack = []
result = ''

for char in expression:
    if char.isalpha():
        result += char

    else:
        if char == '(':
            stack.append(char)
        elif char == '+' or char == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)
        elif char == '*' or char == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)
