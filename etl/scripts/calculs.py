import pandas as pd

#Calculate the median of a specific field in the data.
def calculateMedian(data, fieldName):
    # Convert the values of the field to numeric, replacing non-numeric values with NaN
    data[fieldName] = pd.to_numeric(data[fieldName], errors='coerce')

    # Calculate the median, excluding NaN values
    median = data[fieldName].median(skipna=True)

    return median

def calculateDeviation(data, field):
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if the specified field is present in the DataFrame
    if field not in df.columns:
        raise ValueError(f"The field '{field}' is not present in the data.")
    
    # Calculate the mean of the specified field
    mean = df[field].mean()
    
    # Calculate the deviations from the mean and add a new column to the DataFrame
    df['Deviation from Mean'] = df[field] - mean
    
    # Round the values in the 'Deviation from Mean' column to two decimal places
    df['Deviation from Mean'] = df['Deviation from Mean'].round(2)
    
    # Ensure that the result is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("calculateDeviation did not return a DataFrame.")
    
    return df

def segmentDataByMedian(data, fieldName):
    # Calculate the median
    median = calculateMedian(data, fieldName)
    newName = fieldName + 'MedianComparison'

    # Create a new column to store the groups
    data[newName] = None

    # Assign values to groups based on their proximity to the median
    data.loc[data[fieldName] < median, newName] = 'Below Median'
    data.loc[data[fieldName] == median, newName] = 'Equal to Median'
    data.loc[data[fieldName] > median, newName] = 'Above Median'

    return data
