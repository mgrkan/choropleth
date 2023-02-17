import plotly.express as px
import pandas as pd

df = pd.read_csv("./tr_number_of_storeys.csv")
fig = px.bar(df, y="number_of_storeys",x ="city", title="Average number of storeys in a building per city")
fig.show()
