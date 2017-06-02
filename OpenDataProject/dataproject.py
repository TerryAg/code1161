import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from collections import Counter, defaultdict
import os
import geopandas as gp
import shapely
import fiona
import folium
from IPython.display import display
from math import isnan
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
	d = defaultdict(int)
	for reg in df["registered"]:
		if reg == "T":
			d["True"] += 1
		elif reg == "F":
			d["False"] += 1
		#else:nan
	plt.pie(map(float, d.values()), labels=d.keys())
	plt.axis('equal')
	plt.show()

def colours():
	d = defaultdict(int)
	colour_count = {}
	#print(df["colour"])
	for colour in df["colour"]:
		# if it's a nan
		if isinstance(colour, float): continue
		slash = map(str.strip, colour.split("/"))
		for c in slash:
			d[c] += 1
	d = {k:v for k, v in d.items() if v > 500}
	colours = d.keys()
	sizes = d.values()
	colour_code = ["blue", "brown", "gold", "peachpuff", "lightslategray", "gray", "orange", "chocolate", "green",
					"black", "sienna", "white", "peru", "moccasin", "tan", "red", "navajowhite"]
					#green = tricolour
	plt.pie(sizes,labels=colours, colors=colour_code, autopct='%1.1f%%')
	plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	plt.show()
	
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
#colours()
registered_or_not()