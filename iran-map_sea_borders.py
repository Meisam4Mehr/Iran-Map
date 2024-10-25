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

# Clip lakes and coastlines to the bounding box of Iran
iran_bbox = iran_gdf.total_bounds
lakes_clipped = lakes_gdf.cx[iran_bbox[0]:iran_bbox[2], iran_bbox[1]:iran_bbox[3]]
coastline_clipped = coastline_gdf.cx[iran_bbox[0]:iran_bbox[2], iran_bbox[1]:iran_bbox[3]]

# Further clip lakes and coastlines to only include those intersecting with Iran
lakes_clipped = lakes_clipped[lakes_clipped.intersects(iran_gdf.unary_union)]
coastline_clipped = coastline_clipped[coastline_clipped.intersects(iran_gdf.unary_union)]

# Create a plot
fig, ax = plt.subplots(figsize=(17, 17))
ax.set_xlim(iran_bbox[0], iran_bbox[2])
ax.set_ylim(iran_bbox[1], iran_bbox[3])

# Plot Iran borders
iran_gdf.boundary.plot(ax=ax, linewidth=0.2, color='#005282')

# Plot clipped lakes and coastlines
lakes_clipped.plot(ax=ax, color='#3EC1CF')
coastline_clipped.plot(ax=ax, color='#005282', linewidth=0.1)

# Remove axes for a cleaner look
ax.set_axis_off()

# Save the plot as an SVG file with transparency
plt.savefig('iran_map.svg', format='svg', transparent=True)

# Show the plot (optional)
plt.show()
