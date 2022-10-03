from math import ceil

list_of_nums = [int(x) for x in input().split(', ')]

max_num = max(list_of_nums)
groups_count = ceil(max_num / 10)

for every_group in range(1, groups_count + 1):
    group_count = [num for num in list_of_nums if every_group * 10 - 10 \
            < num <= every_group * 10]
    print(f"Group of {every_group*10}'s: {group_count}") 
