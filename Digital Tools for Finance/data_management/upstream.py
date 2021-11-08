
import pandas as pd
import quandl

from connect import DATAPATH

quandl.ApiConfig.api_key = os.environ.get("QUANDL_API_KEY")

def put_df():

  data = quandl.get('USD/GDP', start_date="2011-12-31", end_date="2021-10-31")

  filename = DATAPATH + "my_df.csv"

  data.to_csv(filename)