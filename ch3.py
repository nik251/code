import numpy as np
g = np.arange(15)
g.reshape((3,5))
h = g.reshape((5,3))
h.T
h.transpose()
np.random.seed(100)
r = np.arange(12).reshape((4,3))
s = np.arange(12).reshape((4,3))*0.5
print(r)
print(s)
print(r+s)

