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

#1)

def mean(data):
    """
    Calculate the mean (average) of the input data.
    
    Parameters:
    data (list): List of numbers
    
    Returns:
    float: Mean value
    
    Raises:
    ValueError: If data list is empty
    TypeError: If data contains non-numeric values
    """

    data_validated = validate_and_convert_data(data)

    if not data:
        raise ValueError("Cannot calculate mean of empty list")
    
    try:
        return sum(data_validated) / len(data_validated)
    except TypeError:
        raise TypeError("All elements in data must be numeric")

def median(data):
    """
    Calculate the median (middle value) of the input data.
    
    Parameters:
    data (list): List of numbers
    
    Returns:
    float: Median value
    
    Raises:
    ValueError: If data list is empty
    TypeError: If data contains non-numeric values
    """

    data_validated = validate_and_convert_data(data)

    if not data_validated:
        raise ValueError("Cannot calculate median of empty list")
    
    try:
        sorted_data = sorted(data_validated)
        n = len(sorted_data)
        mid = n // 2
        
        if n % 2 == 0:
            # Even number of elements - average two middle values
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            # Odd number of elements - return middle value
            return sorted_data[mid]
    except TypeError:
        raise TypeError("All elements in data must be numeric")

def standard_deviation(data, sample=True):
    """
    Calculate the standard deviation of the input data.
    
    Parameters:
    data (list): List of numbers
    sample (bool): If True, calculate sample standard deviation (N-1)
                   If False, calculate population standard deviation (N)
    
    Returns:
    float: Standard deviation
    
    Raises:
    ValueError: If data list has fewer than 2 elements
    TypeError: If data contains non-numeric values
    """

    data_validated = validate_and_convert_data(data)

    if len(data_validated) < 2:
        raise ValueError("At least two data points required for standard deviation")
    
    try:
        # Calculate mean
        mean_val = mean(data_validated)
        
        # Calculate variance
        variance = sum((x - mean_val) ** 2 for x in data_validated)
        
        # Divide by N-1 for sample, N for population
        if sample:
            variance /= (len(data_validated) - 1)
        else:
            variance /= len(data_validated)
        
        # Standard deviation is square root of variance
        return variance ** 0.5
        
    except TypeError:
        raise TypeError("All elements in data must be numeric")
    
# 2)
def pretty_print_stats(data, title="Statistical Summary"):
    """
    Display statistical results with clear and pretty formatting.
    
    Parameters:
    data (list): Input data
    title (str): Title for the summary
    
    Returns:
    None: Prints formatted output to console
    """
    try:
        # Calculate all statistics
        mean_val = mean(data)
        median_val = median(data)
        std_sample = standard_deviation(data, sample=True)
        std_population = standard_deviation(data, sample=False)
        
        # Pretty print formatting
        print("╔" + "═" * 58 + "╗")
        print("║" + f"{title:^58}" + "║")
        print("╠" + "═" * 58 + "╣")
        print("║ {:<25} {:>30} ║".format("Count:", len(data)))
        print("║ {:<25} {:>30.4f} ║".format("Mean:", mean_val))
        print("║ {:<25} {:>30.4f} ║".format("Median:", median_val))
        print("║ {:<25} {:>30.4f} ║".format("Sample Std Dev:", std_sample))
        print("║ {:<25} {:>30.4f} ║".format("Population Std Dev:", std_population))
        print("║ {:<25} {:>30.4f} ║".format("Minimum:", min(data)))
        print("║ {:<25} {:>30.4f} ║".format("Maximum:", max(data)))
        print("║ {:<25} {:>30.4f} ║".format("Range:", max(data) - min(data)))
        print("╚" + "═" * 58 + "╝")
        
    except Exception as e:
        print(f"Error generating statistics: {e}")

