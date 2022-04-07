judges = int(input())

grade_count = 0
presentation_grade = 0
total_grade = 0
average_presentation_grade = 0
command = input()
while command != "Finish":
    for judge in range(1, judges + 1):
        current_grade = float(input())
        grade_count += 1
        presentation_grade += current_grade
        total_grade += current_grade
        average_presentation_grade = presentation_grade / judges
    print(f"{command} - {average_presentation_grade:.2f}.")
    average_presentation_grade = 0
    presentation_grade = 0
    command = input()
total_average_grade = total_grade / grade_count
print(f"Student's final assessment is {total_average_grade:.2f}.")


