
import requests
import pandas as pd 
from pandas import *

# ADD BENEATH TO GOOGLE DOC ONCE BACK ON INTERNET
# This will show us all the headers of the columns
# print(df.head())

# Here we use pandas to create dict from excel data by creating a pandas dataframe
# for certain sheet: df = xlsx.parse(xlsx.sheet_names[2])
# xlsx = ExcelFile('short-station-usage.xlsx')
# df = xlsx.parse()

pload_test = {
	'NLC': 5131,
	'TLC': 'ABW',
	'Station Name': 'Abbey Wood',
	'Region': 'Somerset',
	'Local Authority': 'Bexley (London)',
	'Constituency': 'Erith and Thamesmead',
	'NUTS2 Spatial Unit': 'Outer London - East and North East',
	'NUTS2 Spatial_Unit Code': 'UKI5',
	'OS Grid Easting': 547374,
	'OS Grid Northing': 179035,
	'Station Facility Owner': 'TfL Rail',
	'Station Group': nan,
	'PTE Urban Area Station': nan,
	'London Travelcard Area': 'London Travelcard Area Station',
	'Network Rail Region of station': 'Southern',
	'CRP Line Designation': nan,
	'Entries & Exits_Full': 882924,
	'Entries & Exits_Reduced': 1233842,
	'Entries & Exits_Season': 1652636.0,
    '1819 Entries & Exits': 3769402,
	'1718 Entries & Exits': 3124850,
	'1819 Interchanges': nan,
	'1819 Entries & Exits - GB rank': 145,
	'1718 Entries & Exits - GB rank': 176,
	'Large station change flag': 1.0,
	'Small station change flag': nan,
	'% Change': 0.20626654079395812,
	'Explanation of large change 1819': nan,
	'Source for explanation of large change 1819': nan
}


# added df.fillna(0) to replace all NaN elements with 0s
#print(df.fillna(0).to_dict())

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
df.apply(wrangle, axis=1)

