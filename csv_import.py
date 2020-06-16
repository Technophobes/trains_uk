# This file reads the xls file and saves the worksheet with data as a csv
# https://stackoverflow.com/questions/10802417/how-to-save-an-excel-worksheet-as-csv


import xlrd
from pandas import *

# with xlrd.open_workbook('estimates-of-station-usage-2018-19.xlsx') as workbook:
#     target_sheet = workbook.sheet_by_name('Estimates of Station Usage')
#     for row in range(target_sheet.nrows):
#         print(target_sheet.row_values(row))
    

xlsx = ExcelFile('estimates-of-station-usage-2018-19.xlsx')
df = xlsx.parse(xlsx.sheet_names[2])

empty_dict = {}
def wrangle(row):
    return row.to_dict()

request_bodies = df.apply(wrangle, axis=1).tolist()
print(request_bodies)

# print(df.head())