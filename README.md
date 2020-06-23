# Queue Branch.
Install: `pip3 install rq redis`

To start Redis install docker desktop and run `docker run -p6379:6379 redis`.


To start the worker: `rq worker stations`

The worker runs the function `station_queue.add_station_from_queue` on every item that gets put in the queue.

The api "stations" POST endpoint puts the request data on the queue.




UK Train Stations Project

Aim of the Project: Import train station data via the api

Setup: Requires python 3

Install dependencies: pip install xlrd

Create csv file from xlsx workbook data: csv_import.py


Description of Files:

csv_import.py:

model.py:

api.py:
