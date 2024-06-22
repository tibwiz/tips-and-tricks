import pandas as pd
import folium

# Load CSV file containing zip codes and number of units
data = pd.read_csv("data.csv")

# Create a map centered at Texas
m = folium.Map(location=[31.9686, -99.9018], zoom_start=6)

# Add markers for each zip code with number of units as text labels
for idx, row in data.iterrows():
    label = f"{row['ZipCode']}<br>{row['NumberOfUnits']}"
    folium.Marker(location=[row['Latitude'], row['Longitude']], icon=folium.DivIcon(html=f"<div>{label}</div>")).add_to(m)

# Save the map as an HTML file
m.save("map.html")

