import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("C:/Users/sravy/White Hat Jr/C 108- Bell Curve- Normal Distribution/data.csv")

#fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist = False)
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist = False)
fig.show()