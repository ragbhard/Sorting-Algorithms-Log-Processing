
import matplotlib.pyplot as plt

def plot_performance(results):
    functions = [r['function'] for r in results]
    durations = [r['duration_sec'] for r in results]
    memory_usage = [r['memory_used_MB'] for r in results]

    plt.figure(figsize=(10, 5))
    plt.bar(functions, durations, color='skyblue')
    plt.title('Algorithm Performance - Time (Seconds)')
    plt.ylabel('Time (s)')
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(functions, memory_usage, color='lightgreen')
    plt.title('Algorithm Performance - Memory Usage (MB)')
    plt.ylabel('Memory (MB)')
    plt.show()
