import anvil.server
import requests
import pandas as pd

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def dl():
  url = 'https://data.geo.admin.ch'
  path = 'ch.meteoschweiz.klima/nbcn-tageswerte'
  wsurl = url + '/' + path + '/' + 'liste-download-nbcn-d.csv'
  ws = pd.read_csv(wsurl, sep=";", header=0, encoding = "latin_1").dropna()
  pd.options.display.float_format = '{:.2f}'.format
  ws.rename(columns={'Station': 'station'}, inplace=True)
  ws.rename(columns={'station/location': 'label'}, inplace=True)
  ws.rename(columns={'WIGOS-ID': 'wigos-id'}, inplace=True)
  ws.rename(columns={'Data since': 'datasince'}, inplace=True)
  ws.rename(columns={'Station height m. a. sea level': 'elevation'}, inplace=True)
  ws.rename(columns={'Climate region': 'climateregion'}, inplace=True)
  ws.rename(columns={'Latitude': 'latitude'}, inplace=True)
  ws.rename(columns={'Longitude': 'longitude'}, inplace=True)
  ws.rename(columns={'URL Current year': 'urlcurry'}, inplace=True)
  ws.rename(columns={'URL Previous years (verified data)': 'urlprevy'}, inplace=True)

  # Insert weather stations to database table MeteoCH_WeatherStations
  for index, row in ws.iterrows():
    print(row["station"], row["label"])
    app_tables.meteoch_weatherstations.add_row(station=row["station"],
                                               label=row["label"])
    
#                                            dstart=convert_to_date(line[6:14]),
#                                            dend=convert_to_date(line[15:23]),
#                                            height= convert_to_number(line[24:42]),
#                                            lat= convert_to_number(line[43:52]),
#                                            lon= convert_to_number(line[53:60]),
#                                            name=line[61:101].strip(),
#                                            region=line[102:].strip()
#                                            )
  
#  ['Station', 'label', 'WIGOS-ID', 'DataSince', 'Elevation',
#       'CoordinatesE', 'CoordinatesN', 'Latitude', 'Longitude',
#       'ClimateRegion', 'Canton', 'URL Previous years (verified data)',
#       'URL Current year']
#https://data.geo.admin.ch/ch.meteoschweiz.klima/nbcn-tageswerte/nbcn-daily_GSB_previous.csv
#https://data.geo.admin.ch/ch.meteoschweiz.klima/nbcn-tageswerte/nbcn-daily_GSB_current.csv

  #df = dict_to_dataframe(body)
  #df = df.drop('STATIONS_ID', axis=1) # already given as parameter
  # anvil.server.session[ws] = ws ###> not for pandas dataframe...
  dict_list = ws.to_dict('list')
  return(dict_list)

