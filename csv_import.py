import requests
import pandas as pd 
from pandas import *


# The xlsx containing all the station data is converted to a dataframe using pandas
df = pd.read_excel('short-station-usage.xlsx')

# The wrangle function converts the input object to a dict, gets the region's id or posts the region if it doesn't yet exist, then posts the station and all its respective data
def wrangle(input_object):
	input_dict = input_object.to_dict()
	pload_region = {"Region": input_dict["Region"]}
	region_request = requests.get("http://127.0.0.1:5000/region/{}".format(input_dict["Region"]))
	if region_request.status_code == 400:
		region_request = requests.post("http://127.0.0.1:5000/region" , json=pload_region)
	input_dict["region_id"] = region_request.text
	requests.post("http://127.0.0.1:5000/station" , json=input_dict)
	
# This maps the function wrangle onto df, the dataframe which is a reading of the xlsx
# It applies this to each row, denoted by axis=1 
# .fillna(0) replaces all NaN elements with 0s
df.fillna(0).apply(wrangle, axis=1)

