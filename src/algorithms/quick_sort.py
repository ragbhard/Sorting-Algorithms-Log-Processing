
def quick_sort(arr, tracker):
    def median_of_three(arr, low, high):
        mid = (low + high) // 2
        if tracker.compare(arr[mid], arr[low]):
            tracker.swap(arr, mid, low)
        if tracker.compare(arr[high], arr[low]):
            tracker.swap(arr, high, low)
        if tracker.compare(arr[high], arr[mid]):
            tracker.swap(arr, high, mid)
        tracker.swap(arr, mid, high)
        return partition(arr, low, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if tracker.compare(arr[j], pivot):
                i += 1
                tracker.swap(arr, i, j)
        tracker.swap(arr, i + 1, high)
        return i + 1

    def quicksort_optimized(arr, low, high):
        while low < high:
            pi = median_of_three(arr, low, high)
            if pi - low < high - pi:
                quicksort_optimized(arr, low, pi - 1)
                low = pi + 1
            else:
                quicksort_optimized(arr, pi + 1, high)
                high = pi - 1

    arr = arr.copy()
    quicksort_optimized(arr, 0, len(arr) - 1)
    return arr
