
import dash
import dash_core_components as dcc
import dash_html_components as html
from pytrends.request import TrendReq
import plotly.graph_objs as go

# Google Trends setup
pytrends = TrendReq(hl='en-US', tz=360)

# Keywords to search for
keywords = ['sustainable fashion', 'slow fashion', 'eco friendly clothing']

# Build payload
pytrends.build_payload(kw_list=keywords)

# Interest Over Time
interest_over_time_df = pytrends.interest_over_time()

# Dash app setup
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Fashion Trends Dashboard'),
    
    dcc.Graph(
        id='trends-graph',
        figure={
            'data': [
                go.Scatter(
                    x=interest_over_time_df.index,
                    y=interest_over_time_df[keyword],
                    mode='lines',
                    name=keyword
                ) for keyword in keywords
            ],
            'layout': go.Layout(
                title='Interest Over Time',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Interest'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
