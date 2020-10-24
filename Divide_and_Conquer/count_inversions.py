def sorted_inversions(array):
    if len(array) <= 1:
        return 0, array

    n = len(array)//2
    array_left = array[:n]
    array_right = array[n:]

    count_left, left_sorted = sorted_inversions(array_left)
    count_right, right_sorted = sorted_inversions(array_right)

    i = 0
    j = 0
    k = 0
    n_new = len(left_sorted) + len(right_sorted)
    new_array = [0 for _ in range(n_new)]
    count = 0
    while i < len(left_sorted) and j < len(right_sorted):
        # print(i, j, k)
        if left_sorted[i] < right_sorted[j]:
            new_array[k] = left_sorted[i]
            i += 1
            k += 1
        else:
            new_array[k] = right_sorted[j]
            count = count + len(left_sorted) - i
            j += 1
            k += 1

    while i < len(left_sorted):
        new_array[k] = left_sorted[i]
        i += 1
        k += 1

    while j < len(right_sorted):
        new_array[k] = right_sorted[j]
        j += 1
        k += 1

    return count_right + count_left + count, new_array