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
  ws.rename(columns={'Station height m. a. sea level': 'Elevation'}, inplace=True)
  ws.rename(columns={'station/location': 'label'}, inplace=True)
  print(ws)
#  ['Station', 'label', 'WIGOS-ID', 'Data since', 'Elevation',
#       'CoordinatesE', 'CoordinatesN', 'Latitude', 'Longitude',
#       'Climate region', 'Canton', 'URL Previous years (verified data)',
#       'URL Current year']

#https://data.geo.admin.ch/ch.meteoschweiz.klima/nbcn-tageswerte/nbcn-daily_GSB_previous.csv
#https://data.geo.admin.ch/ch.meteoschweiz.klima/nbcn-tageswerte/nbcn-daily_GSB_current.csv