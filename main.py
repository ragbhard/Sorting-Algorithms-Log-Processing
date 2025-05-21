from src.log_generator.log_generator import LogGenerator
from src.algorithms.quick_sort import quick_sort
from src.algorithms.merge_sort import merge_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.radix_sort import radix_sort
from src.benchmarking.metrics_collector import MetricsCollector, OperationTracker
import pandas as pd
import os

# Configuration
patterns = ['random', 'sorted', 'reverse', 'partial']
algorithms = {
    'Quick Sort': quick_sort,
    'Merge Sort': merge_sort,
    'Heap Sort': heap_sort,
    'Radix Sort': radix_sort
}
entry_count = 10000
repeats = 5
results = []

# Create directories if not exist
os.makedirs("logs", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Run benchmarks
for pattern in patterns:
    print(f"\n--- Pattern: {pattern.upper()} ---")
    
    # Generate log file
    log_file = f"logs/{pattern}_logs.txt"
    LogGenerator().generate_log_file(log_file, entry_count, pattern)

    # Read generated logs
    with open(log_file, 'r') as f:
        original_logs = f.readlines()

    for name, algorithm in algorithms.items():
        print(f"Testing: {name}")
        
        for run in range(repeats):
            logs_copy = original_logs.copy()
            tracker = OperationTracker()
            metrics = MetricsCollector()
            
            # ✅ Proper call to measure()
            sorted_logs = metrics.measure(algorithm, logs_copy, tracker)
            
            # Collect results
            results.append({
                'Algorithm': name,
                'Pattern': pattern,
                'Run': run + 1,
                **metrics.results[-1]  # Get latest recorded result
            })

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("reports/benchmark_results.csv", index=False)
print("\\n✅ Benchmarking complete. Results saved to reports/benchmark_results.csv")

# Generate plots automatically
from src.benchmarking.performance_dashboard import plot_all_metrics
plot_all_metrics("reports/benchmark_results.csv")
