import geopandas as gpd
import matplotlib.pyplot as plt

# Load the Level 0 shapefile for Iran
iran_shapefile = r'path_to_\gadm41_IRN_0.shp'
iran_gdf = gpd.read_file(iran_shapefile)

# Load additional shapefiles for water bodies
lakes_shapefile = r'path_to_\ne_10m_lakes.shp'
coastline_shapefile = r'path_to_\ne_10m_coastline.shp'

lakes_gdf = gpd.read_file(lakes_shapefile)
coastline_gdf = gpd.read_file(coastline_shapefile)

# Define a custom bounding box to include the Persian Gulf and the Gulf of Oman
custom_bbox = [44.0, 24.0, 63.0, 40.0]  # [min_lon, min_lat, max_lon, max_lat]

# Clip lakes and coastlines to the custom bounding box
lakes_clipped = lakes_gdf.cx[custom_bbox[0]:custom_bbox[2], custom_bbox[1]:custom_bbox[3]]
coastline_clipped = coastline_gdf.cx[custom_bbox[0]:custom_bbox[2], custom_bbox[1]:custom_bbox[3]]

# Create a plot
fig, ax = plt.subplots(figsize=(17, 17))
iran_gdf.boundary.plot(ax=ax, linewidth=0.2, color='#005282')  # Plot Iran borders

# Plot clipped lakes and coastlines
lakes_clipped.plot(ax=ax, color='#3EC1CF')  # Lakes and seas
coastline_clipped.plot(ax=ax, color='#005282', linewidth=0.1)  # Coastlines

# Remove axes for a cleaner look
ax.set_axis_off()

# Save the plot as an SVG file with transparency
plt.savefig('iran_map.svg', format='svg', transparent=True)

# Show the plot (optional)
plt.show()
