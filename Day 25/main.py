import csv
import pandas

def without_pandas():
    with open("weather_data.csv") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        temperatures = [int(row[1]) for row in reader]
        print("The temperatures are", temperatures)

        for row in reader:
            print(row)

def with_pandas():
    weather_table = pandas.read_csv("weather_data.csv")

    temperatures_mean   = weather_table.temp.mean().round(3)
    temperatures_median = weather_table.temp.median().round(3)
    temperatures_std    = weather_table.temp.std().round(3)

    print("The average temperature is", temperatures_mean)
    print("The median temperature is", temperatures_median)
    print("The standard deviation of the temperatures is", temperatures_std)

    max_temp_row = weather_table[weather_table.temp == weather_table.temp.max()]
    print(max_temp_row)

    monday_row = weather_table[weather_table.day == "Monday"]
    print(to_fahrenheit(monday_row.temp))

def create_dataframe():
    dict_example = {
        "names": ["julieta", "catalina", "coté"],
        "ages": [35, 36, 35]
    }
    dataframe = pandas.DataFrame(dict_example)
    dataframe.to_csv("datos.csv")

def to_fahrenheit(temperature_in_celsius):
    fahrenheit = (temperature_in_celsius * 9 / 5) + 32
    return  fahrenheit

def squirrels_data():
    squirrels_table = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

    gray_squirrels_rows     = squirrels_table[squirrels_table["Primary Fur Color"] == "Gray"]
    black_squirrels_rows    = squirrels_table[squirrels_table["Primary Fur Color"] == "Black"]
    cinnamon_squirrels_rows = squirrels_table[squirrels_table["Primary Fur Color"] == "Cinnamon"]

    squirrels_color_dict = {
        "Fur Color": ["gray", "black", "cinnamon"],
        "Count": [len(gray_squirrels_rows), len(black_squirrels_rows), len(cinnamon_squirrels_rows)]
    }
    squirrels_colors_dataframe = pandas.DataFrame(squirrels_color_dict)
    squirrels_colors_dataframe.to_csv("squirrels_colors.csv")


#with_pandas()
#create_dataframe()
squirrels_data()
print("hi")
