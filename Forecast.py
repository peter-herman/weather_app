
import pandas as pd
import json, requests

class Forecast(object):
    def __init__(self,
                 coordinates:tuple = (38.9072,-77.0369)):
        self.latitude = coordinates[0]
        self.longitude = coordinates[1]
        self.api_url = 'https://api.weather.gov/points/' + str(self.latitude) + str(self.longitude)
        self.api_landing = json.loads(requests.get(self.api_url).text)
        #forecast_url = self.api_landing['properties']['forecastHourly']
        #forecast_data = json.loads(requests.get(forecast_url).text)
        #forecast_df = pd.DataFrame(forecast_data['properties']['periods'])



