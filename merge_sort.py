"""
Simple implementation of iterativ merge sort.

Copyright 2021, University of Freiburg.
Chair of Algorithms and Data Structures.

Axel Lehmann <lehmann@cs.uni-freiburg.de>
Niklas Schnelle <schnelle@cs.uni-freiburg.de>
Patrick Brosi <brosi@cs.uni-freiburg.de>

"""
import time
import random

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
    # pass  # Add your implementation here
    left_part = lst[left:middle]
    left_index = 0
    right_part = lst[middle:right]
    right_index = 0
    reihe = left
    
    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] < right_part[right_index]:  #! <= or <
            lst[reihe] = left_part[left_index]
            left_index += 1
        else:
            lst[reihe] = right_part[right_index]
            right_index += 1
        reihe += 1
        
    while left_index < len(left_part):
        lst[reihe] = left_part[left_index]
        left_index += 1
        reihe += 1
    
    while right_index < len(right_part):
        lst[reihe] = right_part[right_index]
        right_index += 1
        reihe += 1
    return lst

# print(merge([4, 3, 2, 1], 0, 1, 2))
# print(merge([3, 4, 2, 1], 2, 3, 4))
# print(merge([3, 4, 1, 2], 0, 2, 4))

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
    # empty or one-element list is already sorted
    if len(lst) < 2:
        return lst

    # Initialize the size of the sorted subsequences
    size = 1

    # Loop until all the elements are sorted
    while size < len(lst):
        # Loop over the list by pairs of subsequences of size "size"
        for left in range(0, len(lst), 2*size):
            middle = left + size
            right = min(left + 2*size, len(lst))
            merge(lst, left, middle, right)

        # Double the size of the sorted subsequences
        size *= 2
    return lst

# print(merge_sort([]))
# print(merge_sort([1]))
# print(merge_sort([1, 4, -3]))
# print(merge_sort([1, 2, 3, 4]))
# print(merge_sort([4, 3, 2, 1]))
# print(merge_sort([1, 4, 2, 3]))


# def main():
#     """ Perform test sortings and output their timings. """
#     sizes = [10, 100, 1000, 10000]
#     for size in sizes:
#         lst = [random.randint(-1000, 1000) for _ in range(size)]
#         start_time = time.time()
#         merge_sort(lst)
#         end_time = time.time()
#         print(f"Size: {size}, Time: {end_time - start_time} seconds.")

def main():
    """ Perform test sortings and output their timings. """
    for n in range(500, 10001, 500):
        # Create array with elements: n - 1, ..., 0.
        array = [k for k in range(n, 0, -1)]
        # Sort with MergeSort and time it.
        start_time = time.monotonic()
        merge_sort(array)
        end_time = time.monotonic()
        # Print the array size and the time in milliseconds.
        duration = int(round((end_time - start_time) * 1000.0))
        print("%d\t%d" % (len(array), duration), flush=True)


if __name__ == "__main__":
    main()