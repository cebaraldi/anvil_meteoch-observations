from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
#from utility import filter_dict, filter_by_ClimateRegion 

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    #anvil.server.call('empty_table', 'meteoch_weatherstations')
    #anvil.server.call('getWeatherStations')
    
    cr = anvil.server.call('get_ClimateRegion')
    print(cr)
    #self.drop_down_ClimateRegion.items = sorted(set(self.ws['ClimateRegion']))
    self.label_Station.visible = False
    self.drop_down_Station.visible = False
          
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
  
  def drop_down_ClimateRegion_change(self, **event_args):
    """This method is called when an item is selected"""
    cr = self.drop_down_ClimateRegion.selected_value
    print(cr)
    self.label_Station.visible = True
    self.drop_down_Station.visible = True
    self.drop_down_Station.items = ['0', '1', '2', '3']    

  def drop_down_Station_change(self, **event_args):
    """This method is called when an item is selected"""
    
    print(self.drop_down_Station.selected_value)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(anvil.server.call('my_variables'))
 





    