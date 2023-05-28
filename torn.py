import config
import pygsheets
import pandas as pd

import requests

from datetime import datetime, timezone


now = datetime.now()

torn_api_url = "https://api.torn.com/user/" + config.torn_user_id +"?selections=&key=" + config.torn_key

response = requests.get(torn_api_url)
response.json()

torn_response = response.json()
#print(torn_response)

#authorization, change json file downloaded 
#the google sheet must be created and shared with the email address of the credential api
gc = pygsheets.authorize(service_file='torn-387102-4d620d3b1bcf.json')

# Create empty dataframe
#df = pd.DataFrame(columns=['timestamp','rank','life'])

# Create columns
data = [[now.isoformat(), torn_response["rank"],torn_response["life"]["current"]]]
df = pd.DataFrame(data, columns=['timestamp','rank','life'])

#df['timestamp'] = now.isoformat()
#df['rank'] = torn_response["rank"]
#df['life'] = torn_response["life"]["current"]



print(df)
#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('Torn Statics')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
#wks.set_dataframe(df,(1,1))
#print(wks.get_gridrange('A1','C10'))
wks.append_table(data,start='A1',dimension='ROWS',overwrite=False)
