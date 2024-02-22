import sys
from calculs import calculateMedian
from read import readData

def main():
    if len(sys.argv) < 5:
        print("Usage: python job.py <inputFile> <inputFormat> <field> <operation>")
        return

    inputFile = sys.argv[1]
    inputFormat = sys.argv[2]
    field = sys.argv[3]
    operation = sys.argv[4]

    # Read data based on input format
    data = readData(inputFile, inputFormat)

    # Check if the operation is 'median'
    if operation == 'median':
        # Calculate median for the specified field
        median = calculateMedian(data, field)
        # Print the median to the console
        print(f"The median of {field} is: {median}")
    else:
        print("Invalid operation. Please specify 'median'.")

if __name__ == "__main__":
    main()
