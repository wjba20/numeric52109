# 3)
"""
Graphics module for simple_package
Provides visualization functions for statistical data
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_histogram_with_stats(data, mean_val, median_val, title="Data Distribution"):
    """
    Plot a histogram of data with mean and median marked.
    
    Parameters:
    data (array-like): Input data
    mean_val (float): Mean value to mark
    median_val (float): Median value to mark
    title (str): Plot title
    
    Returns:
    matplotlib.figure.Figure: The generated figure
    """
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot histogram
    n, bins, patches = ax.hist(data, bins='auto', alpha=0.7, color='skyblue', 
                              edgecolor='black', label='Data Distribution')
    
    # Add vertical lines for mean and median
    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, 
               label=f'Mean: {mean_val:.2f}')
    ax.axvline(median_val, color='green', linestyle='--', linewidth=2, 
               label=f'Median: {median_val:.2f}')
    
    # Customize the plot
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Add some statistics as text
    stats_text = f'Count: {len(data)}\nStd Dev: {np.std(data):.2f}'
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    return fig

def show_plot():
    """Display the current plot."""
    plt.show()

def save_plot(filename='histogram.png'):
    """Save the current plot to a file."""
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved as {filename}")

def close_plot():
    """Close the current plot."""
    plt.close()

# Example usage
if __name__ == "__main__":
    # Demo data
    demo_data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7]
    mean_demo = np.mean(demo_data)
    median_demo = np.median(demo_data)
    
    # Create and display plot
    plot_histogram_with_stats(demo_data, mean_demo, median_demo, "Demo Data")
    show_plot()