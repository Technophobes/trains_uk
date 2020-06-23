from model import dbconnect, Region, Station, dbconnect
from sqlalchemy import exc

def add_station_from_queue(request_dict):
	session = dbconnect()
	try:
		region_instance = session.query(Region).filter(Region.id == request_dict["region_id"]).one()
	except:
		print("Region does not exist, please add it")
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
		return station.id
	except exc.IntegrityError:
		session.rollback()
		return "already exists. something broken with q function."
