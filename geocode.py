import pandas as pd

geolocator = GoogleV3(api_key="")



input_address = pd.read_csv('')

addresses = input_address['']

place = []
lat = []
lon = []
accuracy = []
original_list = []
for item in Addresses:
	results = geolocator.geocode(item, timeout=20)
	if results is not None:
		original_list.append(item)
		place.append(results.address)
		lat.append(results.latitude)
		lon.append(results.longitude)

output_final = pd.DataFrame(dict(orginal_address=original_list, google_address=place, google_lat=lat, google_lon=lon))

output_final.to_csv("C:\Projects\Opera\data\masterfile_addresses_geocoded.csv", index=False)

def add(x, y):
	return x + y