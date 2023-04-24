def merge_sort(lst):
    """
    Sorts the input list lst using the iterative merge sort algorithm.

    Args:
    lst: A list of comparable elements.

    Returns:
    A sorted list.

    """
    if len(lst) <= 1:
        return lst

    # Split the list into two halves
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # Sort the two halves recursively
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the two sorted halves
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result


print(merge_sort([1, 4, 2, 3]))