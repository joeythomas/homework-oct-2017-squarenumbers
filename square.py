MAX = 1000
counter = 1

# Method to square a number
def square(number):
    return number * number

# Method to get the last digit
# Use modulus to get the remainder.
def last_digit(number):
    return number % 10

# Method to test if the last digit is 1, 4, 7 or 9
def number_ends_with_one_four_seven_or_nine(number):
    digit = last_digit(number)
    return (digit == 1) or (digit == 4) or (digit == 7) or (digit == 9)   

for counter in range(1, MAX):
    counter_squared = square(counter)
    if counter_squared >= MAX:
        break

    if number_ends_with_one_four_seven_or_nine(counter_squared):
        print(counter_squared)