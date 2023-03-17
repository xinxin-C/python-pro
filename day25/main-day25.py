import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data['temp'].max())
#
# #get data in column
# print(data.condition) # DataFrame类会把每一列转成attributes
#
# #get data in row
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)  #可以从挑出来的row中再挑数据
# mon_temp = int(monday.temp)
# print(mon_temp * 9 / 5 + 32)
#
# #creat a dataframe from scratch

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")