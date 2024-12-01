import folium
import pandas as pd

# Load the CSV file
csv_file_path = 'ELF-HAWK-dump.csv'
df = pd.read_csv(csv_file_path)

# Create a map centered at an average location
average_lat = df['OSD.latitude'].mean()
average_lon = df['OSD.longitude'].mean()
m = folium.Map(location=[average_lat, average_lon], zoom_start=5)

# Add drone locations to the map
for _, row in df.iterrows():
    lat, lon = row['OSD.latitude'], row['OSD.longitude']
    folium.Marker(location=[lat, lon], popup=f"Lat: {lat}, Lon: {lon}").add_to(m)

# Save the map to an HTML file
map_file = 'drone_map.html'
m.save(map_file)
print(f"Map saved to {map_file}")
