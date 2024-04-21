# create file with random context

# Path: practice/work_with_files.py
import random

with open("file.tmp", "w") as file:
    for _ in range(10):
        file.write(f"{random.randint(1, 100)}\n")
# Read the file and print the sum of the numbers in the file

# appending the sum of the numbers to the file
with open("file.tmp", "r") as file:
    numbers = file.readlines()
    sum_of_numbers = sum([int(number) for number in numbers])
    print(sum_of_numbers)
    with open("file.tmp", "a") as file:
        file.write(f"Sum of the numbers: {sum_of_numbers}")