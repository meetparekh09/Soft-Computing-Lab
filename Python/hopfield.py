"""Implements hopfield network on random set of binary bipolar data."""

import numpy as np
from base import DataGenerator
from base import Threshold


def hopfield(x):
    """Finds the weights for the hopfield network

    Parameters:
        x: input data

    Results:
        returns weights for the hopfield associative memory
    """
    w = np.zeros((x.shape[1], x.shape[1]))
    for point in x:
        w += np.matmul(point.reshape(point.shape[0], 1), point.reshape(1, point.shape[0])) - np.identity(point.shape[0])
    return w


def main():
    dg = DataGenerator()
    t = Threshold()
    x = dg.randomData(dims = 3, examples = 3, binary = True, bipolar = True)
    w = hopfield(x)
    print(w)
    for point in x:
        net = np.matmul(point, w)
        out = t.binary(net, bipolar = True, zero = True)
        ind = (out == 0)
        out[ind] = point[ind]
        print("For input point {}, output :: {}".format(point, out))


if __name__ == '__main__':
    main()
