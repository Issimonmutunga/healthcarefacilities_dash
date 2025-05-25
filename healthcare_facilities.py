import requests
import pandas as pd
import geopandas as gpd
import dash
from dash import dcc, html
import plotly.express as px

# Function to fetch data from CKAN data API
def fetch_healthcare_data(resource_id, query=None, limit=5):
    base_url = 'https://energydata.info/api/3/action/datastore_search'
    params = {
        'resource_id': resource_id,
        'limit': limit
    }
    if query:
        params['q'] = query

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['success']:
        return pd.DataFrame(data['result']['records'])
    else:
        raise Exception("Error fetching data from CKAN API")

# Fetch data
resource_id = '841097c2-9424-4c90-b1e7-8e942a817c3c'
df = fetch_healthcare_data(resource_id)

# Drop Null values in latitude and longitude columns
df = df.dropna(subset=['Latitude', 'Longitude'])

# Load country shapefile
country_gdf = gpd.read_file(r'C:\Projects\Python\shp\County.shp')

# Convert country GeoDataFrame to GEOJSON
country_geojson = country_gdf.__geo_interface__

# Create point map using plotly
fig = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    color="County",
    hover_name="Facility_N",
    zoom=6,
    height=600
)

# Add shapefile outline
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_layers=[{
        "source": country_geojson,
        "type": "line",
        "color": "black",
        "line": {"width": 1},
    }],
    margin={"r": 0, "t": 0, "l": 0, "b": 0}
)

# Dash App
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Healthcare Facilities Dashboard"),
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run(debug=True)
