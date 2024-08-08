import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
from datetime import datetime
import requests
        
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
def getWeatherStations():
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
  unique_values = set(row['climateregion'] for row in rows)
  sorted_values = sorted(list(unique_values))
  return(sorted_values)

@anvil.server.callable
def get_Station(ClimateRegion):
  rows = app_tables.meteoch_weatherstations.search(climateregion=q.ilike(ClimateRegion))
  unique_values = set(row['station'] for row in rows)
  sorted_values = sorted(list(unique_values))
  return(sorted_values)

@anvil.server.callable
def get_WSID(station):
  rows = app_tables.meteoch_weatherstations.search(station=q.ilike(station))
  unique_values = set(row['station'] for row in rows)
  sorted_values = sorted(list(unique_values))
  return(sorted_values)
  
@anvil.server.callable
def empty_table(table_name):
  table = getattr(app_tables, table_name)
  table.delete_all_rows()

@anvil.server.callable
def dl_zip(wsid):
  url = "https://opendata.dwd.de/"
  path = 'climate_environment/CDC/observations_germany/climate/daily/kl/'
  recent_path = path + 'recent/'
  filename = f"tageswerte_KL_{wsid}_akt.zip"
  url = url + recent_path + filename
  body = {}
  r = requests.get(url)
  with closing(r), zipfile.ZipFile(io.BytesIO(r.content)) as archive:   
    # print({member.filename: archive.read(member) for member in archive.infolist()})
    body ={member.filename: archive.read(member) 
           for member in archive.infolist() 
           if (member.filename.startswith('produkt_klima_tag_'))
          }
  df = dict_to_dataframe(body)
  df = df.drop('STATIONS_ID', axis=1) # already given as parameter
  dict_list = df.to_dict('list')
  return(dict_list)

