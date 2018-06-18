import numpy as np

A = np.random.rand(10,1)

print(A)


def func(x):

    return (1 / (1 + np.exp(-x)))


result = np.apply_along_axis(func, 0, A)

print(result)


output



[[0.33896846]
 [0.40939275]
 [0.42340152]
 [0.39278956]
 [0.26226425]
 [0.81972033]
 [0.58533213]
 [0.66287995]
 [0.40966161]
 [0.45308286]]
[[0.58393993]
 [0.60094226]
 [0.60429692]
 [0.59695405]
 [0.56519281]
 [0.69417697]
 [0.6422934 ]
 [0.65990703]
 [0.60100674]
 [0.61137196]]
 
 
 
 
