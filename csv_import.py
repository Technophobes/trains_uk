
import requests
from pandas import *

# This will show us all the headers of the columns
# print(df.head())


pload_test = {
	'NLC': 5131,
	'TLC': 'ABW',
	'Station Name': 'Abbey Wood',
	'Region': 'Somerset',
	# 'Local Authority': 'Bexley (London)',
	# 'Constituency': 'Erith and Thamesmead',
	# 'NUTS2 Spatial Unit': 'Outer London - East and North East',
	# 'NUTS2 Spatial_Unit Code': 'UKI5',
	# 'OS Grid Easting': 547374,
	# 'OS Grid Northing': 179035,
	# 'Station Facility Owner': 'TfL Rail',
	# 'Station Group': nan,
	# 'PTE Urban Area Station': nan,
	# 'London Travelcard Area': 'London Travelcard Area Station',
	# 'Network Rail Region of station': 'Southern',
	# 'CRP Line Designation': nan,
	# 'Entries & Exits_Full': 882924,
	# 'Entries & Exits_Reduced': 1233842,
	# 'Entries & Exits_Season': 1652636.0,
    '1819 Entries & Exits': 3769402,
	# '1718 Entries & Exits': 3124850,
	# '1819 Interchanges': nan,
	# '1819 Entries & Exits - GB rank': 145,
	# '1718 Entries & Exits - GB rank': 176,
	# 'Large station change flag': 1.0,
	# 'Small station change flag': nan,
	# '% Change': 0.20626654079395812,
	# 'Explanation of large change 1819': nan,
	# 'Source for explanation of large change 1819': nan
}

# Here we use pandas to create dict from excel data by creating a pandas dataframe
# for certain sheet: df = xlsx.parse(xlsx.sheet_names[2])
xlsx = ExcelFile('short-station-usage.xlsx')
df = xlsx.parse()
# added df.fillna(0) to replace all NaN elements with 0s
print(df.fillna(0).to_dict())

# We got one instance to work for the pload_region dictionary.
# Now we need to put it in the function. Do we need to turn the dataframe into a list of dicts?
# Do we need to bring the function to the dataframe?

# BELOW ISN'T WORKING WITH FUNCTION
def wrangle(row):
    for row in df:
        pload_region = {"Region": pload_test["Region"]}
        region_request = requests.post("http://127.0.0.1:5000/region" , json=pload_region)
        region_id = region_request.text

        pload_station = {"Station Name": pload_test["Station Name"], "1819 Entries & Exits" : pload_test["1819 Entries & Exits"], "Region" : { "id" : region_id}}
        station_request = requests.post("http://127.0.0.1:5000/station" , json=pload_station)
        return row.to_dict()

# The following 5 lines were from Tuesday, June 17:
# def wrangle(row):
#     return row.to_dict()

# request_bodies = df.apply(wrangle, axis=1).tolist()
# print(request_bodies)






