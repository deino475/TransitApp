from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stops(db.Model):
	id = db.Column(db.String(10), primary_key = True)
	name = db.Column(db.String(100))
	lat = db.Column(db.Float)
	lng = db.Column(db.Float)

	def __init__(self, id, name, lat, lng):
		self.id = id
		self.name = name
		self.lat = lat
		self.lng = lng


class Links(db.Model):
	id = db.Column(db.String(100), primary_key = True)
	stop_id = db.Column(db.String(10))
	route_id = db.Column(db.String(50))

	def __init__(self, id, stop_id, route_id):
		self.id = id
		self.stop_id = stop_id
		self.route_id = route_id


class Edges(db.Model):
	id = db.Column(db.String(100), primary_key = True)
	beginning_stop = db.Column(db.String(10))
	ending_stop = db.Column(db.String(10))
	cost = db.Column(db.Float)

	def __init__(self, id, beginning_stop, ending_stop, cost):
		self.id = id
		self.beginning_stop = beginning_stop
		self.ending_stop = ending_stop
		self.cost = cost


class Routes(db.Model):
	id = db.Column(db.String(100), primary_key = True)
	name = db.Column(db.String(100))
	number = db.Column(db.Integer)
	type = db.Column(db.String(30))

	def __init__(self, id, name, number, type):
		self.id = id
		self.name = name
		self.number = number
		self.type = type