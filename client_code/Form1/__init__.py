from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from utility import filter_dict, filter_by_ClimateRegion 

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindinss.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.ws = anvil.server.call('dl')
    self.drop_down_ClimateRegion.items = sorted(set(self.ws['ClimateRegion']))
    self.label_Station.visible = False
    self.drop_down_Station.visible = False
    
  def drop_down_ClimateRegion_change(self, **event_args):
    """This method is called when an item is selected"""
    cr = self.drop_down_ClimateRegion.selected_value
    print(cr)
    #print(self.ws)
    #newl = filter_dict(self.ws, filter_by_ClimateRegion)
    #newl = filter_dict_by_key(self.ws, 'ClimateRegion', cr)
    #newl = [d for d in dictn if d['Age'] > aget]
    #print(newl)
    self.label_Station.visible = True
    self.drop_down_Station.visible = True
    #self.drop_down_Station.items = self.app.state.xyz
    #print(self.ws)
    self.drop_down_Station.items = ['0', '1', '2', '3']    

  def drop_down_Station_change(self, **event_args):
    """This method is called when an item is selected"""
    
    print(self.drop_down_Station.selected_value)



    