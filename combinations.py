num = int(input())
combinations = 0
for x in range(num + 1):
    for y in range(num + 1):
        for z in range(num + 1):
            sum_num = x + y + z
            if sum_num == num:
                combinations += 1

print(combinations)