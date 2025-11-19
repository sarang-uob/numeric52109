#graphics.py - file responsible for plotting functions



import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(data):
    """
    Plot a histogram of the data with mean and median marked.
    """

    # Converting the data to a numpy array if it is not already 
    data = np.asarray(data)

    # Compute mean and median
    mean_val = np.mean(data)
    median_val = np.median(data)

    # Create the histogram
    plt.hist(data, bins='auto', alpha=0.7, edgecolor='black')

    # Plot mean and median lines
    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f"Mean: {mean_val:.2f}")
    plt.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f"Median: {median_val:.2f}")

    # Labels and title
    plt.title("Histogram with Mean and Median")
    plt.xlabel("Data values")
    plt.ylabel("Frequency")
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == '__main__':
    '''This code snipped runs when the script is executed directly. (For testing purposes)'''
    sample_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    plot_histogram(sample_data)