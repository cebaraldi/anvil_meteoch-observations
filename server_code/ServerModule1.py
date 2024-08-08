import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
from datetime import datetime
        
def convert_to_number(string_number):
  try:
    return int(string_number)
  except ValueError:
    try:
      return float(string_number)
    except ValueError:
      return None  # Or handle the error differently

def convert_to_date(string_date):
  format_string = "%Y%m%d"
  try:
    return datetime.strptime(string_date, format_string),
  except ValueError:
    return None  # Or handle the error differently

@anvil.server.callable
def dl():
  url = 'https://data.geo.admin.ch'
  path = 'ch.meteoschweiz.klima/nbcn-tageswerte'
  wsurl = url + '/' + path + '/' + 'liste-download-nbcn-d.csv'
  ws = pd.read_csv(wsurl, sep=";", header=0, encoding = "latin_1").dropna()
  pd.options.display.float_format = '{:.2f}'.format
  ws.rename(columns={'Station': 'station'}, inplace=True)
  ws.rename(columns={'station/location': 'label'}, inplace=True)
  ws.rename(columns={'WIGOS-ID': 'wigos_id'}, inplace=True)
  ws.rename(columns={'Data since': 'datasince'}, inplace=True)
  ws.rename(columns={'Station height m. a. sea level': 'elevation'}, inplace=True)
  ws.rename(columns={'Climate region': 'climateregion'}, inplace=True)
  ws.rename(columns={'Canton': 'canton'}, inplace=True)
  ws.rename(columns={'Latitude': 'latitude'}, inplace=True)
  ws.rename(columns={'Longitude': 'longitude'}, inplace=True)
  ws.rename(columns={'URL Current year': 'urlcurry'}, inplace=True)
  ws.rename(columns={'URL Previous years (verified data)': 'urlprevy'}, inplace=True)
  # Insert weather stations to database table MeteoCH_WeatherStations
  for index, row in ws.iterrows():
    app_tables.meteoch_weatherstations.add_row(station=row["station"],
                                               label=row["label"],
                                               wigos_id=row["wigos_id"],
                                               datasince=convert_to_date(row["datasince"]),
                                               elevation=row["elevation"],
                                               lat=row["latitude"],
                                               lon=row["longitude"],
                                               climateregion=row["climateregion"],
                                               canton=row["canton"],
                                               urlcurry=row["urlcurry"],
                                               urlprevy=row["urlprevy"]
                                              )

@anvil.server.callable
def get_ClimateRegion():
  rows = app_tables.meteoch_weatherstations.search()
  unique_values = set(row['region'] for row in rows)
  sorted_values = sorted(list(unique_values))
  return sorted_values  

@anvil.server.callable
def get_Station(ClimateRegion):
  rows = app_tables.meteoch_weatherstations.search(ClimateRegion=q.ilike(ClimateRegion))
  unique_values = set(row['name'] for row in rows)
  sorted_values = sorted(list(unique_values))
  return sorted_values
