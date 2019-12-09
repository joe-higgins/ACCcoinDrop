import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
import pandas as pd

conn = sqlite3.connect('acc2019.db')
df = pd.read_sql_query(
    '''SELECT player as Player, bet as Bet
    FROM Bets WHERE week_num=1 ORDER BY bet, player''', conn)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('ACC Coin Drop'),
    dcc.Graph(id='example',
              figure = {
                'data': [
                    {'x':df.Player, 'y':df.Bet, 'type':'bar', 'name':'Guesses'},
                    ],
                'layout':{
                    'title':'Player Guesses'
                    }
                })
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
