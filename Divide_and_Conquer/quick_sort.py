from math import ceil


def quick_sort_first(array, low, high):
    global count
    if len(array) < 2 or low > high-1:
        return array

    count += high - low - 1
    pivot = low
    i = pivot + 1
    for j in range(i, high):
        if array[j] < array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[pivot], array[i-1] = array[i-1], array[pivot]

    quick_sort_first(array, low, i-1)
    quick_sort_first(array, i, high)


def quick_sort_last(array, low, high):
    global count
    if len(array) < 2 or low >= high-1:
        return array

    array[low], array[high-1] = array[high-1], array[low]

    count += high - low - 1

    pivot = low
    i = pivot + 1
    for j in range(i, high):
        if array[j] < array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[pivot], array[i-1] = array[i-1], array[pivot]

    quick_sort_last(array, low, i-1)
    quick_sort_last(array, i, high)


def quick_sort_median_of_three(array, low, high):
    global count
    if len(array) < 2 or low >= high-1:
        return array

    first = array[low]
    last = array[high-1]
    median = array[ceil((high-low) / 2) - 1 + low]
    if min(first, median) <= last <= max(first, median):
        array[low], array[high-1] = array[high-1], array[low]
    elif min(first, last) <= median <= max(first, last):
        array[low],  array[ceil((high-low) / 2) - 1 + low] = array[ceil((high-low) / 2) - 1 + low], array[low]

    count += high - low - 1

    pivot = low
    i = pivot + 1
    for j in range(i, high):
        if array[j] < array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[pivot], array[i-1] = array[i-1], array[pivot]

    quick_sort_median_of_three(array, low, i-1)
    quick_sort_median_of_three(array, i, high)


