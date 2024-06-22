import geopandas as gpd

# Load the shapefile
texas_zipcodes = gpd.read_file("/Users/amannath/Downloads/2020/tl_2020_us_zcta520.shp")

# Print the columns of the attribute table
print("Columns of the attribute table:")
print(texas_zipcodes.columns)

