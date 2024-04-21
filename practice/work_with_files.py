# create file with random context

# Path: practice/work_with_files.py
import random

with open("file.tmp", "w") as file:
    for _ in range(10):
        file.write(f"{random.randint(1, 100)}\n")
# Read the file and print the sum of the numbers in the file

