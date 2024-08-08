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
    #self.state.xyz = 0
    self.state.xyz = ws
    self.drop_down_ClimateRegion.items = sorted(set(ws['ClimateRegion']))
    self.label_Station.visible = False
    self.drop_down_Station.visible = False

  def drop_down_ClimateRegion_change(self, **event_args):
    """This method is called when an item is selected"""
    cr = self.drop_down_ClimateRegion.selected_value
    self.label_Station.visible = True
    self.drop_down_Station.visible = True
    #self.drop_down_Station.items = self.app.state.xyz
    #print(self.ws)
    self.drop_down_Station.items = ['0', '1', '2', '3']    

  def drop_down_Station_change(self, **event_args):
    """This method is called when an item is selected"""
    
    print(self.drop_down_Station.selected_value)



    