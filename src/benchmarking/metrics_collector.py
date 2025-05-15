
import time
import psutil

class MetricsCollector:
    def __init__(self):
        self.results = []

    def measure(self, func):
        def wrapper(*args, **kwargs):
            proc = psutil.Process()
            mem_before = proc.memory_info().rss
            start_time = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            mem_after = proc.memory_info().rss
            self.results.append({
                'function': func.__name__,
                'duration_sec': duration,
                'memory_used_MB': (mem_after - mem_before) / (1024 * 1024)
            })
            return result
        return wrapper
