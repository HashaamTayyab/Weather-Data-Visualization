from pathlib import Path
import csv

path = Path('weather_data\sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, value in enumerate(header_row):
    print(index, value)