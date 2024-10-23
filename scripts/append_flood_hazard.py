import geopandas as gpd
from shapely.geometry import Point
import json

# Load the shapefile
shapefile = gpd.read_file('flood/flood.shp')  # Replace with path to your shp file

# Create a spatial index for faster lookup
spatial_index = shapefile.sindex

# Read the JSON file
with open('main/data/mandaue.json', 'r') as file:
    data = json.load(file)

# Loop over the "features" array and update the "hazard" value
for feature in data['features']:
    coordinates = feature["geometry"]["coordinates"]

    # Calculate the center point
    start_lat, start_lng = coordinates[0][1], coordinates[0][0]
    end_lat, end_lng = coordinates[1][1], coordinates[1][0]

    center_lat = (start_lat + end_lat) / 2
    center_lng = (start_lng + end_lng) / 2
    point = Point(center_lng, center_lat)

    # Use the spatial index to directly find geometries that could contain the point
    possible_matches_index = list(spatial_index.intersection(point.bounds))
    possible_matches = shapefile.iloc[possible_matches_index]

    # Check if the point is inside any of the possible geometries
    hazard_idx = 0
    for idx, row in possible_matches.iterrows():
        if row['geometry'].contains(point):
            hazard_idx = idx
            break

    # Update the 'hazard' property with the index (set hazard to 0 if not found)
    feature['properties']['hazard'] = hazard_idx
    print(f"{point} is inside geometry at index {hazard_idx}")

# Save the updated data to a new JSON file
with open('main/data/updated_mandaue.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Hazard values updated and saved to 'mandaue_with_hazard.json'")
