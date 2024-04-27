
#iterating lists of numbers

import random

numbers = [random.randint(1, 100) for _ in range(10)]

#print only even numbers    
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

#iterating dictionaries
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# convert temperature from Celsius to Fahrenheit
weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)


# iterating pandas dataframe
import pandas as pd

students_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}


df = pd.DataFrame(students_dict)
print(df)
#loop through the dataframe
for (index, row) in df.iterrows():
    print(row.students, row.scores)