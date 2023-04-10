"""
Simple implementation of iterativ merge sort.

Copyright 2021, University of Freiburg.
Chair of Algorithms and Data Structures.

Axel Lehmann <lehmann@cs.uni-freiburg.de>
Niklas Schnelle <schnelle@cs.uni-freiburg.de>
Patrick Brosi <brosi@cs.uni-freiburg.de>

"""


def merge(lst, left, middle, right):
    """
    Merge lst[left:middle] and lst[middle:right], overwriting lst[left:right]
    with the result. Use the algorithm explained in Vorlesung 1.

    TIP: First copy the two parts from lst to two separate lists and then merge
    these copies and overwrite lst with the result. Merging "in-place" (without
    using separate lists for the input and the output) is very hard.

    >>> lst = [4, 3, 2, 1]
    >>> merge(lst, 0, 1, 2) # sublists: [4], [3] with [2, 1] remaining in lst
    >>> lst
    [3, 4, 2, 1]
    >>> merge(lst, 2, 3, 4) # sublists: [2], [1]
    >>> lst
    [3, 4, 1, 2]
    >>> merge(lst, 0, 2, 4) # sublists: [3, 4], [1, 2]
    >>> lst
    [1, 2, 3, 4]
    """
    pass  # Add your implementation here


def merge_sort(lst):
    """
    Sort the input list lst using the *iterative* MergeSort algorithm, as
    explained in Vorlesung 1.

    >>> lst = []
    >>> merge_sort(lst)
    >>> lst
    []

    >>> lst = [1]
    >>> merge_sort(lst)
    >>> lst
    [1]

    >>> lst = [1, 4, -3]
    >>> merge_sort(lst)
    >>> lst
    [-3, 1, 4]

    >>> lst = [1, 2, 3, 4]
    >>> merge_sort(lst)
    >>> lst
    [1, 2, 3, 4]

    >>> lst = [4, 3, 2, 1]
    >>> merge_sort(lst)
    >>> lst
    [1, 2, 3, 4]

    >>> lst = [1, 4, 2, 3]
    >>> merge_sort(lst)
    >>> lst
    [1, 2, 3, 4]

    >>> import random, copy
    >>> random.seed(42)
    >>> lst = [random.randint(-1000, 1000) for _ in range(0, 63)]
    >>> lst_copy = copy.deepcopy(lst)
    >>> merge_sort(lst)
    >>> sorted(lst_copy) == lst
    True

    """
    pass  # Add your implementation here


def main():
    """ Perform test sortings and output their timings. """
    pass  # Add your implementation here


if __name__ == "__main__":
    main()