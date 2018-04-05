"""Implements bidirectional associative memory"""

import numpy as np
from base import DataGenerator
from base import Threshold


def bidirectional(a, b):
    """Implements bidirectional algorithm to find weights
    for bidirectional mapping

    Parameters:
        a: one set of data
        b: another set of data

    Results:
        weights that map a to b and b to a
    """
    w = np.zeros((a.shape[1], b.shape[1]))
    for p, q in zip(a,b):
        w += np.matmul(p.reshape(p.shape[0], 1), q.reshape(1, q.shape[0]))
    return w


def main():
    dg = DataGenerator()
    t = Threshold()
    a = dg.randomData(dims = 5, examples = 3, binary = True, bipolar = True)
    b = dg.randomData(dims = 3, examples = 3, binary = True, bipolar = True)
    for p, q in zip(a,b):
        print("input {} - output {}".format(p, q))
    print("\n\n")
    w = bidirectional(a, b)
    for p, q in zip(a,b):
        print("input {} maps to output {}".format(p, t.binary(np.matmul(p, w), bipolar = True)))
        print("input {} maps to output {}".format(q, t.binary(np.matmul(q, w.T), bipolar = True)))


if __name__ == '__main__':
    main()
