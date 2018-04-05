import numpy as np
from scipy.special import expit

x = np.array([[1, 1, 1], [1, 2, 1], [2, -1, 1], [2, 0, 1], [-1, 2, 0], [-2, 1, 0], [-1, -1, 0], [-2, -2, 0]])
d = np.array([[1, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 1]])
w = np.random.rand(x.shape[1] - 1, 4)
w = np.vstack((w, np.array([-1, -1, -1, -1]).reshape(1, 4)))
print(w)

err = -1
iterations = 0
while err != 0 and iterations <= 1000:
    err = 0
    c = 0.1
    iterations += 1
    for point, out in zip(x, d):
        net = point.dot(w)
        o = np.zeros(net.shape[0])
        o[np.argmax(net)] = 1
        err += np.sum(out - o)
        w = w + c*(out - o)*point.reshape(point.shape[0], 1)

print(err)
print(iterations)

print(w)
