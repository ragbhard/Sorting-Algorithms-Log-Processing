
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_all_metrics(data, output_dir='reports/plots'):
    if isinstance(data, str):
        df = pd.read_csv(data)
    elif isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise ValueError("Input must be a path to CSV, a list of dicts, or a pandas DataFrame.")

    os.makedirs(output_dir, exist_ok=True)
    sns.set_theme(style="whitegrid")

    def save_plot(metric, ylabel, title, filename):
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x="Algorithm", y=metric, hue="Pattern")
        plt.title(title)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        filepath = os.path.join(output_dir, filename)
        plt.savefig(filepath)
        plt.close()

    save_plot("duration_sec", "Time (seconds)", "Execution Time by Algorithm and Pattern", "time_plot.png")
    save_plot("memory_data_MB", "Memory (MB)", "Data Memory Usage by Algorithm and Pattern", "memory_data_plot.png")
    save_plot("memory_program_MB", "Memory (MB)", "Program Memory Usage by Algorithm and Pattern", "memory_program_plot.png")
    save_plot("comparisons", "Comparisons", "Number of Comparisons by Algorithm and Pattern", "comparisons_plot.png")
    save_plot("swaps", "Swaps", "Number of Swaps by Algorithm and Pattern", "swaps_plot.png")

    print(f"✅ Plots saved in: {output_dir}")
