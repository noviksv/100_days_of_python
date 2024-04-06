print("Welcome to the tip calculator!!!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate the tip
bill_with_tips = total_bill * (1 + tip_percentage / 100)

# Calculate the bill per person
bill_per_person = bill_with_tips / people

# Print the bill per person with 2 decimal places
print(f"Each person should pay: ${bill_per_person:.2f}")

