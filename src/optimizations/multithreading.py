
from threading import Thread

def threaded_sort(arr, sort_fn):
    def sort_task(data):
        sort_fn(data)

    threads = [Thread(target=sort_task, args=(chunk,)) for chunk in arr]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
