import pandas as pd
import folium
import math

floor_counts = pd.read_csv("./tr_number_of_storeys.csv")

m = folium.Map(location=(39, 35), zoom_start=6, tiles="cartodb positron")
folium.Choropleth(

    geo_data = "./tr-cities.json",
    data = floor_counts,
    columns=["city", "number_of_storeys"],
    bins = [1, 2, 3, 4, 5, 6, 7, 8, 8.5],
    key_on="feature.properties.name",
    fill_color = "OrRd",
    fill_opacity=0.8,
    line_opacity=0.3,
    legend_name = "Average number of storeys in a building per city"

).add_to(m)

m.save("choropleth.html")
