from collections import deque

input_line = deque(input())
i = 0
while len(input_line):
    parentheses_mismatch = False
    if len(input_line) % 2 == 1 or len(input_line) == 0:
        parentheses_mismatch = True
        print('NO')
        break
    if ord(input_line[0]) == 40:
        if ord(input_line[-1]) == 41:
            input_line.popleft()
            input_line.pop()
        elif ord(input_line[1]) == 41:
            input_line.popleft()
            input_line.popleft()
        else:
            parentheses_mismatch = True
    elif ord(input_line[0]) == 91:
        if ord(input_line[-1]) == 93:
            input_line.popleft()
            input_line.pop()
        elif ord(input_line[1]) == 93:
            input_line.popleft()
            input_line.popleft()
        else:
            parentheses_mismatch = True
    elif ord(input_line[0]) == 123:
        if ord(input_line[-1]) == 125:
            input_line.popleft()
            input_line.pop()
        elif ord(input_line[1]) == 125:
            input_line.popleft()
            input_line.popleft()
        else:
            parentheses_mismatch = True
    if parentheses_mismatch:
        print('NO')
        break
if len(input_line) == 0:
    print('YES')
#judge: 75/100 : time limit


