def merge(lst, left, middle, right):
    left_part = lst[left:middle]
    right_part = lst[middle:right]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            lst[k] = left_part[i]
            i += 1
        else:
            lst[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        lst[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        lst[k] = right_part[j]
        j += 1
        k += 1

