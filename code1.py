import geopandas as gpd
import pandas as pd
import plotly.express as px

# Read the DataFrame from a CSV file
df = pd.read_csv("average_temperatures_1950.csv", encoding='latin1')

# Change the name of "United States" to "United States of America"
df['Country'] = df['Country'].replace('United States', 'United States of America')

# Read the GeoJSON file and create a GeoDataFrame
gdf = gpd.read_file('countries.geojson')

# Merge the DataFrame with the GeoDataFrame based on the 'Country' column
merged = gdf.merge(df, left_on='ADMIN', right_on='Country')

# Create a Plotly choropleth map
fig = px.choropleth(merged,
                    geojson=merged.geometry,
                    locations=merged.index,
                    color='AverageTemperature',
                    color_continuous_scale='RdYlBu_r',
                    range_color=(-20, 30),
                    projection='natural earth')

# Customize the map layout
fig.update_layout(title_text='Average Temperature by Country (1950)',
                  geo=dict(showframe=False,
                           showcoastlines=False,
                           projection_type='natural earth'))

# Display the map
fig.show()
