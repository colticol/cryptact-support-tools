import pandas as pd


class CustomFile(object):
  """
  Control Custom File for Crytact
  """
  def __init__(self):
    self.t = pd.DataFrame(columns=['Timestamp', 'Action', 'Source', 'Base', 'DerivType', 'DerivDetails', 'Volume', 'Price', 'Counter', 'Fee', 'FeeCcy', 'Comment'])


  def append(self, *args):
    row = pd.Series(args, index=self.t.columns)
    self.t = self.t.append(row, ignore_index=True)


  def write(self, filename='custom.csv'):
    self.t.to_csv(filename, index=False)
