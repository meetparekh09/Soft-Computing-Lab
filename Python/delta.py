"""Implements delta learning rule for
Linearly separable gates
"""

from base import Threshold
from base import DataGenerator
import numpy as np


def delta(x, d, c = 0.1, lamda = 1, iterations = 100):
    """gives weight computed by perceptron learning rule

    Parameters:
        x: matrix, input
        d: teachers signal
        c: learning rate, default 1
        lamda: steepness of sigmoid function
        iterations: iterations to be performed over data, default 100

    Results:
        adjusted weight vector
    """
    w = np.random.rand(x.shape[1], 1)
    t = Threshold()
    for _ in range(iterations):
        for ind, point in enumerate(x):
            net = point.dot(w)
            o = t.sigmoid(net, bipolar = True, lamda = lamda)
            grad = 1/2*((1 - o**2))
            w = w + c*grad*(d[ind] - o)*(point.reshape(point.shape[0], 1))
    return w


def predict(x, d, w):
    """Predicts x using w and compares with actual output to give error

    Parameters:
        x: input
        d: expected output
        w: weight vector

    Results:
        gives error in computation
    """
    err = 0
    t = Threshold()
    for ind, val in enumerate(x):
        net = val.dot(w)
        o = t.sigmoid(net)
        if o > 0:
            o = 1
        else:
            o = -1
        if o != d[ind]:
            err += 1
    return err


def main():
    dg = DataGenerator()
    x, d = dg.prepareBinaryData(gate = 'and', bipolar = True)
    w = delta(x, d)
    separator = '=================================================================='
    print(separator)
    print('For And Gate :: ')
    print('\n\nWeights ::')
    print('\n', w)
    print('\n\nComputation Error ::')
    print('\n', predict(x, d, w))
    print(separator)

    x, d = dg.prepareBinaryData(gate = 'or', bipolar = True)
    w = delta(x, d)
    print(separator)
    print('For Or Gate :: ')
    print('\n\nWeights ::')
    print('\n', w)
    print('\n\nComputation Error ::')
    print('\n', predict(x, d, w))
    print(separator)

    x, d = dg.prepareBinaryData(gate = 'nand', bipolar = True)
    w = delta(x, d)
    print(separator)
    print('For Nand Gate :: ')
    print('\n\nWeights ::')
    print('\n', w)
    print('\n\nComputation Error ::')
    print('\n', predict(x, d, w))
    print(separator)

    x, d = dg.prepareBinaryData(gate = 'nor', bipolar = True)
    w = delta(x, d)
    print(separator)
    print('For Nor Gate :: ')
    print('\n\nWeights ::')
    print('\n', w)
    print('\n\nComputation Error ::')
    print('\n', predict(x, d, w))
    print(separator)


if __name__ == '__main__':
    main()
