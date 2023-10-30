from pathlib import Path
import csv
import matplotlib.pyplot as plt

# Giving path and splitting the lines read from the file.
path = Path('weather_data\sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
# Read the csv file format and store all the elements seperated by the de-limiter ','
reader = csv.reader(lines)
header_row = next(reader)
# Extracting the temperature high values present in the csv.
highs = [int(row[4]) for row in reader]

# Drawing the graph on the matplotlib viewer
plt.style.use('grayscale')
fig, ax = plt.subplots()
ax.plot(highs, color = 'red')

# Setting the title and axes labels.
ax.set_title("Daily High Temperatures", fontsize = 24)
ax.set_xlabel("", fontsize = 14)
ax.set_ylabel("Temperature (F)", fontsize = 16)

plt.show()