"""Implements competitive learning rule on a random set of data"""

import numpy as np
from sklearn.datasets import make_blobs
from pprint import pprint as pp


def competitive_learning(x, classes, c = 1):
    """Implements competitive learning rule on an input
    data x with the number of neurons equals classes

    Parameters:
        x: input data
        classes: int, number of output classes
        c: int, learning rate, default 1

    Results:
        adjusted weight for all neurons which map input to output classes.
    """
    a = -5
    b = 5
    w = (b - a)*np.random.random_sample((x.shape[1], classes)) + a
    for point in x:
        net = np.matmul(point, w)
        max_ind = np.argmax(net)
        w[:, max_ind] = w[:, max_ind] + c*point
    return w


def predict(x, w):
    """Predicts the classes according to the competitive learning rule.

    Parameters:
        x: input data
        w: weight matrix for corresponding neurons

    Results:
        assigns corresponding class to each input point
    """
    pre = np.argmax(x.dot(w), axis = 1)
    return pre


def main():
    x = make_blobs(n_samples = 120, n_features = 3, centers = 3, random_state = 69)[0]
    w = competitive_learning(x, 3, c = 1)
    unique, counts = np.unique(predict(x, w), return_counts = True)
    results = dict(zip(unique, counts))
    for k, v in results.items():
        print("Number of examples of class {} :: {}".format(k, v))


if __name__ == '__main__':
    main()
