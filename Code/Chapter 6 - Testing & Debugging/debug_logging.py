# Example of how to use logging for a scalable debugging approach.

import logging  # Importing the logging module to enable logging functionality

# Configure the log settings
# level=logging.DEBUG: Sets the minimum level of messages to be logged (DEBUG level and above)
# format='%(levelname)s : %(message)s': Defines the format of log messages
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(message)s')


def factorial(n):
    # Factorial is undefined for negative numbers; log an error and return None
    if n < 0:
        logging.error("Factorial is not defined for negative numbers")
        return None

    result = 1
    # Log a basic information message indicating that the factorial calculation has started
    logging.info("Starting to calculate factorial for n = %d", n)

    for i in range(1, n + 1):
        result *= i
        # Log a debug message showing the intermediate value of result after each multiplication
        logging.debug("i = %d, result = %d", i, result)

    # Log an informational message with the final calculated factorial result
    logging.info("Factorial of %d is %d", n, result)

    return result


user_input = int(input("Enter any positive integer and I will give you the factorial : "))
factorial(user_input)
