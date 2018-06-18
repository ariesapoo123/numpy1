import numpy as np

a = np.random.random((10,20))

b = np.random.random((20,25))

z = np.matmul(a, b)

print(z)

print(np.sum(z))

