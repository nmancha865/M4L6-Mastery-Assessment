from pathlib import Path
import os
import csv
import plotly.express as px

# Debugging: Print the current working directory
print(f"Current Working Directory: {os.getcwd()}")

# Define the relative or absolute path
# Use absolute path for testing purposes:
path = Path(r"C:\Users\natno\Downloads\eq_data\world_fires_1_day.csv")

# Check if the file exists
if not path.is_file():
    print(f"File not found: {path}")
    exit()

# Read the file and split into lines
lines = path.read_text().splitlines()

# Use csv.reader to parse the lines
reader = csv.reader(lines)
header_row = next(reader)

# Extract lat, lon, brightness
lats, lons, brights = [], [], []
for row in reader:
    if len(row) < 3:  # Ensure there are at least 3 columns
        print(f"Skipping row with insufficient data: {row}")
        continue
    
    try:
        lat = float(row[0])  # Lat
        lon = float(row[1])  # Lon
        bright = float(row[2])  # Brightness
    except ValueError:
        print(f"Invalid data for row: {row}")
    else:
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# Check if there is data to plot
if not lats or not lons or not brights:
    print("No valid data available to plot.")
    exit()

# Plot brightnesses on a world map.
title = "Global wildfire activity"
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
                     color=brights, 
                     color_continuous_scale='Viridis', 
                     labels={'color': 'Brightness'},
                     projection='natural earth')

# Display the plot
fig.show()



This Python code creates a world map of fires across the world from one day and plots based on how bright they where
