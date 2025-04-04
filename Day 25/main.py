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
        "ages": [34, 35, 35]
    }
    dataframe = pandas.DataFrame(dict_example)
    dataframe.to_csv("datos.csv")

def to_fahrenheit(temperature_in_celsius):
    fahrenheit = (temperature_in_celsius * 9 / 5) + 32
    return  fahrenheit

#with_pandas()
create_dataframe()