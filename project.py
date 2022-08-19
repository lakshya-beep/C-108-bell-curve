import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("projectData.csv")
fig2=ff.create_distplot([df["Avg Rating"].tolist()],["Ratings"])

#fig1.show()
fig2.show()