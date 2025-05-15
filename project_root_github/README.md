
# Comparative Analysis of Sorting Algorithms for Large-Scale Log File Processing

## 📌 Project Overview
This project provides a complete solution for sorting large-scale log files using four optimized sorting algorithms:
- Quick Sort (Optimized with Median-of-Three Pivot Selection)
- Merge Sort (External Sorting for large files)
- Heap Sort (Memory-Efficient In-Place Sorting)
- Radix Sort (Timestamp-Optimized Sorting)

The project includes a fully modular codebase with components for log generation, sorting, benchmarking, and performance visualization.

---

## 📁 Project Directory Structure

```
project_root/
│
├── src/
│   ├── algorithms/          # Sorting Algorithm Implementations
│   │   ├── quick_sort.py
│   │   ├── merge_sort.py
│   │   ├── heap_sort.py
│   │   └── radix_sort.py
│   │
│   ├── log_generator/       # Log File Generator
│   │   └── log_generator.py
│   │
│   ├── benchmarking/        # Benchmarking and Metrics Collection
│   │   ├── metrics_collector.py
│   │   └── performance_dashboard.py
│   │
│   ├── optimizations/       # Advanced Optimizations
│   │   ├── multithreading.py
│   │   ├── memory_pool.py
│   │   └── circular_buffer.py
│   │
│   └── stream_processing/   # Efficient Log File Stream Processing
│       └── log_stream_processor.py
│
├── reports/                 # Benchmark Results Storage
│   └── benchmark_results.csv
│
└── main.py                  # Main Program - Complete Workflow
```

---

## 🚀 Features
- Four optimized sorting algorithms with clear modular implementation.
- Synthetic log file generation (Random, Time-sequential, Mixed, Partially Sorted).
- Benchmarking framework with CPU, Memory, and Time metrics collection.
- Multi-threaded sorting using Python threads.
- Advanced memory management with Circular Buffer and Memory Pool.
- Real-time performance visualization with matplotlib.

---

## ⚡ Getting Started

### Prerequisites
- Python 3.11+
- Libraries: matplotlib, psutil

```bash
pip install matplotlib psutil
```

### Running the Project
1. Clone the Repository (or unzip the provided folder).
2. Navigate to the project root.
3. Run the main program:
   ```bash
   python main.py
   ```

### Expected Output
- Synthetic log file (logs.txt) will be generated.
- All four sorting algorithms will be applied and benchmarked.
- Performance metrics will be displayed using a graphical dashboard.

---

## 💡 Usage Examples

### Example: Generating Logs
```python
from src.log_generator.log_generator import LogGenerator

gen = LogGenerator()
gen.generate_log_file("logs.txt", 10000)  # Generates a 10,000 entry log file
```

### Example: Running Sorting Algorithms
```python
from src.algorithms.quick_sort import quick_sort

logs = ["2025-05-14 12:34:56 [INFO] Sample log"]
sorted_logs = quick_sort(logs)
```

### Example: Visualizing Performance
```python
from src.benchmarking.performance_dashboard import plot_performance

# Example results data
results = [
    {'function': 'Quick Sort', 'duration_sec': 0.51, 'memory_used_MB': 15.2},
    {'function': 'Merge Sort', 'duration_sec': 1.32, 'memory_used_MB': 25.8}
]
plot_performance(results)
```

---

## ⚡ Contributing
Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
