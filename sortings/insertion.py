def insertion_sort(unsorted):
    if len(unsorted) == 1:
        return unsorted
    for x in range(1,len(unsorted)):
        y = x
        while y >= 1 and unsorted[y-1] > unsorted[y]:
            unsorted[y], unsorted[y-1] = unsorted[y-1], unsorted[y]
            y -= 1

    return unsorted
