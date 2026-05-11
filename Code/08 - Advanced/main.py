#  if __name__ == '__main__'
# This basically means that the code inside the main() function will only be executed if the script is run directly, and not when it is imported in another script.
# If we were to import this script in another script, the code inside the main function would not be executed,
# allowing us to reuse the functions and classes defined in this script without running the code inside main().


def main():
    print("This code will run only when the script is executed directly.")


if __name__ == '__main__':
    main()  # This will be executed, only if this script is run directly.
