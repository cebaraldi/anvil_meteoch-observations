from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    ws = anvil.server.call('dl')
    self.drop_down_ClimateRegion.items = sorted(set(ws['ClimateRegion']))
    self.label_Station.visible = False
    self.drop_down_Station.visible = False
    #self.drop_down_Station.items = ['0', '1', '2', '3']

  def drop_down_ClimateRegion_change(self, **event_args):
    """This method is called when an item is selected"""
    #self.drop_down_ClimateRegion.visible = True
    #stations = anvil.server.call('get_ws', self.drop_down_ClimateRegion.selected_value)
    #self.wsDropdown.items = stations

  def drop_down_Station_change(self, **event_args):
    """This method is called when an item is selected"""
    self.label_Station.visible = True
    self.drop_down_Station.visible = True
    self.drop_down_Station.items = ['0', '1', '2', '3']



    