import random
from math import radians, cos, sin, asin, sqrt

def generate_random_string(min_num, max_num):
	ret_string = ""
	char_bank = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
	for x in range(random.randint(min_num, max_num)):
		ret_string += char_bank[random.randint(0, len(char_bank) - 1)]
	return ret_string

def haversine(lon1, lat1, lon2, lat2):
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	r = 3956 # Radius of earth in kilometers. Use 3956 for miles
	return c * r