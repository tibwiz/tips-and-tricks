import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import mplleaflet

# Load Texas zip code shapefile
texas_zipcodes = gpd.read_file("/Users/amannath/Downloads/texas/tl_2010_48_zcta510.shp")

# Load CSV file containing zip codes and number of units
data = pd.read_csv("data.csv")

# Convert the data type of the 'ZipCode' column in the CSV file to string
data['ZipCode'] = data['ZipCode'].astype(str)

# Merge shapefile with data from CSV file based on zip codes
merged_data = texas_zipcodes.merge(data, how='left', left_on='ZCTA5CE10', right_on='ZipCode')

# Create a new figure
fig, ax = plt.subplots()

# Plot the map of Texas zip codes
merged_data.plot(column='NumberOfUnits', cmap='Blues', figsize=(10, 6), legend=True, edgecolor='black', ax=ax)

# Plot numbers on specific zip codes
for idx, row in merged_data.iterrows():
    if not pd.isnull(row['NumberOfUnits']):
        plt.text(row.geometry.centroid.x, row.geometry.centroid.y, str(row['NumberOfUnits']), fontsize=8, color="red")

# Set plot title and labels
plt.title("Number of Housing Units by Zip Code in Texas")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Convert matplotlib plot to interactive Leaflet map and save as HTML file
html_map = mplleaflet.fig_to_html(fig)  # Pass the figure 'fig' instead of the axes 'ax'
with open("map.html", "w") as html_file:
    html_file.write(html_map)

