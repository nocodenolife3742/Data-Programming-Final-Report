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
    html.H4(
        '各校退學率、延修率、休學率',
        style={'textAlign': 'center', 'color': 'black', 'fontSize': 24, 'fontWeight': 'bold'}
    ),
    dcc.Dropdown(
        id="school",
        options=list(all_school),
        value=list(all_school)[0],
        style={'width': '50%', 'margin': 'auto', 'margin-bottom': '20px'},
        clearable=False
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
                overall_data[year][f"{attribute}率"] = data[f"{attribute}人數-總計"].item() / data[
                    '在學學生數-總計'].item()
            except:
                overall_data[year][f"{attribute}率"] = np.nan
    fig = px.line(
        pd.DataFrame(overall_data).transpose(),
        y=['退學率', '延修率', '休學率'],
        x=range(106, 111)
    )
    fig.update_layout(
        xaxis_title="年分",
        yaxis_title="比例",
    )
    return fig


app.run_server()
