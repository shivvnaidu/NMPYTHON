import numpy as np
import matplotlib.pyplot as plt
num = np.fromfile("C://data/numbers.txt", dtype=int, sep=",")
#print(type(num))
items = np.genfromtxt("c:/data/alphabets.txt", dtype='str', delimiter=",")
#print(type(items))
x = np.arange(len(items))
plt.bar(x,num)
plt.xticks(x,items)
plt.xlabel("numbers")
plt.ylabel("items")
plt.show()