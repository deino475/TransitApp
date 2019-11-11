import sys
import csv
import json

sys.path.append("..")

from functions import generate_random_string
from app import app
from models import db, Stops, Links, Edges, Routes

with app.app_context():
	#ADD ROUTES TO DATABASE
	with open("routes.json","r") as file_to_read:
		data = json.load(file_to_read)
		for row in data['d']['results']:
			new_route = Routes(row['RouteId'], row['LongName'], row['RouteName'], row['RouteType'])
			db.session.add(new_route)
			db.session.commit()

	#ADD STOPS TO DATABASE
	with open("stops.csv","r") as file_to_read:
		csv_to_read = csv.reader(file_to_read)
		for row in csv_to_read:
			current_stop = Stops.query.filter_by(id = row[1]).first()
			if current_stop != None:
				continue
			new_stop = Stops(row[1],row[0],row[3],row[2])
			db.session.add(new_stop)
			db.session.commit()

	#ADD LINKS TO DATABASE
	with open("stops.csv","r") as file_to_read:
		csv_to_read = csv.reader(file_to_read)
		for row in csv_to_read:
			new_link = Links(generate_random_string(10,20), row[1], row[5])
			db.session.add(new_link)
			db.session.commit()

	#ADD EDGES TO DATABASE
	with open("edges.csv","r") as file_to_read:
		csv_to_read = csv.reader(file_to_read)
		for row in csv_to_read:
			new_edge = Edges(generate_random_string(10,20),row[0],row[1],int(row[2]))
			db.session.add(new_edge)
			db.session.commit()

print("Finished")
