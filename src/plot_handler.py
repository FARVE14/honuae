"""

"""

__author__ = "Faisal Ahmed"

import matplotlib.pyplot as plt
from pathlib import Path

def calculate_time_parameters(time_array: list[float]) -> dict:
    """

    """
    valid_times = [t for t in time_array if t is not None]
    mean_time = sum(valid_times) / len(valid_times) if valid_times else 0
    max_time = max(valid_times) if valid_times else 0
    min_time = min(valid_times) if valid_times else 0

    return {
        "valid_times": valid_times,
        "mean_time": mean_time,
        "max_time": max_time,
        "min_time": min_time
    }

def plot_results(load_times: list[float], host_url: str, output_graph_path: bool | str = False) -> dict:
    """

    """
    time_parameters = calculate_time_parameters(load_times)
    mean_time = time_parameters.get("mean_time", 0)
    if output_graph_path:
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, len(load_times) + 1), load_times, marker='o', color='blue')
        plt.axhline(y=mean_time, color='red', linestyle='--', label=f'Mean = {mean_time:.2f}s')
        plt.title(f"Browser Load Time Test for {host_url}")
        plt.xlabel("Attempt Number")
        plt.ylabel("Load Time (seconds)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        # plt.show()
        plt.savefig(output_graph_path)
        print(f"\nMean Load Time: {mean_time:.2f} seconds")
    return time_parameters
