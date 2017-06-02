import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter, defaultdict
import os
import geopandas as gp
import shapely
import fiona
import folium
from IPython.display import display
df = pd.read_csv("registeredpets.csv")
print(df.columns)

def display_age_graph():
	plt.hist(df["age"][df["age"] < 30], 29, facecolor="blue", alpha=0.75)
	plt.xlabel("Age", fontsize=20)
	plt.ylabel("Number of pets", fontsize=20)
	plt.title("List of all animals and their age")
	plt.grid(True, axis='x', ls=':')
	plt.show()

def pet_count_suburbs():
	d = Counter(df["suburb"])
	suburbs = d.keys()
	suburbs = map(str.strip, sorted(suburbs, key=lambda x:d[x]))
	plt.bar(range(len(d)), sorted(d.values()))
	plt.xticks(map(lambda x: x+0.4, range(len(d))), suburbs, rotation=90, size='xx-small')
	plt.show()

def registered_or_not():
	pass

def colours():
	d = defaultdict(int)
	colour_count = {}
	print(df["colour"])
	for colour in df["colour"]:
		if colour is None: continue
		slash = colour.split("/")
		for c in slash:
			d[c] += 1
	print d

	print(d)
	"""colours = d.keys()[1:]
				sizes = d.values()[1:]
				print(Counter(df["colour"]).keys()[1:])
				fig1, ax1 = plt.subplots()
				ax1.pie(sizes, labels=colours, autopct='%1.1f%%', shadow=True, startangle=90)
				ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
				plt.show()"""
	
#burbs = gp.GeoDataFrame.from_file("Geelong_Roads.shp")
#geelong_coords = [38.1499, 144.3617]
#g=folium.Map(location=geelong_coords, zoom_start=3.6)
#g.save("mymap.html")
#plt.xlim([0, 34564])
#print(burbs.columns)
#print(burbs["GEOCODE"])
#burbs[burbs["GEOCODE"] is not None].plot()
#plt.show()

#display_age_graph()
#pet_count_suburbs()
colours()