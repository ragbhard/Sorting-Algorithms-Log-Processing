
def quick_sort(arr, tracker):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if tracker.compare(arr[j], pivot):
                i += 1
                tracker.swap(arr, i, j)
        tracker.swap(arr, i + 1, high)
        return i + 1

    def quicksort_recursive(arr, low, high):
        while low < high:
            pi = partition(arr, low, high)
            if pi - low < high - pi:
                quicksort_recursive(arr, low, pi - 1)
                low = pi + 1
            else:
                quicksort_recursive(arr, pi + 1, high)
                high = pi - 1

    arr = arr.copy()
    quicksort_recursive(arr, 0, len(arr) - 1)
    return arr
