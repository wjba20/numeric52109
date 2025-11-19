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

## Functions for basic statistical operations:
try:
    import numpy as np
except ImportError:
    raise ImportError("Error: numpy is required for statistics.py but is not installed.")


def validate_input(data):
    """
    Ensure the input is a numpy array.
    Convert Python lists to numpy arrays.
    Raise an error for invalid types.
    """
    if isinstance(data, list):
        return np.array(data)

    if isinstance(data, np.ndarray):
        return data

    raise TypeError("Input data must be a list or numpy array.")


def calculate_stats(data):
    """
    Calculate the mean, median, and standard deviation of a dataset.
    Returns a dictionary of results.
    """
    data = validate_input(data)

    mean = np.mean(data)
    median = np.median(data)
    std = np.std(data)

    return {
        "mean": mean,
        "median": median,
        "std": std
    }


def print_stats(stats):
    """
    Pretty-print the statistics dictionary.
    """
    print("=== Statistics Summary ===")
    print(f"Mean:   {stats['mean']:.4f}")
    print(f"Median: {stats['median']:.4f}")
    print(f"Std:    {stats['std']:.4f}")
    print("==========================")