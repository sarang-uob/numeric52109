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


###
## simple_package - Module statistics.py
## Basic statistics calculations
###

# -------------------------------
# Import necessary packages with checks
# -------------------------------
try:
    import numpy as np
except ImportError:
    raise ImportError("NumPy is required. Please install it with `pip install numpy`.")

try:
    import matplotlib.pyplot as plt
except ImportError:
    # We'll still allow stats functions to work even if plotting is unavailable
    plt = None
    print("Warning: Matplotlib not installed. Plotting functions will not work.")

# -------------------------------
# Basic statistical functions
# -------------------------------

def mean(data):
    """Calculate the mean of the data."""
    data = np.asarray(data)
    return np.mean(data)

def median(data):
    """Calculate the median of the data."""
    data = np.asarray(data)
    return np.median(data)

def std_dev(data):
    """Calculate the standard deviation of the data."""
    data = np.asarray(data)
    return np.std(data)

# -------------------------------
# Pretty-print function
# -------------------------------
def pretty_print_stats(data):
    """
    Display mean, median, and standard deviation with a clear print statement.
    """
    data = np.asarray(data)
    m = mean(data)
    med = median(data)
    sd = std_dev(data)
    
    print("----- Statistics Summary -----")
    print(f"Mean: {m:.2f}")
    print(f"Median: {med:.2f}")
    print(f"Standard Deviation: {sd:.2f}")
    print("------------------------------")

# -------------------------------
# Plotting function (optional)
# -------------------------------
def plot_histogram(data):
    """
    Plot a histogram of the data with mean and median marked.
    Requires matplotlib.
    """
    if plt is None:
        raise ImportError("Matplotlib is not installed. Install it with `pip install matplotlib` to plot histograms.")
    
    data = np.asarray(data)
    m = mean(data)
    med = median(data)
    
    plt.hist(data, bins='auto', alpha=0.7, edgecolor='black')
    plt.axvline(m, color='red', linestyle='--', linewidth=2, label=f"Mean: {m:.2f}")
    plt.axvline(med, color='green', linestyle='--', linewidth=2, label=f"Median: {med:.2f}")
    
    plt.title("Histogram with Mean and Median")
    plt.xlabel("Data values")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

# -------------------------------
# Block for testing the statistics module directly
# -------------------------------
if __name__ == '__main__':
    '''This code snipped runs when the script is executed directly. (For testing purposes)'''
    sample_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    pretty_print_stats(sample_data)
    
    # Plot histogram only if matplotlib is available
    if plt:
        plot_histogram(sample_data)




if __name__ == '__main__':
    '''This code snipped runs when the script is executed directly. (For testing purposes)'''
    sample_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    pretty_print_stats(sample_data)
    
    # Plot histogram only if matplotlib is available
    if plt:
        plot_histogram(sample_data)