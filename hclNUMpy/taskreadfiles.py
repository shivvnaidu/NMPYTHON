import numpy as np
import matplotlib.pyplot as plt

year1 = np.fromfile("C://data/YEAR1.txt", dtype=int, sep=":")
year2 = np.fromfile("C://data/YEAR2.txt", dtype=int, sep=":")
sale1 = np.fromfile("C://data/year1sales.txt", dtype=int, sep=":")
sale2 = np.fromfile("C://data/year2sales.txt", dtype=int, sep=":")
plt.plot(year1, sale1, label="year one sales")
plt.plot(year2, sale2, label="year two sales")
plt.xlabel('years')
plt.ylabel('sales')
plt.title('sales comparison')
plt.show()
