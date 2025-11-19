###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##

try:
    import numpy as np
except ImportError:
    raise ImportError("NumPy is required for statistics.py, but it is not installed.")

def ensure_array(data):
    """Ensure input is a NumPy array."""
    if isinstance(data, list):
        return np.array(data)
    elif isinstance(data, np.ndarray):
        return data
    else:
        raise TypeError("Input must be a list or numpy array.")


def compute_statistics(data):
    """Return mean, median, std for given data."""
    data = ensure_array(data)

    mean = np.mean(data)
    median = np.median(data)
    std = np.std(data)

    print("\n=== Statistics Summary ===")
    print(f"Mean:   {mean:.4f}")
    print(f"Median: {median:.4f}")
    print(f"Std:    {std:.4f}\n")

    return mean, median, std

def plot_statistics(data):
    """Plot histogram with mean and median using graphics.py."""
    from . import graphics  # import from same package

    data = ensure_array(data)
    mean, median, std = compute_statistics(data)

    graphics.plot_histogram(data, mean, median)
