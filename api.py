# This api will import data to the database

# Every request will look like below. Api needs to handle this

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
		region_instance.region = request_dict["Region"]
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
		region_instance = session.query(Region).filter(Region.region_name == request_dict["Region"]).one()
	except:
		return "Region does not exist, please add it", 400

	try:
		station = Station()
		station.region = request_dict["Region"]
		station.station_name = request_dict["Station Name"]
		station.total_1819 = request_dict["1819 Entries & Exits"]
		station.region_id = region_instance.id
		session.add(station)
		session.commit()
		return jsonify(station.id)
	except exc.IntegrityError:
		session.rollback()
		return "already exists", 400

# to get the error message on the url
if __name__ == '__main__':

	app.run(debug=True)