# read csv file

# with open("weather_data.csv") as file:
#     data = [name.strip() for name in file.readlines()]
#     print(data)

# for i in data:
#     print(i.split(","))

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print("Temperatures: ",temperatures)

import pandas as pd


data = pd.read_csv("weather_data.csv")

print(data["temp"])
print(data.to_dict())

#convert temp data to list
temp_list = data["temp"].to_list()
print("Temp List: ",temp_list)

#average temp
average_temp = data["temp"].mean()
print("Average Temp: ",average_temp)
print("Average Temp: ", data ["temp"].sum()/data["temp"].count())

#max temerature

print("Max Temp:",data["temp"].max())

#Get data in columns
print(data["condition"])
#or
print(data.condition)

#Get data in row
print(data[data.day == "Monday"])

#get row with max temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]


#convert temp to fahrenheit
print(monday.temp * 9/5 + 32)


#create a dataframe from scratch
data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}

data = pd.DataFrame(data_dict)
print(data)

#convert dataframe to csv
data.to_csv("new_data.csv")

