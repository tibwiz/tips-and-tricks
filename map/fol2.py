import pandas as pd
import folium

# Load CSV file containing zip codes and number of units
data = pd.read_csv("data.csv")

# Create a map centered at Texas
m = folium.Map(location=[31.9686, -99.9018], zoom_start=6)

# Add markers for each zip code with number of units in a popup
for idx, row in data.iterrows():
    popup_text = f"Zip Code: {row['ZipCode']}<br>Number of Units: {row['NumberOfUnits']}"
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=popup_text).add_to(m)

# Set the bounds of the map to limit it to Texas
m.fit_bounds([[25.8372, -106.6462], [36.5007, -93.5071]])

# Save the map as an HTML file
m.save("map.html")

