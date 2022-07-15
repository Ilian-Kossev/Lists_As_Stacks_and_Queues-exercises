from collections import deque

input_line = input().split(';')
starting_time = input()
command = input()
assembly_line = deque()
capacity_line = []
robots_line = []
counter = 0
for el in input_line:
    robot_name, process_time = el.split('-')
    robots_line.append(robot_name)
    capacity_line.append(int(process_time))
copy_of_capacity_line = [x * 0 for x in capacity_line]
index = 0
while not command == 'End':
    counter += 1
    subject = command
    for num in range(len(copy_of_capacity_line)):
        copy_of_capacity_line[num] += 1
        if copy_of_capacity_line[num] == capacity_line[num]:
            index = num
            print(f'{robots_line[index]} - {subject} {counter}')
            copy_of_capacity_line[num] = 0
    command = input()








