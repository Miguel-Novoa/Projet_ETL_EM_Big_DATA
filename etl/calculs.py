import pandas as pd

import pandas as pd

def calculateMedian(data, fieldName):
    """
    Calculate the median of a specific field in the data.

    Args:
        data (DataFrame): The input data.
        fieldName (str): The name of the field for which to calculate the median.

    Returns:
        float: The median value of the specified field.
    """
    # Convert the values of the field to numeric, replacing non-numeric values with NaN
    data[fieldName] = pd.to_numeric(data[fieldName], errors='coerce')

    # Calculate the median, excluding NaN values
    median = data[fieldName].median(skipna=True)

    return median

