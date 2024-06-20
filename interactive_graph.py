import numpy as np
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

datum = {year: pd.read_csv(f'./data/{year}.csv') for year in range(106, 111)}

all_school = set()
for year in range(106, 111):
    for school in datum[year]['學校名稱']:
        all_school.add(school)

app = Dash(__name__)

app.layout = html.Div([
    html.H4('各校退學率、延修率、休學率與排名'),
    dcc.Dropdown(
        id="school",
        options=list(all_school),
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"),
    Input("school", "value")
)
def update_line_chart(school: str):
    overall_data = {year: {'退學率': np.nan, '延修率': np.nan, '休學率': np.nan} for year in range(106, 111)}
    for year in range(106, 111):
        data = datum[year][datum[year]['學校名稱'] == school]
        for attribute in ['退學', '休學', '延修']:
            try:
                overall_data[year][f"{attribute}率"] = (data[f"{attribute}人數-總計"].item() / data['在學學生數-總計'].item())
            except:
                overall_data[year][f"{attribute}率"] = np.nan
    fig = px.line(pd.DataFrame(overall_data).transpose(), y=['退學率', '延修率', '休學率'], x=range(106, 111))
    return fig

def aaa(school: str):
    overall_data = {year: {'退學率': np.nan, '延修率': np.nan, '休學率': np.nan} for year in range(106, 111)}
    for year in range(106, 111):
        data = datum[year][datum[year]['學校名稱'] == school]
        for attribute in ['退學', '休學', '延修']:

            overall_data[year][f"{attribute}率"] = (data[f"{attribute}人數-總計"].item() / data['在學學生數-總計'].item())
    print(pd.DataFrame(overall_data))

aaa('國立成功大學')


app.run_server()
