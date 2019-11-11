import sys
import csv
import json

sys.path.append("..")

from functions import generate_random_string, haversine
from app import app
from models import db, Stops, Links, Edges, Routes

index = 0.0
with app.app_context():
	stops = Stops.query.all()
	num_stops = len(stops) * 1.0
	for begin_stop in stops:
		index += 1.0
		print(begin_stop.id)
		print(str(index / num_stops))
		for end_stop in stops:
			if begin_stop.id != end_stop.id:
				distance = haversine(begin_stop.lng, begin_stop.lat, end_stop.lng, end_stop.lat)
				existing_edge = Edges.query.filter_by(beginning_stop = begin_stop.id).filter_by(ending_stop=end_stop.id).first()
				if existing_edge == None:
					if distance < 1:
						new_edge = Edges(generate_random_string(10,20), begin_stop.id, end_stop.id, distance)
						db.session.add(new_edge)
						db.session.commit()

print("Finished")