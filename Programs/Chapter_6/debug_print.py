# Example of using print statement as a debugging tool.

def sum_even(numbers):
    total = 0
    print("Initial total:", total)  # Check the initial value of total
    for number in numbers:
        print("Current number:", number)  # Display the current number
        if number % 2 == 0:
            total += number
            print("Added to total:", number)  # Indicate if the number is added to total
    print("Final total:", total)  # Check the final value of total
    return total


num = (1, 2, 3, 4, 5, 6)
sum_even(num)
