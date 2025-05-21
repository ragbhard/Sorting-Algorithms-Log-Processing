
import time
import psutil

class MetricsCollector:
    def __init__(self):
        self.results = []

    def measure(self, func, data, tracker):
        proc = psutil.Process()
        mem_before = proc.memory_info().rss
        start_time = time.time()

        result = func(data, tracker)

        end_time = time.time()
        mem_after = proc.memory_info().rss

        self.results.append({
            'algorithm': func.__name__,
            'duration_sec': round(end_time - start_time, 4),
            'memory_data_MB': round((mem_after - mem_before) / (1024 * 1024), 4),
            'memory_program_MB': round(proc.memory_info().rss / (1024 * 1024), 4),
            'comparisons': tracker.comparisons,
            'swaps': tracker.swaps
        })
        return result

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
