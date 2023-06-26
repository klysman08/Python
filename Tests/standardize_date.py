""" Input The input argument (arr) is a 2-D NumPy array containing floating-point numbers. An example input would look like this: """

""" Output Your standardize data function will return arr with each of its rows standardized. Specifically, for a row of values: """




import numpy as np
def standardize_data(arr):
    """
    Standardizes each row of a 2-D NumPy array.

    Parameters:
    arr (numpy.ndarray): A 2-D NumPy array containing floating-point numbers.

    Returns:
    numpy.ndarray: The input array with each of its rows standardized.
    """
    # Calculate the mean and standard deviation of each row
    row_means = np.mean(arr, axis=1)
    row_stdevs = np.std(arr, axis=1)

    # Subtract the mean and divide by the standard deviation for each row
    standardized_arr = (
        arr - row_means[:, np.newaxis]) / row_stdevs[:, np.newaxis]

    return standardized_arr


""" Test with arr = np.array([
    [1.2, -0.3, 1.3],
    [1.2, 2., 0.3]
]).astype(np.float64)
 """
arr = np.array([
    [1.2, -0.3, 1.3],
    [1.2, 2., 0.3]
]).astype(np.float64)
print(standardize_data(arr))
