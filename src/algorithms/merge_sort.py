
def merge_sort(arr, tracker):
    def merge(left, right):
        sorted_list = []
        while left and right:
            if tracker.compare(left[0], right[0]):
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        return sorted_list + left + right

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    return sort(arr.copy())
