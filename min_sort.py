import time

def min_sort(array):
    """
    Sort the given array of integers using the MinSoer algorithm explained in Vorlesung 01.
    
    >>> min_sort([17, 4, 32, 19, 8, 65, 19, 44])
    [4, 8, 17, 19, 19, 32, 44, 65]
    >>> min_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> min_sort([])
    []
    """

    n = len(array)
    
    # Let i iterate over the array from 0 to n-2. Note that for n = 0, range(-1) is the empty set and there are no loop iterations,
    # which is the right thing to do in that case.
    for i in range(n-1):
        
        # Compute the minimum starting from the i-th element.
        min_so_far = array[i]
        min_so_far_index = i
        for j in range(i + 1, n):
            if array[j] < min_so_far:
                min_so_far = array[j]
                min_so_far_index = j
        
        # If the minimum is after the i-th element, swap it with the i-th element.
        if min_so_far_index > i:
            array[i], array[min_so_far_index] = array[min_so_far_index], array[i]
    
    return array


def min_sort_timing():
    """
    Run MinSort for arrays of increasing size. For each size, pick an array
    with the elements in reverse order, so that MinSort actually has something
    to do.
    """
    
    # Iterate over 500, 1000, 1500, ..., 10000.
    for n in range(500, 10001, 500):
        # Array of size n with elements in reverse order.
        array = [k for k in range(n, 0, -1)]
        # Time how long MinSort takes
        start_time = time.monotonic()
        min_sort(array)
        end_time = time.monotonic()
        # Duration in integer milliseconds. Note that time.monotonic() returns
        # the time in seconds, as a floating point number.
        duration = int(round((end_time - start_time) * 1000))
        # Print the size and the time, tab-separated.
        print("%d\t%d" % (n, duration))


if __name__ == "__main__":
    # print(min_sort([17, 4, 32, 19, 8, 65, 19, 44]))
    # print(min_sort([5, 4, 3, 2, 1]))
    # print(min_sort([]))
    min_sort_timing()



