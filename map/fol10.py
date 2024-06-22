import pandas as pd
import folium

# Step 1: Read the CSV file
data = pd.read_csv('data.csv')

# Step 2: Create a map centered around Texas
m = folium.Map(location=[31.9686, -99.9018], zoom_start=6)  # Centered on Texas

# Step 3: Add markers for each zip code
for idx, row in data.iterrows():
    if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f'{row["ZipCode"]} ({row["Number of Units"]})',
            icon=None
        ).add_to(m)

# Save the map as HTML
m.save('texas_zipcode_map.html')
print("HTML file saved successfully.")

