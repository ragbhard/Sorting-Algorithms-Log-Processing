
import time
import psutil
import os
import tracemalloc

class OperationTracker:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def compare(self, a, b):
        self.comparisons += 1
        return a < b

    def swap(self, arr, i, j):
        self.swaps += 1
        arr[i], arr[j] = arr[j], arr[i]

    def write(self, arr, index, value):
        self.swaps += 1
        arr[index] = value


class MetricsCollector:
    def __init__(self):
        self.results = []

    def measure(self, func, data, tracker):
        process = psutil.Process(os.getpid())

        tracemalloc.start()
        start_mem_data, _ = tracemalloc.get_traced_memory()

        start_time = time.time()
        func(data, tracker)
        end_time = time.time()

        end_mem_data, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        program_mem_now = process.memory_info().rss  # current RSS snapshot

        self.results.append({
            "duration_sec": round(end_time - start_time, 5),
            "memory_data_MB": round((end_mem_data - start_mem_data) / 1024 / 1024, 5),
            "memory_program_MB": round(program_mem_now / 1024 / 1024, 5),
            "comparisons": tracker.comparisons,
            "swaps": tracker.swaps
        })

        return data
