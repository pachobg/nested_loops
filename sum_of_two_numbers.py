num1 = int(input())
num2 = int(input())
condition = False
counter_x_y = 0
magic_num = int(input())
for x in range(num1, num2 + 1):
    for y in range(num1, num2 + 1):
        counter_x_y += 1
        result = x + y
        if result == magic_num:
            condition = True
            print(f"Combination N:{counter_x_y} ({x} + {y} = {magic_num})")
            break
    if condition:
        break

if not condition:
    print(f"{counter_x_y} combinations - neither equals {magic_num}")