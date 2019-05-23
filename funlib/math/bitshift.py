import numpy as np


def encode64(c, shifts=None):
    """
    Encodes a tuple c into an int64
    """
    id64 = 0
    cum_shift = 0
    if shifts is None:
        # If shifts are not given we will evenly
        # space the bits
        shifts = [64 // len(c) for _ in c]
    for d in range(len(c)):
        id64 |= c[d] << cum_shift
        cum_shift += shifts[d]
    return id64


def decode64(id64, dims, shifts=None):
    if shifts is None:
        # If shifts are not given we will evenly
        # space the bits
        shifts = [64 // dims for _ in range(dims)]
    coord = []
    for d in range(dims):
        mask = (1 << shifts[d]) - 1
        coord.append(np.uint64(id64 & mask))
        id64 = id64 >> shifts[d]
    return coord
