"""Performs Hebbian Learning Rule on input and calculates corresponding weight"""

from sklearn.datasets import make_blobs
from base import Threshold
import numpy as np


def hebbian(x, c = 1, lamda = 1, iterations=100):
    """Performs hebbian learning rule on input data
    to calculate corresponding weights

    Parameters:
        x: input data
        c: learning rate, default 1
        l: signum steepness constant, default 1
        iterations: number of iterations over data, default 100

    Results:
        weights aligned according to the data
    """
    t = Threshold()
    w = np.random.rand(x.shape[1], 1)
    for _ in range(iterations):
        for point in x:
            net = point.dot(w)
            o = t.sigmoid(net, bipolar = True, lamda = lamda)
            w = w + c*o*point.reshape(point.shape[0], 1)
    return w


def predict(x, w):
    """Predicts the output classes for input and corresponding weights

    Parameters:
        x: input data
        w: weights

    Results:
        returns class assignment for each input point
    """
    t = Threshold()
    pre = t.sigmoid(x.dot(w), bipolar = True)
    pre[pre < 0] = -1
    pre[pre >= 0] = 1
    return pre


def main():
    x, d = make_blobs(n_samples = 50, n_features = 3, centers = 2, random_state = 34)
    w = hebbian(x, iterations = 10)
    print('Weights :: ')
    print(w)
    unique, counts = np.unique(predict(x, w), return_counts = True)
    result = dict(zip(unique, counts))
    for k, v in result.items():
        print('Number of data points in cluster {} :: '.format(k), v)


if __name__ == '__main__':
    main()