def describe_data(data):
    """
    Generate a comprehensive statistical summary of the data.
    
    Parameters:
    data (list): Input data
    
    Returns:
    dict: Dictionary containing all statistical measures
    """
    return {
        'count': len(data),
        'mean': mean(data),
        'median': median(data),
        'std_dev_sample': standard_deviation(data, sample=True),
        'std_dev_population': standard_deviation(data, sample=False),
        'min': min(data),
        'max': max(data),
        'range': max(data) - min(data)
    }

def simple_print_stats(data):
    """
    Simple formatted output for quick statistics.
    
    Parameters:
    data (list): Input data
    """
    try:
        stats = describe_data(data)
        
        print("\n" + "=" * 40)
        print("QUICK STATISTICS")
        print("=" * 40)
        print(f"Data points: {stats['count']}")
        print(f"Mean:        {stats['mean']:.4f}")
        print(f"Median:      {stats['median']:.4f}")
        print(f"Std Dev:     {stats['std_dev_sample']:.4f} (sample)")
        print(f"Range:       {stats['min']:.4f} to {stats['max']:.4f}")
        print("=" * 40)
        
    except Exception as e:
        print(f"Error: {e}")


# 4)
def validate_and_convert_data(data):
    """
    Validate input data and convert to numpy array if needed.
    
    Parameters:
    data: Input data (list, tuple, or numpy array)
    
    Returns:
    numpy.ndarray or list: Validated data (numpy array if available, else original list)
    
    Raises:
    TypeError: If data is not a list, tuple, or numpy array
    ValueError: If data is empty or contains non-numeric values
    """
    # Check input type
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input data must be a list or tuple")
    
    # Check if data is empty
    if len(data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Try to convert to numpy array (will handle numeric validation)
    try:
        import numpy as np
        data_array = np.array(data, dtype=float)
        return data_array
    except ImportError:
        # Fallback to pure Python if numpy not available
        # Validate that all elements are numeric
        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("All elements in data must be numeric")
        return data  # Return as-is for pure Python processing
    except (ValueError, TypeError):
        raise ValueError("All elements in data must be numeric")
    

# 5)
def check_dependencies():
    """
    Check if required packages (numpy, matplotlib) are installed.
    
    Returns:
    tuple: (numpy_available, matplotlib_available)
    
    Raises:
    ImportError: With helpful message if packages are missing
    """
    numpy_available = True
    matplotlib_available = True
    missing_packages = []
    
    # Check numpy
    try:
        import numpy as np
    except ImportError:
        numpy_available = False
        missing_packages.append("numpy")
    
    # Check matplotlib
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        matplotlib_available = False
        missing_packages.append("matplotlib")
    
    # Provide helpful error message if packages are missing
    if missing_packages:
        packages_str = ", ".join(missing_packages)
        print(f"Warning: The following packages are not installed: {packages_str}")
        print("Some features may not work properly.")
        print("Install missing packages with: pip install " + " ".join(missing_packages))
        print()
    
    return numpy_available, matplotlib_available

def validate_and_convert_data(data):
    """
    Validate input data and convert to numpy array if needed.
    
    Parameters:
    data: Input data (list, tuple, or numpy array)
    
    Returns:
    numpy.ndarray or list: Validated data (numpy array if available, else original list)
    
    Raises:
    TypeError: If data is not a list, tuple, or numpy array
    ValueError: If data is empty or contains non-numeric values
    """
    # Check input type
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input data must be a list or tuple")
    
    # Check if data is empty
    if len(data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Check dependencies first
    numpy_available, _ = check_dependencies()
    
    # Try to convert to numpy array if available
    if numpy_available:
        try:
            import numpy as np
            data_array = np.array(data, dtype=float)
            return data_array
        except (ValueError, TypeError):
            raise ValueError("All elements in data must be numeric")
    else:
        # Fallback to pure Python if numpy not available
        # Validate that all elements are numeric
        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("All elements in data must be numeric")
        return data  # Return as-is for pure Python processing    


    