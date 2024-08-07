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
    print(ws)
    self.drop_down_ClimateRegion.items = ['a', 'b', 'c']
    self.drop_down_Station.items = ['0', '1', '2', '3']
    