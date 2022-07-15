number = int(input())
stack = []
i = 1
while i <= number:
    command = input()
    if command.startswith('1'):
        number_to_add = int(command.split()[1])
        stack.append(number_to_add)
    elif command.startswith('2'):
        if len(stack) == 0:
            i += 1
            continue
        else:
            stack.pop()
    elif command.startswith('3'):
        print(max(stack))
    elif command.startswith('4'):
        print(min(stack))
    i += 1
stack_str = [str(x) for x in stack]

print(', '.join(stack_str[::-1]))
#judge: 80/100
