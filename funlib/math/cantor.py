from __future__ import division


def pyramide_volume(dims, edge_length):

    prod = 1
    norm = 1
    for d in range(dims):
        prod *= edge_length + d + 1
        norm *= d + 1

    return prod/norm


def cantor_number(coordinate):

    if len(coordinate) == 1:
        return coordinate[0] + 1

    return (
        pyramide_volume(len(coordinate), sum(coordinate) - 1) +
        cantor_number(coordinate[:-1]))
