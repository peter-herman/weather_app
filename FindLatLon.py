import json, requests
import pandas as pd

url = 'https://api.weather.gov/stations'
stations_json = data = json.loads(requests.get(url).text)
stations_list_outer = stations_json['features']
stations_list = []
for station in stations_list_outer:
    stations_list.append(station['properties'])
stations_df = pd.DataFrame(data = stations_list)