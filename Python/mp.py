"""Implements simple McCulloh-Pitts neurons on linearly separable logic gates"""

import numpy as np
from base import Threshold
from base import DataGenerator


def andMP(X, d):
    """Implements MP Neuron for and gate and gives error in computation

    Parameters:
        X: input data points
        d: corresponding output

    Results:
        gives error in computation
    """
    t = Threshold()
    err = 0
    w = np.array([1, 1, 1.5]).reshape(3,1)
    for ind, point in enumerate(X):
        net = np.matmul(point, w)
        o = t.binary(net, bipolar = True)
        if o != d[ind]:
            err += 1
    return err


def orMP(X, d):
    """Implements MP Neuron for or gate and gives error in computation

    Parameters:
        X: input data points
        d: corresponding output

    Results:
        gives error in computation
    """
    t = Threshold()
    err = 0
    w = np.array([1, 1, -1]).reshape(3,1)
    for ind, point in enumerate(X):
        net = np.matmul(point, w)
        o = t.binary(net, bipolar = True)
        if o != d[ind]:
            err += 1
    return err


def nandMP(X, d):
    """Implements MP Neuron for nand gate and gives error in computation

    Parameters:
        X: input data points
        d: corresponding output

    Results:
        gives error in computation
    """
    t = Threshold()
    err = 0
    w = np.array([-1, -1, -1.5]).reshape(3,1)
    for ind, point in enumerate(X):
        net = np.matmul(point, w)
        o = t.binary(net, bipolar = True)
        if o != d[ind]:
            err += 1
    return err


def norMP(X, d):
    """Implements MP Neuron for nor gate and gives error in computation

    Parameters:
        X: input data points
        d: corresponding output

    Results:
        gives error in computation
    """
    t = Threshold()
    err = 0
    w = np.array([-1, -1, 1.5]).reshape(3,1)
    for ind, point in enumerate(X):
        net = np.matmul(point, w)
        o = t.binary(net, bipolar = True)
        if o != d[ind]:
            err += 1
    return err


def main():
    dg = DataGenerator()
    x, d = dg.prepareBinaryData(gate = 'and', bipolar = True)
    separator = '=================================================================='
    print(separator)
    print('For And Gate :: ')
    print('Computation Error ::')
    print('\n', andMP(x, d))
    print(separator)

    x, d = dg.prepareBinaryData(gate = 'or', bipolar = True)
    print(separator)
    print('For Or Gate :: ')
    print('Computation Error ::')
    print('\n', orMP(x, d))
    print(separator)

    x, d = dg.prepareBinaryData(gate = 'nand', bipolar = True)
    print(separator)
    print('For Nand Gate :: ')
    print('Computation Error ::')
    print('\n', nandMP(x, d))
    print(separator)

    x, d = dg.prepareBinaryData(gate = 'nor', bipolar = True)
    print(separator)
    print('For Nor Gate :: ')
    print('Computation Error ::')
    print('\n', norMP(x, d))
    print(separator)


if __name__ == '__main__':
    main()
