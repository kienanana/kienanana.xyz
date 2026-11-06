---
class: note
tags:
  - y4s1
  - finance/dashboards
source:
related:
author:
date: 2026-10-05
updated: 2026-10-05 19:47:01
aliases:
---
## Interactive Dashboards with Python Dash
![[Screenshot 2026-10-05 at 7.35.23 PM.png]]

## Plotly
```
pip install plotly==5.18.0
```
- free and open source graphing library for python
- over 40 unique chart types 
- built on top of plotly javascript (plotly.js) library
- referred to as "plotly.py"
- enables python users to create interactive web-based visualisations that can be displayed in jupyter notebooks, saved to standalone html files or served as part of pure python-built web applications using Dash
- built in feature for real-time updates of data objects 

## Python Dash
> https://dash.plotly.com/
> https://dash.plotly.com/tutorial
- python framework for building web analytic applications
- built on top of flask, plotly,js and react.js
- suited for anyone who works with data in python
- not static files 
- can interact with the dashboards 
- rendered in web browser 
- can be deployed in servers and URL can be shared 
- cross-platform and mobile ready

### Steps to Build a Dash App (`main.py`)
1. **Import packages**
   ```python
   from dash import Dash, html, dash_table, dcc, callback, Output, Input
   ```
2. **Incorporate data (files)** - load the data to be used in the dashboard.
3. **Initialize the app**
   ```python
   app = Dash(__name__)
   ```
4. **App layout** - define and design components.
   ```python
   app.layout = html.Div([...])
   ```
5. **Add controls to build the interaction** - connect component inputs to outputs using a callback.
   ```python
   @callback(
       Output(component_id='', component_property='figure'),
       Input(component_id='', component_property='value')
   )
   def update_graph(col_chosen):
       fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
       return fig
   ```
   - Replace the empty component IDs with the IDs of the corresponding layout components.
   - This example assumes `df` has been loaded and Plotly Express has been imported as `px` (`import plotly.express as px`).
6. **Run the app**
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```
   Run from the terminal:
   ```bash
   python main.py
   ```


## HTML
- html is comprised of elements
- elements start and end with a tag
	- <tag_name>content</tag_name>
- tags have attributes, values and content 
	- <tag_name attribute='value'>content</tag_name>
- html is not case sensitive (preferential lower case for the tag and attribute names)
![[Screenshot 2026-10-05 at 7.45.28 PM.png]]


![[Screenshot 2026-10-05 at 7.45.39 PM.png]]

## Dash Components
Dash core components (`dcc`) include **Dropdown**, **DatePicker**, and **Input**. Wrap them in `html.Div` with an `html.Label` to label and arrange the controls.

### Instrument Dropdown
```python
def Instrument_Dropdown(id, instruments):
    instrument_dropdown = html.Div([
        html.Label('Select Instrument:', className='input-label'),
	    ### 
        dcc.Dropdown(
            id=id,
            options=[{'label': instrument, 'value': instrument}
                     for instrument in instruments],
            value=instruments[0], className='dropdown'
        )
    ], style={'width': '20%', 'display': 'inline-block'})
    return instrument_dropdown
```
- `options` defines the displayed labels and their corresponding values.
- `value=instruments[0]` selects the first instrument by default.

### Start Date Selector
```python
def Start_Date_Selector(id):
    start_date = html.Div([
        html.Label('Select start date:', className='date-label'),
	    ### 
        dcc.DatePickerSingle(
            id=id,
            date='2020-01-01',
            # end_date='2023-12-20',
            display_format='YYYY-MM-DD',
        )
    ], style={'width': '20%', 'display': 'inline-block'})
    return start_date
```
- `date` sets the initial selected date; `display_format` controls how it is displayed.

### Short-Term Moving Average Input
```python
def STMA(id):
    instrument_input = html.Div([
        html.Label('Enter the short term moving average',
                   className='input-label'),
	    ### 
        dcc.Input(
            id=id,
            type='text',
            # placeholder='Enter MA',
            className='input',
        )
    ], style={'width': '20%', 'display': 'inline-block'})
```
The slide ends after constructing `instrument_input`; add `return instrument_input` to use this helper in the layout.

## Callbacks for Interactive Webpages
- **Output** identifies the component property to update. Here, the callback updates the `children` of `backtest-results`.
- **Input** triggers the callback when its value changes. Here, clicking the button changes `n_clicks`.
- **State** supplies the current values without triggering the callback when those values change. Users can enter parameters first, then click the button to run the backtest.

```python
# Define the callback to update backtest results
@app.callback(
    Output('backtest-results', 'children'),
    [Input('rb-button', 'n_clicks')],
    [State('instrument-dropdown', 'value'),
     State('start_date', 'date'),
     State('end_date', 'date'),
     State('short_ma_period', 'value'),
     State('long_ma_period', 'value')]
)
def update_backtest_results(n, instrument, start_date, end_date,
                            short_ma_period, long_ma_period):
    if n == 0 or any(x is None for x in [instrument, start_date, end_date,
                                        short_ma_period, long_ma_period]):
        raise dash.exceptions.PreventUpdate

    # Fetch historical data
    data = pd.DataFrame(yf.download(instrument, start=start_date,
                                    end=end_date, progress=False))

    # Create moving averages
    data['short_ma'] = data['Close'].rolling(
        window=int(float(short_ma_period))).mean()
    data['long_ma'] = data['Close'].rolling(
        window=int(float(long_ma_period))).mean()
```
- `PreventUpdate` leaves the output unchanged when the button's click count is zero or any required parameter is `None`.
- `yf.download` fetches historical prices for the selected instrument and date range.
- Rolling means of `Close` produce the short-term and long-term moving averages, using the entered window sizes.
- The excerpt assumes imports for `State` (from `dash`), `dash`, `pandas as pd`, and `yfinance as yf`. The slide shows only part of the callback; the remaining backtest logic and returned output are not shown.

### other considerations:
- use a virtual environment 
- live updates: dcc.Interval for auto updates 
- deploy your app to a server 
	- Dash Enterprise is preferred 
	- Heroku or any other cloud provider 
- https://dash.plotly.com/deployment
- trading dashboard


