# Multithreading in Python
# Used to perform multiple tasks simultaneously, improving performance and responsiveness.
# Good for IO bound tasks, such as file handling or fetching data from APIs.
# The 'threading' module provides a way to create and manage threads in Python.


import threading
import time


def walk_dog(first, last):
    time.sleep(8)  # Simulating time taken to walk the dog
    print(f"Finished walking {first} {last}.")


def make_food():
    time.sleep(10)  # Simulating time taken to make food
    print("Finished making food.")


def eat_food():
    time.sleep(5)  # Simulating time taken to eat food
    print("Finished eating food.")


# Executing the functions in separate threads to run them concurrently
thread1 = threading.Thread(target=walk_dog, args=("Leo", "Pillu"))
thread1.start()

thread2 = threading.Thread(target=make_food)
thread2.start()

thread3 = threading.Thread(target=eat_food)
thread3.start()


# Wait for all threads to complete
thread1.join()
thread2.join()
thread3.join()
print("All tasks completed.")
