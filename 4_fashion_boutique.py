clothes = input().split()
rack_capacity = int(input())
racks = {}
rack_num = 1

while clothes:
    clothes_item = int(clothes[-1])
    if rack_num not in racks:
        racks[rack_num] = []
    if sum(racks[rack_num]) + clothes_item < rack_capacity and len(clothes) > 0:
        racks[rack_num].append(clothes_item)
        clothes.pop(-1)
    else:
        rack_num += 1
        racks[rack_num] = []
        racks[rack_num].append(clothes_item)
        clothes.pop(-1)

print(len(racks))
#judge: 60/100

