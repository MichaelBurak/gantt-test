import pandas as pd
import numpy as np
import plotly
import plotly.express as px

from datetime import datetime, timedelta

# establish start date of today
Today = datetime.today()


def create_date_list(n, interval):
    '''today create timedelta looping over range of 0-n deltas at n min intervals'''
    return [Today + timedelta(minutes=interval*x) for x in range(0, n)]


# list of 100 time records at 15 min intervals
date_list = create_date_list(50, 15)
# appending 3 min intervals, 7 min intervals
three_min_intervals = create_date_list(100, 3)
seven_min_intervals = create_date_list(50, 7)
date_list.extend(three_min_intervals)
date_list.extend(seven_min_intervals)

# formatting the datelist
datetext = [x.strftime('%Y-%m-%d %H:%M %S') for x in date_list]

df = pd.DataFrame(datetext, columns=['start'])

# create new df with every second value in second column
new_df = pd.DataFrame(
    {'start': df['start'].iloc[::2].values, 'end': df['start'].iloc[1::2].values})

# needs to be done column-wise, whole df doesn't seem to work so far, convert to datetim
new_df['start'] = pd.to_datetime(new_df['start'], format='%Y-%m-%d %H:%M %S')
new_df['end'] = pd.to_datetime(new_df['end'], format='%Y-%m-%d %H:%M %S')

# creating chart
fig = px.timeline(new_df, x_start="start", x_end="end")
# otherwise tasks are listed from the bottom up
fig.update_yaxes(autorange="reversed")
plotly.offline.plot(fig, filename='gantt_test.html')
