# with open("weather_data.csv") as file:
#   data = file.readlines()
#   print(data)
  
  
import csv

with open("weather_data.csv") as data_file:
  data = csv.reader(data_file)
  print(data)
  for row in data:
    print(row)
  

  