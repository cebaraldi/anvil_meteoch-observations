from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

def strings_to_dates(string_list, date_format="%Y-%m-%d"):  # Adjust date format as needed
  date_list = []
  for string_value in string_list:
    try:
      date_value = datetime.strptime(str(string_value), date_format).date()
      date_list.append(date_value)
    except ValueError:
      # Handle invalid dates, e.g., log an error or skip the value
      print(f"Error converting '{string_value}' to date with format {date_format}")
  return date_list
  
def strings_to_floats(string_list):
  float_list = []
  for string_value in string_list:
    try:
      float_value = float(string_value)
      float_list.append(float_value)
    except ValueError:
      # Handle invalid values, e.g., log an error or skip the value
      print(f"Error converting '{string_value}' to float")
  return float_list

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # DB = 'meteoch_weatherstations'
    #anvil.server.call('empty_table', DB)
    #anvil.server.call('write_weather_stations2DB')   
    
    self.drop_down_ClimateRegion.items = anvil.server.call('get_climate_region')
    self.label_Station.visible = False
    self.drop_down_Station.visible = False
         
  def drop_down_ClimateRegion_change(self, **event_args):
    """This method is called when an item is selected"""
    cr = self.drop_down_ClimateRegion.selected_value
    self.drop_down_Station.items = anvil.server.call('get_station', cr)
    self.label_Station.visible = True
    self.drop_down_Station.visible = True

  def drop_down_Station_change(self, **event_args):
    """This method is called when an item is selected"""
    ws = self.drop_down_Station.selected_value
    print(ws) 
    data = anvil.server.call('get_observations', 
                      ws,
                      self.check_box_CurrentData.checked, 
                      self.check_box_HistoricalData.checked
                     )
#    if self.check_box_CurrentData.checked:
#      urlcurry = anvil.server.call('get_url_current', ws)
#    if self.check_box_HistoricalData.checked:       
#      urlprevy = anvil.server.call('get_url_historical', ws)
    #print(wsid) 
    
    #data = anvil.server.call('dl_csv', wsid)
    Notification('observations downloaded').show()
    
    print(data.keys())
    obsdate = data['date']
    #tmin = data['TNK']
    tavg = data['tre200d0']
    #tmax = data['TXK']
    #print(obsdate)
    #print(tavg)
    #print(f"Length of mininum temperatue observations is {len(tmin)}")
    #print(f"Length of maxinum temperatue observations is {len(tmax)}")

    x = strings_to_dates(obsdate, date_format="%Y%m%d")
    y = replace_negative_999(strings_to_floats(tavg))
    #print(y)

    # Create a Plotly figure
    #fig = go.Figure(data=go.Scatter(x=x, y=y))

    # Display the plot in an Anvil Plot component (client side)
    #self.plot_1.figure = fig        

# ## Air temperature
#axs.plot(df.index, df.tre200d0)
#axs.plot(df.index, df.tre200dn, color='0.8')
#axs.plot(df.index, df.tre200dx, color='0.8')
#plt.ylabel('Air temperature [°C]')
#plt.title('Air temperature 2 m above ground; daily mean\n' + wstation)

# ## Global radiation
#axs.plot(df.index, df.gre000d0)
#plt.ylabel('Global radiation [W/m²]')
#plt.title('Global radiation; daily mean\n' + wstation)

# ## Total snow depth
#axs.plot(df.index, df.hto000d0)
#plt.ylabel('Total snow depth [cm]')
#plt.title('Total snow depth; morning recording at 6 UTC\n' + wstation)

# ## Cloud cover
#xs.plot(df.index, df.nto000d0)
#plt.ylabel('Cloud cover [%]')
#plt.title('Cloud cover; daily mean\n' + wstation)

# ## Pressure at station level 
#xs.plot(df.index, df.prestad0)
#plt.ylabel('Pressure at station level [hPa]')
#plt.title('Pressure at station level (QFE); daily mean\n' + wstation)

# ## Precipitation
#xs.plot(df.index, df.rre150d0)
#plt.ylabel('Cloud cover [mm]')
#plt.title('Precipitation; daily total 6 UTC\n' + wstation)

# ## Sunshine duration
#xs.plot(df.index, df.sre000d0)
#plt.ylabel('Sunshine duration [min]')
#plt.title('Sunshine duration; daily total\n' + wstation)

# ## Relative air humidity
#xs.plot(df.index, df.ure200d0)
#plt.ylabel('Relative air humidity [%]')
#plt.title('Relative air humidity; 2 m above ground; daily\n' + wstation)
