tweeted_cities = []

filename = 'tweeted_cities.json'
with open(filename, 'w') as f:
	json.dump(tweeted_cities, f)