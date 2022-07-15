from collections import deque

petrol_pumps = int(input())
km_stack = deque()
petrol_stack = deque()
for num in range(petrol_pumps):
    litres_petrol, km_to_next_pump = input().split()
    petrol_stack.append(int(litres_petrol))
    km_stack.append(int(km_to_next_pump))

starting_index = 0
i = 0
petrol_left = 0
while i < petrol_pumps:
    petrol_left += petrol_stack[i]
    if petrol_left >= km_stack[i]:
        petrol_left -= km_stack[i]
        i += 1
    else:
        starting_index += 1
        petrol_stack.rotate(-1)
        km_stack.rotate(-1)
        petrol_left = 0
        i = 0
print(starting_index)







