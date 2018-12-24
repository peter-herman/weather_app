import pandas as pd
import json, requests
import matplotlib.pyplot as plt
url = 'https://api.weather.gov/points/38.9072,-77.0369'
data = json.loads(requests.get(url).text)
forecast_url = data['properties']['forecastHourly']

forecast_data = json.loads(requests.get(forecast_url).text)
forecast_df = pd.DataFrame(forecast_data['properties']['periods'])

forecast_df.head()
forecast_df['date'] = forecast_df['startTime'].str[5:10]
forecast_df['hour'] = forecast_df['startTime'].str[11:13]
forecast_df['time'] = forecast_df['date'] + ', ' + forecast_df['hour'] + ':00'
forecast_df['Wind'] = forecast_df['windSpeed'].str.rstrip(' mph').astype(int)
fig, axis = plt.subplots()
bar_width = 0.2
axis.bar(forecast_df.index, forecast_df['Wind'],bar_width,
                label='Wind Speed')
axis.set_xlabel('Date, Time')
axis.set_ylabel('Wind Speed (MPH)')
axis.set_title('Hourly Wind Speed Forecast')
axis.set_xticks(forecast_df.index + bar_width / 2)
axis.set_xticklabels(forecast_df['time'])
plt.show()