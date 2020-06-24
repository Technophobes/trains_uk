# Queue Branch.
Install: `pip3 install rq redis`

To start Redis install docker desktop and run `docker run -p6379:6379 redis`.


To start the worker: `rq worker stations`

The worker runs the function `station_queue.add_station_from_queue` on every item that gets put in the queue.

The api "stations" POST endpoint puts the request data on the queue.




UK Train Stations Project

Aim of the Project: Import train station data via the api to database

Setup: Requires python 3

Install dependencies: `pip install xlrd`



Description of Files:

csv_import.py: This file imports the data in the excel file and posts its contents (using the endpoints in api.py)

model.py: The model contains the 2 classes, Region and Station.

api.py: This file contains all api endpoints.

station_queue.py: This file contains the function to add all stations to the queue that will be later added to the database.
