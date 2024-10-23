import geopandas as gpd
from shapely.geometry import Point, Polygon
import json

# Read the JSON file
with open('main/data/mandaue.json', 'r') as file:
    data = json.load(file)

# Read the Historical Strip Zone Polygon GeoJSON file
with open('main/data/historical_strip_polygon.json', 'r') as f:
    historical_strip_feature_collection = json.load(f)

# Extract the 2D coordinates array from the GeoJSON file
historical_strip_polygon_coordinates_2d_array = historical_strip_feature_collection["features"][0]["geometry"]["coordinates"][0]

# Convert the 2D array into a list of tuples
historical_strip_polygon_coordinates_tuple_list = [(coord[0], coord[1]) for coord in historical_strip_polygon_coordinates_2d_array]

# Create a Polygon object from the tuple list
historical_strip_polygon = Polygon(historical_strip_polygon_coordinates_tuple_list)

# Loop over the "features" array and update the "hazard" value
for feature in data['features']:
    coordinates = feature["geometry"]["coordinates"]

    # Calculate the center point of the feature's line geometry
    start_lat, start_lng = coordinates[0][1], coordinates[0][0]
    end_lat, end_lng = coordinates[1][1], coordinates[1][0]

    center_lat = (start_lat + end_lat) / 2
    center_lng = (start_lng + end_lng) / 2
    point = Point(center_lng, center_lat)

    # Check if the center point is inside the historical strip polygon
    is_inside_historical_strip = historical_strip_polygon.contains(point)

    feature['properties']['population'] = 2980
    feature['properties']['zone'] = 'City Core Commercial'

    if is_inside_historical_strip:
        feature['properties']['zone'] = 'Historical Strip'

    print(f"{point} belongs to {feature['properties']['zone']} Zone")

# Save the updated data to a new JSON file
with open('main/data/updated_mandaue.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Hazard values updated and saved to 'updated_mandaue.json'")
