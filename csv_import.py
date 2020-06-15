# This file reads the xls file and saves the worksheet with data as a csv
# https://stackoverflow.com/questions/10802417/how-to-save-an-excel-worksheet-as-csv


import xlrd
import csv

with xlrd.open_workbook('estimates-of-station-usage-2018-19.xlsx') as workbook:
    target_sheet = workbook.sheet_by_name('Estimates of Station Usage')
    # writes target csv file
    with open('train_station_data_uk.csv', 'w', newline="") as csvfile:
        # creates default csv writer object
        csv_object = csv.writer(csvfile)
        for row in range(target_sheet.nrows):
            # adds each row to the csv
            csv_object.writerow(target_sheet.row_values(row))
