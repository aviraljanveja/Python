# Exception Handling Example.

try:  # Try this block of code.
    a = int(input("Enter a number: "))
    b = int(input("Enter another number : "))
    print("Sum = ", a + b)
    print("Division = ", a / b)

# If an error occurs in the above block, it is handled by except
# statements below.
except ValueError:  # Only for this type of errors
    print("Invalid Input!")
except ZeroDivisionError:  # Only for this type of errors
    print("Can't divide by Zero!")
except:  # For any other type of errors
    print("Something went very wrong!")
