import sys
import pandas as pd
from calculs import calculateMedian, segmentDataByMedian, calculateDeviation
from read import readData
from write import writeData

def main():
    if len(sys.argv) < 4:
        print("Usage: python job.py <inputFile> <inputFormat> <field> <operation> [<outputFile> <outputFormats...>]")
        return

    inputFile = sys.argv[1]
    inputFormat = sys.argv[2]
    field = sys.argv[3]
    operation = sys.argv[4]

    # Read the data based on input format
    data = readData(inputFile, inputFormat)

    # Check if the operation is 'median', 'segmentByMedian' or 'deviation'
    if operation == 'median':
        # Calculate the median for the specified field
        median = calculateMedian(data, field)
        # Print the median to the console
        print(f"The median of {field} is: {median}")
    elif operation == 'segmentByMedian':
        if len(sys.argv) < 6:
            print("Usage: python job.py <inputFile> <inputFormat> <field> segmentByMedian <outputFile> <outputFormats...>")
            return
        outputFile = sys.argv[5]
        outputFormats = sys.argv[6].split(',')
        # Segment the data by median for the specified field
        segmentedData = segmentDataByMedian(data, field)
        # Write the segmented data to the output file
        writeData(outputFile, outputFormats, segmentedData)
    elif operation == 'deviation':
        if len(sys.argv) < 6:
            print("Usage: python job.py <inputFile> <inputFormat> <field> deviation <outputFile> <outputFormats...>")
            return
        outputFile = sys.argv[5]
        outputFormats = sys.argv[6].split(',')
        # Calculate the deviations from the mean for the specified field
        dfWithDeviation = calculateDeviation(data, field)
        # Write the DataFrame with the new column to the output file
        writeData(outputFile, outputFormats, dfWithDeviation)
    else:
        print("Invalid operation. Please specify 'median', 'segmentByMedian', or 'deviation'.")

if __name__ == "__main__":
    main()
