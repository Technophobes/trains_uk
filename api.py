# This api will import data to the database

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from model import dbconnect, Region, Station
from sqlalchemy import exc

app = Flask(__name__)
CORS(app)

@app.route('/region', methods=['POST'])
def add_region():
	session = dbconnect()
	request_dict = request.get_json()
	try:
		region_instance = Region()
		region_instance.region_name = request_dict["Region"]
		session.add(region_instance)
		session.commit()
		return jsonify(region_instance.id)
	except exc.IntegrityError:
		session.rollback()
		return "already exists", 400

@app.route('/station',  methods=['POST'])
def add_station():
	session = dbconnect()
	request_dict = request.get_json()
	try:
		region_instance = session.query(Region).filter(Region.id == request_dict["region_id"]).one()
	except:
		return "Region does not exist, please add it", 400

	try:
		station = Station()
		station.station_name = request_dict["Station Name"]
		station.total_1819 = request_dict["1819 Entries & Exits"]
		station.NLC = request_dict["NLC"]
		station.TLC = request_dict["TLC"]
		station.Local_Authority = request_dict["Local Authority"]
		station.Constituency = request_dict["Constituency"]
		station.NUTS2_Spatial_Unit = request_dict["NUTS2 Spatial Unit"]
		station.NUTS2_Spatial_Unit_Code = request_dict["NUTS2 Spatial_Unit Code"]
		station.OS_Grid_Easting = request_dict["OS Grid Easting"]
		station.OS_Grid_Northing = request_dict["OS Grid Northing"]
		station.Station_Facility_Owner = request_dict["Station Facility Owner"]
		station.Station_Group = request_dict["Station Group"]
		station.PTE_Urban_Area_Station = request_dict["PTE Urban Area Station"]
		station.London_Travelcard_Area = request_dict["London Travelcard Area"]
		station.Network_Rail_Region_of_station = request_dict["Network Rail Region of station"]
		station.CRP_Line_Designation = request_dict["CRP Line Designation"]
		station.Entries_Exits_Full = request_dict["Entries & Exits_Full"]
		station.Entries_Exits_Reduced = request_dict["Entries & Exits_Reduced"]
		station.Entries_Exits_Season = request_dict["Entries & Exits_Season"]
		station.Entries_Exits_1819 = request_dict["1819 Entries & Exits"]
		station.Entries_Exits_1718 = request_dict["1718 Entries & Exits"]
		station.Interchanges_1819 = request_dict["1819 Interchanges"]
		station.Entries_Exits_1819_GBrank = request_dict["1819 Entries & Exits - GB rank"]
		station.Entries_Exits_1718_GBrank = request_dict["1718 Entries & Exits - GB rank"]
		station.Large_station_change_flag = request_dict["Large station change flag"]
		station.Small_station_change_flag = request_dict["Small station change flag"]
		station.Percent_Change = request_dict["% Change"]
		station.Explanation_of_large_change_1819 = request_dict["Explanation of large change 1819"]
		station.Source_for_explanation_of_large_change_1819 = request_dict["Source for explanation of large change 1819"]
		station.region = region_instance
		session.add(station)
		session.commit()
		return jsonify(station.id)
	except exc.IntegrityError:
		session.rollback()
		return "already exists", 400

@app.route('/region/<search_term>', methods=['GET'])
def get_region(search_term):
	session = dbconnect()
	try:
		region_instance = session.query(Region).filter(Region.region_name == search_term).one()
		return jsonify(region_instance.id), 200
	except:
		return "Region doesn't exist in database", 400

@app.route('/station/<search_term>', methods=['GET'])
def get_station(search_term):
	session = dbconnect()
	# try:
	# 	region_instance = session.query(Region).filter(Region.region_name == search_term).one()
	# 	return jsonify(region_instance.id), 200
	# except:
	# 	return "Region doesn't exist in database", 400


#{"region_id" : 3 , "Station Name": "london"}

# This provides the error message on the url
if __name__ == '__main__':

	app.run(debug=True)