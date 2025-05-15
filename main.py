
from src.algorithms.quick_sort import quick_sort
from src.algorithms.merge_sort import merge_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.radix_sort import radix_sort
from src.log_generator.log_generator import LogGenerator
from src.benchmarking.metrics_collector import MetricsCollector
from src.benchmarking.performance_dashboard import plot_performance

def main():
    # Generate Log File
    generator = LogGenerator()
    generator.generate_log_file("logs.txt", 10000)

    # Sorting Algorithms
    with open("logs.txt") as f:
        logs = f.readlines()
    
    metrics = MetricsCollector()

    # Quick Sort
    logs_copy = logs.copy()
    sorted_logs = metrics.measure(quick_sort)(logs_copy)
    
    # Merge Sort
    logs_copy = logs.copy()
    sorted_logs = metrics.measure(merge_sort)(logs_copy)

    # Heap Sort
    logs_copy = logs.copy()
    sorted_logs = metrics.measure(heap_sort)(logs_copy)

    # Radix Sort
    logs_copy = [int(line.split()[0].replace("-", "").replace(":", "").replace(" ", "")) for line in logs]
    sorted_logs = metrics.measure(radix_sort)(logs_copy)

    # Display Results
    plot_performance(metrics.results)

if __name__ == "__main__":
    main()
