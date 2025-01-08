# While loop for taking user-input
# he while loop is particularly useful for scenarios where
# you need to repeatedly take user input until a certain condition is met.
# Especially when the number of iterations isn't known in advance.
# This is where it is often preferred over a for loop.
# For example : Let's say you want to keep asking the user for input until they type "exit".

while True:
    user_input = input("Enter a word (type 'exit' to stop): ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")
