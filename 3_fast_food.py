from collections import deque

quantity = int(input())
orders = input().split()
list_of_orders = [int(x) for x in orders]
queue = deque(list_of_orders)
print(max(queue))

while queue:
    if queue[0] <= quantity:
        quantity -= queue.popleft()
    else:
        break
if len(queue) > 0:
    print_queue = [str(x) for x in queue]
    print(f"Orders left: {' '.join(print_queue)}")
else:
    print(f'Orders complete')

