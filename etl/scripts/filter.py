import pandas as pd

#Function to filter a DataFrame based on a specific value in a given column.
def filterDataFrameByEqualValue(dataframe, field, value):
    # Convert all values in the specified column to strings
    dataframe[field] = dataframe[field].astype(str)
    # Filter the data based on the value in the specified column
    filteredData = filteredData = dataframe[dataframe[field] == str(value)]
    return filteredData

#Function to filter a DataFrame based on values greater than a specified value in a given column.
def filterDataFrameByGreaterThanValue(dataframe, field, value):
    # Convert all values in the specified column to numbers
    dataframe[field] = pd.to_numeric(dataframe[field], errors='coerce')

    # Convert the value to a number
    value = pd.to_numeric(value, errors='coerce')
    
    # Filter the data based on values greater than the specified value in the specified column
    filteredData = dataframe[dataframe[field] > value]
    
    return filteredData

#Function to filter a DataFrame based on values greater than or equal to a specified value in a given column.
def filterDataFrameByGreaterThanOrEqualToValue(dataframe, field, value):
    # Convert all values in the specified column to numbers
    dataframe[field] = pd.to_numeric(dataframe[field], errors='coerce')
    
    # Convert the value to a number
    value = pd.to_numeric(value, errors='coerce')
    
    # Filter the data based on values greater than or equal to the specified value in the specified column
    filteredData = dataframe[dataframe[field] >= value]
    
    return filteredData

#Function to filter a DataFrame based on values less than a specified value in a given column.
def filterDataFrameByLessThanValue(dataframe, field, value):
    # Convert all values in the specified column to numbers
    dataframe[field] = pd.to_numeric(dataframe[field], errors='coerce')
    
    # Convert the value to a number
    value = pd.to_numeric(value, errors='coerce')
    
    # Filter the data based on values less than the specified value in the specified column
    filteredData = dataframe[dataframe[field] < value]
    
    return filteredData

#Function to filter a DataFrame based on values less than or equal to a specified value in a given column.
def filterDataFrameByLessThanOrEqualToValue(dataframe, field, value):
    # Convert all values in the specified column to numbers
    dataframe[field] = pd.to_numeric(dataframe[field], errors='coerce')
    
    # Convert the value to a number
    value = pd.to_numeric(value, errors='coerce')
    
    # Filter the data based on values less than or equal to the specified value in the specified column
    filteredData = dataframe[dataframe[field] <= value]
    
    return filteredData

#Function to filter a DataFrame to keep only specified fields/columns.
def filterDataFrameByFields(dataframe, fields):
    # Filter the DataFrame to keep only the specified fields
    filteredData = dataframe[fields]
    
    return filteredData
