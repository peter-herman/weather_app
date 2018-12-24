
import pandas as pd

class Forecast(object):
    def __init__(coordinates:tuple = (38.9072,-77.0369)):
        self.lattitude = coordinates[0]
        self.longitude = coordinates[1]
        self.api_url = 'https://api.weather.gov/points/' + str(self.lattitude) + self.longitude
        self.api_landing = pd.read_json(self.api_url)


