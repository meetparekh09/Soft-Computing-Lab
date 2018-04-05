"""Implements rbf network"""

import numpy as np
from sklearn.datasets import make_blobs
from scipy.spatial.distance import euclidean
from random import random
from base import Threshold


beta = 0.46


def rbfActivation(x, mean):
    """Calculates the activation of rbf

    Parameters:
        x: input data
        mean: mean of all the prototypes

    Results:
        returns rbf activation output of the input
    """
    for point in x:
        input = []
        for center in mean:
            input.append(np.exp(-beta*euclidean(point, center)**2))
        input = np.array(input)
        yield input


def perceptron(x, d, mean, centers, c = 1, iterations = 100):
    """gives weight computed by perceptron learning rule

    Parameters:
        x: matrix, input
        d: teachers signal
        c: learning rate, default 1
        iterations: iterations to be performed over data, default 100

    Results:
        adjusted weight vector
    """
    inp = rbfActivation(x, mean)
    w = np.random.rand(x.shape[1], centers)
    t = Threshold()
    for i in range(iterations):
        for ind, point in enumerate(inp):
            net = point.dot(w)
            o = t.binary(net)
            out = -1*np.ones(centers)
            out[d[ind]] = 1
            w = w + c*(out - o)*(point.reshape(point.shape[0], 1))
    return w


def predict(x, mean, w, d):
    """Predict the number of misclassified points

    Parameters:
        x: input data
        mean: means of activation prototypes
        w: adjusted weights
        d: expected output

    Results:
        returns the number of misclassified points.
    """
    t = Threshold()
    inp = rbfActivation(x, mean)
    err = 0
    for ind, point in enumerate(inp):
        net = np.matmul(point, w)
        o = t.binary(net)
        c = np.argmax(o)
        if c != d[ind]:
            err += 1
    return err


def main():
    centers = 3
    x, d = make_blobs(n_samples = 150, n_features = 3, centers = centers, random_state = 325)
    mean = []
    for i in range(centers):
        mean.append(np.mean(x[d == i], axis = 0))
    mean = np.array(mean)
    w = perceptron(x, d, mean, centers)
    print(w)
    print(beta)
    print("Error in prediction :: {}".format(predict(x, mean, w, d)))


if __name__ == '__main__':
    main()
