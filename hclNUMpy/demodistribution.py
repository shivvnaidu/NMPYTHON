import numpy as np
import matplotlib.pyplot as plt # used for graphs
snum=np.random.standard_normal(100)
print(snum)
plt.hist(snum,bins=10)
plt.show()
score=np.array([90,60,65])
print(score.mean())
print(score.std())
print(score.var())