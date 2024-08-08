import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.

def filter_dict(data, condition):
  """Filters a dictionary based on a condition.

  Args:
    data: The dictionary to filter.
    condition: A function that takes a key-value pair and returns a boolean.

  Returns:
    A new dictionary containing only the key-value pairs that meet the condition.
  """

  return {k: v for k, v in data.items() if condition(k, v)}

def filter_by_ClimateRegion(k, v):
  return v['ClimateRegion'] == 'Engadin' # TypeError: list indices must be integers or slices, not str
