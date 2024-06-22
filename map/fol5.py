import pandas as pd
import geopandas as gpd
import folium

# Load the shapefile
texas_zipcodes = gpd.read_file("/Users/amannath/Downloads/2020/tl_2020_us_zcta520.shp")

# Print the columns of the attribute table
print("Columns of the attribute table:")
print(texas_zipcodes.columns)

# Step 1: Read the CSV file
data = pd.read_csv('data.csv')

# Convert ZipCode column to object type
data['ZipCode'] = data['ZipCode'].astype(str)

# Step 2: Merge data from CSV with Texas zip code boundaries
texas_zipcodes = texas_zipcodes.merge(data, how='left', left_on='ZCTA5CE20', right_on='ZipCode')

# Step 3: Generate HTML file using folium
m = folium.Map(location=[31.9686, -99.9018], zoom_start=6)  # Centered on Texas

# Add choropleth layer
folium.Choropleth(
    geo_data=texas_zipcodes,
    name='choropleth',
    data=data,
    columns=['ZipCode', 'Number of Units'],
    key_on='feature.properties.ZCTA5CE20',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number of Units'
).add_to(m)

# Step 4: Add labels
for idx, row in texas_zipcodes.iterrows():
    folium.Marker(
        location=[row.geometry.centroid.y, row.geometry.centroid.x],
        popup=f'{row["ZCTA5CE20"]} ({row["Number of Units"]})',
        icon=None
    ).add_to(m)

# Save the map as 

