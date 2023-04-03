def selection_sort(array):
    """ Sort array using the SelectionSort algorithm from the lecture.
    >>> selection_sort([5, 1, 3, 8, 4, 18, 0, 8])
    [0, 1, 3, 4, 5, 8, 8, 18]
    
    >>> selection_sort([])
    []
    """
    n = len(array)
    for i in range(n - 1):
        # Find the minimum in array[i .. n-1].
        minPos = i
        for j in range(i+1,n):
            if array[j] < array[minPos]:
                minPos = j
            
        # Swap min to position i 
        array[i], array[minPos] = array[minPos], array[i]
    return array

print(selection_sort([5, 1, 3, 8, 4, 18, 0, 8]))
print(selection_sort([]))