sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
command = input()
while command != "stop":
    current_num = int(command)
    if current_num < 0:
        print("Number is negative.")
    else:
        number_is_prime = True
        for number in range(2, current_num):
            if current_num % number == 0:
                number_is_prime = False
                break
        if number_is_prime:
            sum_of_prime_numbers += current_num
        else:
            sum_of_non_prime_numbers += current_num

    command = input()
print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")
