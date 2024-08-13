def partition(array, low, high):
    pivot = array[high]

    pointer = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            pointer += 1
            (array[pointer], array[j]) = (array[j], array[pointer])
    (array[pointer + 1], array[high]) = (array[high], array[pointer + 1])

    return pointer + 1

def quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)


array = [10, 7, 8, 9, 1, 5]
N = len(array)

quicksort(array, 0, N-1)