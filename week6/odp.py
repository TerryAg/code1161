import csv
import pandas as pd
from pylab import show
import matplotlib.pyplot as plt
import matplotlib
df = pd.read_csv("registeredpets.csv")
plt.hist(df["age"][df["age"] < 30], 29, facecolor="blue", alpha=0.75)
plt.xlabel("Age")
plt.ylabel("Number of pets")
plt.title("List of all animals and their age")
plt.grid(True, axis='x', ls='dotted')
plt.show()
# Brown: Both
# Blue: Cats
# Yellow: Dogs
