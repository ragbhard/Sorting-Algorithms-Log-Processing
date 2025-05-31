
def radix_sort(arr, tracker):
    arr = [int(''.join(filter(str.isdigit, line.split()[0]))) for line in arr]
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp, tracker)
        exp *= 10
    return arr

def counting_sort(arr, exp, tracker):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        position = count[index] - 1
        tracker.write(output, position, arr[i])  # count this as a write operation
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
