import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter
import os
import geopandas as gp
import shapely
import fiona
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


"""print(os.path.isfile("geelongpos/Geelong_POS.shp"))
burbs = gp.GeoDataFrame.from_file("geelongpos/Geelong_POS.shp")
print("here")
plt.savefig('mynewmap.png')
burbs.plot()
plt.show()"""

display_age_graph()
#print(set(map(str.strip, df["suburb"])))
#map_suburbs()
#df.head()
#display_age_graph()

