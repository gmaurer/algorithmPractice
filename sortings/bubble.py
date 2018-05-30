
def bubble_sort(unsorted):
    #assuming unsorted is an array
    l = len(unsorted)
    sort = False
    count = 0
    if l == 1:
        return unsorted
    while sort is False:
        count = 0
        for i in range(0,len(unsorted)-1):
            if unsorted[i+1] < unsorted[i]:
                temp = unsorted[i]
                unsorted[i] = unsorted[i+1]
                unsorted[i+1] = temp
                count += 1
        if count == 0:
            sort = True

    return unsorted
