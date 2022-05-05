from urllib.request import urlopen
from utils import *
import json
import pandas as pd
import plotly.express as px

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
ri_traffic_stops = get_ri_stops_df()
rtsPerCountryGeoName = ri_traffic_stops["county_name"].value_counts()
rtsPerCountryGeo = ri_traffic_stops["county_fips"].value_counts()
fipsGeoCode = [i[0] for i in rtsPerCountryGeo.iteritems()]
totalViolationsGeo = [i[1] for i in rtsPerCountryGeo.iteritems()]
fipsGeoName = [i[0] for i in rtsPerCountryGeoName.iteritems()]

fig = px.choropleth(fipsGeoCode, geojson=counties, locations=fipsGeoCode, color=totalViolationsGeo,
                           hover_name=fipsGeoName,
                           color_continuous_scale="Viridis",
                           range_color=(totalViolationsGeo),
                           scope="usa",
                           labels={'unemp':'unemployment rate'},
                           width=1024,
                           height=500
                          )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()