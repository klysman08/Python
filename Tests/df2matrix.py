""" Input The input argument is a DataFrame object with five columns: FirstName LastName GradYear and MedianScore. 
The data frame represents the mean and median test scores for various students (where LastNa and GradYear columns represent the first name, last name, 
and graduation year o each contains integers in the set [2021, 2022, 2023].

Output Your df2matrix function should retum a NumPy array containing the numeric representation of the data stored in [PÊ]. Specifically, the NumPy array will have the same number of rows as [PÊ] and five columns. • The rows are not sorted in this initial order must not change. 
• The first column represents the values, while the second column represents the MedianScore values. • The final three columns are indicator columns for the GradYear column, where the third column represents year 2021, the fourth column represents year 2022, and the fifth column represents year 2023. """


import numpy as np
import pandas as pd


def df2matrix(df):
    """
    Converts a DataFrame object to a NumPy array with the specified format.

    Parameters:
    df (pandas.DataFrame): A DataFrame object with five columns: FirstName, LastName,
                           GradYear, and MedianScore.

    Returns:
    numpy.ndarray: A NumPy array containing the numeric representation of the data
                   stored in df with five columns.
    """
    # Create an indicator matrix for the GradYear column
    indicator_matrix = pd.get_dummies(df['GradYear'])

    # Combine the MedianScore column and the indicator matrix into a single DataFrame
    data_matrix = pd.concat([df['MedianScore'], indicator_matrix], axis=1)

    # Convert the DataFrame to a NumPy array
    np_array = data_matrix.to_numpy()

    return np_array
