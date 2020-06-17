# This file reads the xls file and saves the worksheet with data as a csv
# https://stackoverflow.com/questions/10802417/how-to-save-an-excel-worksheet-as-csv


import xlrd
import requests
from pandas import *

# with xlrd.open_workbook('estimates-of-station-usage-2018-19.xlsx') as workbook:
#     target_sheet = workbook.sheet_by_name('Estimates of Station Usage')
#     for row in range(target_sheet.nrows):
#         print(target_sheet.row_values(row))
    

# xlsx = ExcelFile('short-station-usage.xlsx')
# # for certain sheet: df = xlsx.parse(xlsx.sheet_names[2])
# df = xlsx.parse()

pload_test = {
	'NLC': 5131,
	'TLC': 'ABW',
	'Station Name': 'Abbey Wood',
	'Region': 'London',
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
	# '1819 Entries & Exits': 3769402,
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

# def wrangle(row):
    # requests.post
region_request = requests.post("http://127.0.0.1:5000/region" , json=pload_test)
region_id = region_request.text
print(region_id)
# return row.to_dict()

# request_bodies = df.apply(wrangle, axis=1).tolist()
# print(request_bodies)

# print(df.head())