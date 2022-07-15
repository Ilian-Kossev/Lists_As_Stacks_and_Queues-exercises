from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque(input().split())
locks = deque(input().split())
intelligence_value = int(input())

bullet_count = 0
reload_count = 0
while True:
    if len(bullets) == 0 or len(locks) == 0:
        break
    bullet_count += 1
    reload_count += 1
    if int(bullets[-1]) <= int(locks[0]):
        print('Bang!')
        bullets.pop()
        locks.popleft()
    else:
        print('Ping!')
        bullets.pop()
    if reload_count == barrel_size and len(bullets) > 0:
        print('Reloading!')
        reload_count = 0
        continue
price_shots = bullet_count * bullet_price
money_earned = intelligence_value - price_shots
if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f'{len(bullets)} bullets left. Earned ${money_earned}')

