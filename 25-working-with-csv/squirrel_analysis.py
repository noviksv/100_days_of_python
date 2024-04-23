import pandas as pd

data = pd.read_csv("2018_Squirrel_Data.csv")

# find count of squirrels in each color
count = data["Primary Fur Color"].value_counts()

count.to_csv("squirrel_count.csv")