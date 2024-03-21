import sys
from scripts.calculs import calculateMedian, segmentDataByMedian, calculateDeviation
from scripts.read import readData
from scripts.write import writeData
from scripts.checkAndFormatFile import check_missing_data_and_format_json, check_csv_file_and_format_csv
from scripts.filter import filterDataFrameByEqualValue, filterDataFrameByGreaterThanValue, filterDataFrameByGreaterThanOrEqualToValue, filterDataFrameByLessThanValue, filterDataFrameByLessThanOrEqualToValue, filterDataFrameByFields

def main():
    if len(sys.argv) < 3:
        print("Usage: python job.py <inputFile> <inputFormat> <operation> [<outputFile> <outputFormats...>]")
        return

    inputFile = sys.argv[1]
    inputFormat = sys.argv[2]
    operation = sys.argv[3]

    # Read the data based on input format
    data = readData(inputFile, inputFormat)

    # Check if the operation is 'median', 'segmentByMedian' or 'deviation'
    if operation == 'median':
        if len(sys.argv) < 4:
            print("Usage: python job.py <inputFile> <inputFormat> <field> <operation> [<outputFile> <outputFormats...>]")
            return
        field = sys.argv[4]
        # Calculate the median for the specified field
        median = calculateMedian(data, field)
        # Print the median to the console
        print(f"The median of {field} is: {median}")
    elif operation == 'segmentByMedian':
        if len(sys.argv) < 6:
            print("Usage: python job.py <inputFile> <inputFormat> <field> segmentByMedian <outputFile> <outputFormats...>")
            return
        field = sys.argv[4]
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
        field = sys.argv[4]
        outputFile = sys.argv[5]
        outputFormats = sys.argv[6].split(',')
        # Calculate the deviations from the mean for the specified field
        dfWithDeviation = calculateDeviation(data, field)
        # Write the DataFrame with the new column to the output file
        writeData(outputFile, outputFormats, dfWithDeviation)
    elif operation == 'formatJson':
        if len(sys.argv) < 5:
            print("Usage: python job.py <inputFile> <inputFormat> <field> deviation <outputFile> <outputFormats...>")
            return
        outputFile = sys.argv[4]
        outputFormats = sys.argv[5].split(',')

        formattedDatas = check_missing_data_and_format_json(data)
        writeData(outputFile, outputFormats, formattedDatas)
    elif operation == "formatCsv":
        if len(sys.argv) < 5:
            print("Usage: python job.py <inputFile> <inputFormat> <field> deviation <outputFile> <outputFormats...>")
            return
        outputFile = sys.argv[4]
        outputFormats = sys.argv[5].split(',')
        
        formattedDatas = check_csv_file_and_format_csv(data)
        writeData(outputFile, outputFormats, formattedDatas)
    elif operation == "filterEqual":
        if len(sys.argv) < 7:
            print("Usage: python job.py <inputFile> <inputFormat> <field> deviation <outputFile> <outputFormats...>")
            return
        field = sys.argv[4]
        value = sys.argv[5]
        outputFile = sys.argv[6]
        outputFormats = sys.argv[7].split(',')

        filtredDatas = filterDataFrameByEqualValue(data, field, value)
        writeData(outputFile, outputFormats, filtredDatas)
    elif operation == "filterGreater":
        if len(sys.argv) < 7:
            print("Usage: python job.py <inputFile> <inputFormat> <field> deviation <outputFile> <outputFormats...>")
            return
        field = sys.argv[4]
        value = sys.argv[5]
        outputFile = sys.argv[6]
        outputFormats = sys.argv[7].split(',')

        filtredDatas = filterDataFrameByGreaterThanValue(data, field, value)
        writeData(outputFile, outputFormats, filtredDatas)
    elif operation == "filterGreaterOrEqual":
        if len(sys.argv) < 7:
            print("Usage: python job.py <inputFile> <inputFormat> <field> deviation <outputFile> <outputFormats...>")
            return
        field = sys.argv[4]
        value = sys.argv[5]
        outputFile = sys.argv[6]
        outputFormats = sys.argv[7].split(',')

        filtredDatas = filterDataFrameByGreaterThanOrEqualToValue(data, field, value)
        writeData(outputFile, outputFormats, filtredDatas)
    elif operation == "filterLess":
        if len(sys.argv) < 7:
            print("Usage: python job.py <inputFile> <inputFormat> <field> deviation <outputFile> <outputFormats...>")
            return
        field = sys.argv[4]
        value = sys.argv[5]
        outputFile = sys.argv[6]
        outputFormats = sys.argv[7].split(',')

        filtredDatas = filterDataFrameByLessThanValue(data, field, value)
        writeData(outputFile, outputFormats, filtredDatas)
    elif operation == "filterLessOrEqual":
        if len(sys.argv) < 7:
            print("Usage: python job.py <inputFile> <inputFormat> <field> deviation <outputFile> <outputFormats...>")
            return
        field = sys.argv[4]
        value = sys.argv[5]
        outputFile = sys.argv[6]
        outputFormats = sys.argv[7].split(',')

        filtredDatas = filterDataFrameByLessThanOrEqualToValue(data, field, value)
        writeData(outputFile, outputFormats, filtredDatas)
    elif operation == "filterByFields":
        if len(sys.argv) < 6:
            print("Usage: python job.py <inputFile> <inputFormat> <field> deviation <outputFile> <outputFormats...>")
            return
        fields = sys.argv[4].split(',')
        outputFile = sys.argv[5]
        outputFormats = sys.argv[6].split(',')

        filtredDatas = filterDataFrameByFields(data, fields)
        writeData(outputFile, outputFormats, filtredDatas)
    else:
        print("Invalid operation. Please specify 'median', 'segmentByMedian', or 'deviation'.")

if __name__ == "__main__":
    main()
