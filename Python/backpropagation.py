"""Implements backpropagation algorithm on a ranodm set of data"""


import numpy as np
from sklearn.datasets import make_blobs
from sklearn import datasets
from base import Threshold
from pprint import pprint as pp


def backpropagation(x, n_layer1, classes, d, c = 1, lamda = 1):
    """Implements backpropagation algorithm on two layer neural networks

    Parameters:
        x: input data
        n_layer1: int, number of neurons in layer 1
        classes: int, number of output classes
        c: int, learning rate, default 1
        lamda: int, steepness of sigmoid function, default 1

    Results:
        adjusted weights for both layers of neural network
    """
    v = np.random.rand(x.shape[1], n_layer1)
    w = np.random.rand(n_layer1, classes)
    t = Threshold()
    for _ in range(10000):
        for ind, point in enumerate(x):
            y = t.sigmoid(np.matmul(point, v), bipolar = True, lamda = lamda)
            o = t.sigmoid(np.matmul(y, w), bipolar = True, lamda = lamda)
            res = -1*np.ones(classes)
            res[d[ind]] = 1
            delo = 1/2*(res - o)*(1 - np.square(o))
            dery = 1/2*(1 - np.square(y))
            dely = dery*(np.matmul(delo, w.T))
            v = v + c*dely*point.reshape(point.shape[0], 1)
            w = w + c*delo*y.reshape(y.shape[0], 1)
    return v, w


def predict(x, v, w, d):
    """ Predicts the number of misclassified points as per two layered neural networks

    Parameters:
        x: input data,
        v: weights for layer 1
        w: weights for layer 2
        d: correct classification class

    Results:
        number of misclassified points as err
    """
    err = 0
    t = Threshold()
    for ind, point in enumerate(x):
        y = t.sigmoid(np.matmul(point, v), bipolar = True, lamda = 1)
        o = t.sigmoid(np.matmul(y, w), bipolar = True, lamda = 1)
        c = np.argmax(o)
        if c != d[ind]:
            err += 1
    return err


def main():
    #x, d = make_blobs(n_samples = 150, n_features = 3, centers = 2, random_state = 235)
    x = np.array([[1, 3, -1], [3, 3, -1], [1, 2, -1], [2, 2, -1], [3, 2, -1], [2, 1.5, -1], [-2, 0, -1], [1, 0, -1], [3, 0, -1], [5, 0, -1]])
    d = np.array([0, 0, 0, 1, 0, 1, 1, 1, 1, 0])
    v, w = backpropagation(x, n_layer1 = 3, classes = 2, d = d)
    print("Weights of hidden layer(V) :: ")
    pp(v)
    print("Weights of output layer(W) :: ")
    pp(w)
    print("Number of misclassified points :: {}".format(predict(x, v, w, d)))


if __name__ == '__main__':
    main()
