from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # DB = 'meteoch_weatherstations'
    #anvil.server.call('empty_table', DB)
    #anvil.server.call('writeWeatherStations2DB')   
    
    self.drop_down_ClimateRegion.items = anvil.server.call('get_ClimateRegion')
    self.label_Station.visible = False
    self.drop_down_Station.visible = False
         
  def drop_down_ClimateRegion_change(self, **event_args):
    """This method is called when an item is selected"""
    cr = self.drop_down_ClimateRegion.selected_value
    self.drop_down_Station.items = anvil.server.call('get_Station', cr)
    self.label_Station.visible = True
    self.drop_down_Station.visible = True

  def drop_down_Station_change(self, **event_args):
    """This method is called when an item is selected"""
    ws = self.drop_down_Station.selected_value
    print(ws) 
    anvil.server.call('get_Observations', 
                      ws,
                      self.check_box_CurrentData.checked, 
                      self.check_box_HistoricalData.checked
                     )
#    if self.check_box_CurrentData.checked:
#      urlcurry = anvil.server.call('get_URLcurrent', ws)
#    if self.check_box_HistoricalData.checked:       
#      urlprevy = anvil.server.call('get_URLhistorical', ws)
    #print(wsid) 
    
    data = anvil.server.call('dl_csv', wsid)
    Notification('observations downloaded').show()
    
    #print(data.keys())
    #obsdate = data['MESS_DATUM']
    #tmin = data['TNK']
    #tavg = data['TMK']
    #tmax = data['TXK']
    #print(obsdate)
    #print(tavg)
    #print(f"Length of mininum temperatue observations is {len(tmin)}")
    #print(f"Length of maxinum temperatue observations is {len(tmax)}")

    #x = strings_to_dates(obsdate, date_format="%Y%m%d")
    #y = replace_negative_999(strings_to_floats(tavg))
    #print(y)

    # Create a Plotly figure
    #fig = go.Figure(data=go.Scatter(x=x, y=y))

    # Display the plot in an Anvil Plot component (client side)
    #self.plot_1.figure = fig        

  def check_box_CurrentData_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass
