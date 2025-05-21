
def heap_sort(arr, tracker):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and not tracker.compare(arr[l], arr[largest]):
            largest = l
        if r < n and not tracker.compare(arr[r], arr[largest]):
            largest = r
        if largest != i:
            tracker.swap(arr, i, largest)
            heapify(arr, n, largest)

    arr = arr.copy()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        tracker.swap(arr, 0, i)
        heapify(arr, i, 0)
    return arr
