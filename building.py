floors = int(input())
rooms = int(input())

current_number_of_rooms = 0
room_numbers = ""

for f in range(floors, 0, -1):
    for r in range(rooms):
        current_number_of_rooms = f * 10 + r
        if f == floors:
            print(f"L{current_number_of_rooms} ", end="")
        elif f % 2 != 0:
            room_numbers += f"A{current_number_of_rooms} "
        else:
            room_numbers += f"O{current_number_of_rooms} "

    print(room_numbers)
    room_numbers = ""
