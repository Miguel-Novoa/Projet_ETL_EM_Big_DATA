import pandas as pd

def check_csv_file_and_format_csv(data):
    # Function to check for missing values and format the data
    def recursive_check_and_format(obj, current_path=[]):
        missing_data_count = 0

        for column in obj.columns:
            current_path.append(column)
            if obj[column].isnull().any() or (obj[column] == "").any():
                print(f"Missing value in column '{'.'.join(current_path)}'")
                column_missing_data = obj[column].isnull().sum() + (obj[column] == "").sum()
                missing_data_count += column_missing_data
                print("Number of missing values:", column_missing_data)
                # Replace empty strings with None
                obj[column] = obj[column].replace("", None)

            current_path.pop()

        return missing_data_count

    missing_data_count = recursive_check_and_format(data)
    
    if missing_data_count > 0:
        print(f"There are {missing_data_count} missing values in the CSV file.")
    else:
        print("No missing values in the CSV file.")

    return data

def check_missing_data_and_format_json(data):
    # Function to check for missing values and format the data
    def recursive_check_and_format(obj, current_path=[]):
        missing_data_count = 0

        for column in obj.columns:
            current_path.append(column)
            if obj[column].isnull().any() or (obj[column] == "").any():
                print(f"Missing value in column '{'.'.join(current_path)}'")
                column_missing_data = obj[column].isnull().sum() + (obj[column] == "").sum()
                missing_data_count += column_missing_data
                print("Number of missing values:", column_missing_data)
                # Replace empty strings with quotes
                obj[column] = obj[column].fillna('""').replace("", None)

                # Convert strings containing 'true' or 'false' to boolean
                if obj[column].dtype == 'object':
                    obj[column] = obj[column].apply(lambda x: True if isinstance(x, str) and x.lower() == 'true' else (False if isinstance(x, str) and x.lower() == 'false' else x))

            current_path.pop()

        return missing_data_count

    missing_data_count = recursive_check_and_format(data)
    
    if missing_data_count > 0:
        print(f"There are {missing_data_count} missing values in the JSON file.")
        return data
    else:
        print("No missing values in the JSON file.")
        return data
