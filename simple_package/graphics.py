###
## simple_package - Module graphics.py
## Plotting histograms with mean and median
###

# Try importing matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Matplotlib is required for graphics.py but is not installed.")


def plot_histogram(data, mean=None, median=None, bins=10, title="Histogram"):
    """
    Plot a histogram of the data with optional mean and median lines.

    Parameters:
    - data: numpy array or list of numbers
    - mean: float (optional) mean of data
    - median: float (optional) median of data
    - bins: int, number of histogram bins
    - title: str, plot title
    """

    # Convert list to numpy array if needed
    try:
        import numpy as np
        if isinstance(data, list):
            data = np.array(data)
    except ImportError:
        raise ImportError("NumPy is required to process the data in graphics.py")

    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=bins, color="skyblue", edgecolor="black")
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    # Draw mean line if provided
    if mean is not None:
        plt.axvline(mean, color="red", linestyle="dashed", linewidth=2, label=f"Mean = {mean:.2f}")

    # Draw median line if provided
    if median is not None:
        plt.axvline(median, color="green", linestyle="dashed", linewidth=2, label=f"Median = {median:.2f}")

    if mean is not None or median is not None:
        plt.legend()

    plt.show()
