"""Consists of Threshold, Data Generation and
other functions required by other modules
"""

import numpy as np
import random
from scipy.special import expit


class Threshold:
    """Consists of all the Threshold functions"""

    def __init__(self):
        pass


    def binary(self, X, bipolar = True, zero = False):
        """Binary threshold function,
        gives 1 for x >= 0 else gives -1 for bipolar
        and 1 for unipolar

            Parameters:
                X: array_like, input
                bipolar: bool, default True, defines output polarity

            Results:
                ndarray having 1 for all elements in X >= 0,
                for other elements gives -1 if bipolar is True
                0 otherwise
        """
        o = np.array(X)
        if zero:
            o[o > 0] = 1
        else:
            o[o >= 0] = 1
        if bipolar:
            o[o < 0] = -1
        else:
            o[o < 0] = 0
        return o


    def sigmoid(self, X, bipolar = True, lamda = 1):
        """Signum threshold function,
        gives value between 1 and -1 if bipolar,
        otherwise gives value between 1 and 0
        if x >= 0 gives value greater than mean,
        otherwise less than mean

            Parameters:
                X: array_like, input for which signum output to be calculated
                bipolar: bool, default True, defines output polarity
                lamda: float, default 1, defines steepness of function

            Results:
                ndarray having value greater than mean for all elements in X >= 0,
                for other elements gives value less than mean
        """
        o = np.copy(X)
        if bipolar:
            o = (2/(1 + np.exp(-lamda * o))) - 1
        else:
            o = 1/(1 + expit(-lamda * o))
        return o


class DataGenerator:
    """defines functions that allow generation of Data
    for the training example
    """

    def __init__(self):
        pass


    def randomData(self, dims, examples, binary = False, bipolar = True):
        """Generates random Data, dims defines number
        of dimension/features in the Data, if binary is True
        then binary data is generated otherwise random float

        Parameters:
            dims: int, number of dimesion/features
            examples: int, determines number of datapoints
            binary: bool, default False determines binary or continuous Data
            bipolar: bool, default True, defines the sign of Data

        Results:
            returns data matrix with examples as row, dims as column,
            if binary is True then only binary data is generated,
            if bipolar is True then datapoints have both positive and
            negative polarity otherwise only positive
        """
        temp = []
        if binary:
            if bipolar:
                bag = [-1, 1]
            else:
                bag = [0, 1]
            for i in range(examples):
                temp.append([])
                for _ in range(dims):
                    temp[i].append(random.choice(bag))
            return np.array(temp)
        else:
            if bipolar:
                return 20*np.random.random_sample((examples, dims)) - 10
            else:
                return 10*np.random.rand(examples, dims)


    def andOutput(self, x, bipolar = True):
        """gives the corresponding teachers signal
        for 'and' gate given the two dimensional binary input

        Parameters:
            x: ndarray, having 2 binary features
            bipolar: bool, default True, defines input as well as output polarity

        Results:
            gives teachers signal for the corresponding input
        """
        d = np.array([np.sum(y) for y in x])
        if bipolar:
            d[d != 2] = -1
        else:
            d[d != 2] = 0
        d[d == 2] = 1
        return d


    def orOutput(self, x, bipolar = True):
        """gives the corresponding teachers signal
        for 'or' gate given the two dimensional binary input

        Parameters:
            x: ndarray, having 2 binary features
            bipolar: bool, default True, defines input as well as output polarity

        Results:
            gives teachers signal for the corresponding input
        """
        d = np.array([np.sum(y) for y in x])
        if bipolar:
            d[d == -2] = -1
            d[d >= 0] = 1
        else:
            d[d > 0] = 1
        return d


    def norOutput(self, x, bipolar = True):
        """gives the corresponding teachers signal
        for 'nor' gate given the two dimensional binary input

        Parameters:
            x: ndarray, having 2 binary features
            bipolar: bool, default True, defines input as well as output polarity

        Results:
            gives teachers signal for the corresponding input
        """
        d = np.array([np.sum(y) for y in x])
        if bipolar:
            d[d >= 0] = -1
            d[d == -2] = 1
        else:
            temp_d = np.copy(d)
            temp_d[d == 0] = 1
            temp_d[d > 0] = 0
            d = np.copy(temp_d)
        return d


    def nandOutput(self, x, bipolar = True):
        """gives the corresponding teachers signal
        for 'nand' gate given the two dimensional binary input

        Parameters:
            x: ndarray, having 2 binary features
            bipolar: bool, default True, defines input as well as output polarity

        Results:
            gives teachers signal for the corresponding input
        """
        d = np.array([np.sum(y) for y in x])
        if bipolar:
            d[d != 2] = 1
            d[d == 2] = -1
        else:
            d[d != 2] = 1
            d[d == 2] = 0
        return d


    def prepareBinaryData(self, gate, bipolar):
        """Generates random binary data for particular gate and corresponding output

        Parameters:
            gate: str, identifies the gate for output
            bipolar: bool, defines polarity of data and output

        Results:
            returns tuple of datapoints and corresponding output as per gate
        """
        dg = DataGenerator()
        x = dg.randomData(2, 1000, binary = True, bipolar = bipolar)
        if gate == 'and':
            d = dg.andOutput(x, bipolar = bipolar)
        elif gate == 'or':
            d = dg.orOutput(x, bipolar = bipolar)
        elif gate == 'nand':
            d = dg.nandOutput(x, bipolar = bipolar)
        else:
            d = dg.norOutput(x, bipolar = bipolar)
        bias = -1*np.ones((x.shape[0], 1))
        x = np.append(x, bias, axis = 1)
        return (x,d)
