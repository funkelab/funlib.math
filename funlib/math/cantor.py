from __future__ import division


def cantor_number(coordinate):
    '''Return the "Cantor number" of tuples of arbitrary length.

    The Cantor number is the generalization of Cantor's mapping of rational
    numbers (2-tuples) to natural numbers for arbitrary dimensions.

    The numbers obtained this way can be used to uniquely index a positive
    integer coordinate in a volume of unknown size.
    '''

    if len(coordinate) == 1:
        return coordinate[0] + 1

    return (
        pyramide_volume(len(coordinate), sum(coordinate) - 1) +
        cantor_number(coordinate[:-1]))


def pyramide_volume(dims, edge_length):

    prod = 1
    norm = 1
    for d in range(dims):
        prod *= edge_length + d + 1
        norm *= d + 1

    return prod/norm
