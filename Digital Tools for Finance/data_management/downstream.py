import pandas as pd
from connect import DATAPATH

def get__data(subset, start_dt="2001-01-01", end_dt="2005-12-31"):
  
  filename = DATAPATH + "my_df.csv"

  df = pd.read_csv(filename)

  return df