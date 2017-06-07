import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from collections import Counter, defaultdict
import os
from math import isnan
df = pd.read_csv("registeredpets.csv")
print(df.columns)
fontsize = 20

def display_age_graph():
	plt.hist(df["age"][df["age"] < 30], 29, facecolor="blue", alpha=0.75)
	plt.xlabel("Age", fontsize=fontsize)
	plt.ylabel("Number of pets", fontsize=fontsize)
	plt.title("List of all animals and their age")
	plt.grid(True, axis='x', ls=':')
	plt.show()

def pet_count_suburbs():
	#
	d = Counter(df["suburb"])
	suburbs = d.keys()
	suburbs = map(str.strip, sorted(suburbs, key=lambda x:d[x]))
	plt.bar(range(len(d)), sorted(d.values()))
	plt.ylabel("Number of pets", fontsize=fontsize)
	plt.title("Amount of pets in suburbs")
	plt.xticks(map(lambda x: x+0.4, range(len(d))), suburbs, rotation=90, size='xx-small')
	plt.show()
#do above but dogs/cats separated
# https://stackoverflow.com/questions/23293011/how-to-plot-a-superimposed-bar-chart-using-matplotlib-in-python

def make_autopct(values):
	# https://stackoverflow.com/a/6170354/1971805
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

def registered_or_not():
	d = defaultdict(int)
	for reg in df["registered"]:
		if reg == "T":
			d["True"] += 1
		elif reg == "F":
			d["False"] += 1
		#else:nan
	plt.pie(map(float, d.values()), labels=d.keys(), autopct=make_autopct(d.values()))
	plt.title("Number of registered pets")
	plt.axis('equal')
	plt.show()

def dogs_v_cats():
	d = defaultdict(int)
	for t in df["type"]:
		if t == "Dog":
			d["Dogs"] += 1
		elif t == "Cat":
			d["Cats"] += 1
	plt.pie(map(float, d.values()), labels=d.keys(), autopct=make_autopct(d.values()))
	plt.title("Number of dogs and cats")
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
	plt.title("Most common colours of pets")
	plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	plt.show()
	
def top_pet_names(number):
	"""
	Returns top number of pet names
	"""
	d = Counter(df["animal_nam"])
	#print(d)
	#print(d.items())
	ranked = sorted(d.items(), key=lambda x: x[1], reverse=True)
	most_common = ranked[:number]
	remaining = 0
	for i in ranked[number:]:
		remaining += i[1]
	main = 0
	for i in most_common:
		main += i[1]
	print(main)
	print("Percentage of top n names: %.2f%%" % (main*1.0/remaining*1.0 * 100.0))
	print("Top %d names:" % number)
	for name in most_common:
		print(name[0], name[1])
	plt.pie([float(i[1]) for i in most_common], labels=[i[0] for i in most_common])
	plt.title("Top %d cat and dog names" % number)
	plt.axis('equal')
	plt.show()

def top_dogcat_names(number):
	d_dog = Counter()
	d_cat = Counter()
	global_count = 0
	for anim in df["type"]:
		if anim == "Dog":
			d_dog[df.iloc[global_count]["animal_nam"]] += 1
		elif anim == "Cat":
			d_cat[df.iloc[global_count]["animal_nam"]] += 1
		global_count += 1
	dog_common = d_dog.most_common(number)
	cat_common = d_cat.most_common(number)
	print(dog_common)
	print(cat_common)
	plt.pie([float(i[1]) for i in dog_common], labels=[i[0] for i in dog_common])
	plt.title("Top %d dog names" % number)
	plt.axis('equal')
	plt.show()
	plt.pie([float(i[1]) for i in cat_common], labels=[i[0] for i in cat_common])
	plt.title("Top %d cat names" % number)
	plt.axis('equal')
	plt.show()

# BASICS #
display_age_graph()
pet_count_suburbs()
colours()
registered_or_not()
dogs_v_cats()
top_pet_names(5)
top_dogcat_names(5)



