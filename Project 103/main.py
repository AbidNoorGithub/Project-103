import pandas as pd

import plotly_express as px

chart = pd.read_csv("CovidChart.csv")

Scatterplot = px.scatter(chart, x = "date", y = "cases", color = "country")

Scatterplot.show()