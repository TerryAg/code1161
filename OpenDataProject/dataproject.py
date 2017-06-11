import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
df = pd.read_csv("registeredpets.csv")
fontsize = 20

def display_age_graph():
	"""
	Returns a histogram of ages.
	"""
	plt.hist(df["age"][df["age"] < 30], 29, facecolor="blue", alpha=0.75)
	plt.xlabel("Age", fontsize=fontsize)
	plt.ylabel("Number of pets", fontsize=fontsize)
	plt.title("List of all animals and their age")
	plt.grid(True, axis='x', ls=':')
	plt.show()


def pet_count_suburbs():
	"""
	Returns a bar graph of all suburb pet count.
	"""
	d = Counter(df["suburb"])
	suburbs = d.keys()
	suburbs = map(str.strip, sorted(suburbs, key=lambda x:d[x]))
	plt.bar(range(len(d)), sorted(d.values()))
	plt.ylabel("Number of pets", fontsize=fontsize)
	plt.title("Amount of pets in suburbs")
	plt.xticks(map(lambda x: x+0.4, range(len(d))), suburbs, rotation=90, size='xx-small')
	plt.show()


def make_autopct(values):
	# Source: https://stackoverflow.com/a/6170354/1971805
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct


def registered_or_not():
	"""
	Returns a pie chart of registered pets to non-registered.
	"""
	d = defaultdict(int)
	for reg in df["registered"]:
		if reg == "T":
			d["True"] += 1
		elif reg == "F":
			d["False"] += 1
	plt.pie(map(float, d.values()), labels=d.keys(), autopct=make_autopct(d.values()))
	plt.title("Number of registered pets")
	plt.axis('equal')
	plt.show()


def dogs_v_cats():
	"""
	Returns a pie chart of dogs to cats.
	"""
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
	"""
	Returns pie chart of most common colours.
	"""
	d = defaultdict(int)
	colour_count = {}
	#print(df["colour"])
	for colour in df["colour"]:
		# If it's NaN
		if isinstance(colour, float): continue
		slash = map(str.strip, colour.split("/"))
		for col in slash:
			d[col] += 1
	d = {k:v for k, v in d.items() if v > 500} # Only including colours mentioned 500 times or more
	sizes = d.values()
	colour_code = ["blue", "brown", "gold", "peachpuff", "lightslategray", "gray", "orange", "chocolate", "green",
					"black", "sienna", "white", "peru", "moccasin", "tan", "red", "navajowhite"]
	plt.pie(sizes, colors=colour_code, autopct='%1.1f%%')
	plt.axis('equal')
	plt.show()

	
def top_pet_names(number):
	"""
	Returns top number of pet names.
	"""
	d = Counter(df["animal_nam"])
	ranked = sorted(d.items(), key=lambda x: x[1], reverse=True)
	most_common = ranked[:number]
	remaining = 0
	for i in ranked[number:]:
		remaining += i[1]
	main = 0
	for i in most_common:
		main += i[1]
	print("Percentage of top n names: %.2f%%" % (main*1.0/remaining*1.0 * 100.0))
	plt.pie([float(i[1]) for i in most_common], labels=[i[0] for i in most_common], autopct='%1.1f%%')
	plt.title("Top %d cat and dog names" % number)
	plt.axis('equal')
	plt.show()


def top_dogcat_names(number):
	"""
	Plots top number of dog/cat names in a pie chart.
	"""
	d_dog = Counter()
	d_cat = Counter()
	global_count = 0
	for anim in df["type"]:
		row = df.iloc[global_count]
		if anim == "Dog":
			d_dog[row["animal_nam"]] += 1
		elif anim == "Cat":
			d_cat[row["animal_nam"]] += 1
		global_count += 1
	dog_common = d_dog.most_common(number)
	cat_common = d_cat.most_common(number)
	plt.pie([float(i[1]) for i in dog_common], labels=[i[0] for i in dog_common], autopct='%1.1f%%')
	plt.title("Top %d dog names" % number)
	plt.axis('equal')
	plt.show()
	plt.pie([float(i[1]) for i in cat_common], labels=[i[0] for i in cat_common], autopct='%1.1f%%')
	plt.title("Top %d cat names" % number)
	plt.axis('equal')
	plt.show()


if __name__ == '__main__':
	display_age_graph()
	pet_count_suburbs()
	colours()
	registered_or_not()
	dogs_v_cats()
	top_pet_names(5)
	top_dogcat_names(5)