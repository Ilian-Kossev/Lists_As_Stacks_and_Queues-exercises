from collections import deque

cups = input().split()
cups_line = deque([int(x) for x in cups])
bottles = input().split()
bottles_line = deque([int(x) for x in bottles])
wasted_water = 0

while True:
    if bottles_line[-1] >= cups_line[0]:
        bottles_line[-1] -= cups_line[0]
        wasted_water += bottles_line.pop()
        cups_line.popleft()
    else:
        cups_line[0] -= bottles_line[-1]
        bottles_line.pop()
    if len(cups_line) == 0 or len(bottles_line) == 0:
        break
if len(cups_line) > 0:
    print('Cups: ', end='')
    for x in cups_line:
        print(x, end=' ')
else:
    print(f'Bottles: ', end='')
    for x in bottles_line:
        print(x, end=' ')
print(f'\nWasted litters of water: {wasted_water}')

