import geopandas as gpd
from shapely.geometry import Point, Polygon
import json

# Read the JSON file
with open('main/data/mandaue.json', 'r') as file:
    data = json.load(file)

# Loop over the "features" array and update the "hazard" value
for feature in data['features']:
    feature['properties']['population'] = 2980
    feature['properties']['zone'] = 'City Core Commercial'

# Save the updated data to a new JSON file
with open('main/data/updated_mandaue.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Hazard values updated and saved to 'updated_mandaue.json'")
