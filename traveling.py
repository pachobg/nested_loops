destination = input()
saved_money = 0


while destination != "End":
    needed_budget = float(input())

    while saved_money < needed_budget:
        current_money = float(input())
        saved_money += current_money
        if saved_money >= needed_budget:
            print(f"Going to {destination}!")
            break
    saved_money = 0
    destination = input()


