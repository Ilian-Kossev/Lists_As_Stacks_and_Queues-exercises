from collections import deque

green_light = int(input())
free_window = int(input())
queue = deque()
passed_cars = []
usable_seconds = 0
command = input()
cars_crashed = False
while not command == 'END':
    if not command == 'green':
        queue.append(command)
    else:
        green_light_seconds = green_light
        usable_seconds = green_light + free_window
        while green_light_seconds > 0:
            green_light_seconds -= len(queue[0])
            usable_seconds -= len(queue[0])
            if usable_seconds >= 0:
                passed_cars.append(queue.popleft())
            else:
                crash_index = usable_seconds
                print('A crash happened!')
                print(f'{queue[0]} was hit at {queue[0][crash_index]}.')
                cars_crashed = True
                break
            if len(queue) == 0:
                break

    command = input()
if not cars_crashed:
    print('Everyone is safe.')
    print(f"{len(passed_cars)} total cars passed the crossroads.")
#judge: 71/100




