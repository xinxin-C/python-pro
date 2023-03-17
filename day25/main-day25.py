# with open("weather_data.csv") as data:
#     data_content = data.readlines()
#
# print(data_content)

# import csv
# with open("weather_data.csv") as data:
#     data_content = csv.reader(data) #返回一个csv.reader类
#     temperature = []
#     for row in data_content:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#         print(row)
#
# print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data['temp'])
print(data)
