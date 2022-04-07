num1 = int(input())
num2 = int(input())

for number in range(num1, num2 +1):
    odd_digits_sum = 0
    even_digits_sum = 0
    number_as_string = str(number)
    for index, digit in enumerate(number_as_string):
        if index % 2 == 0:
            odd_digits_sum += int(digit)
        else:
            even_digits_sum += int(digit)
    if odd_digits_sum == even_digits_sum:
        print(number_as_string, end=" ")