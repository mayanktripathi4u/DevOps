import pandas as pd

# Define the expected columns and their data types
EXPECTED_COLUMNS = {
    'Name': 'object',
    'Age': 'int64',
    'Email': 'object',
    'salary': 'float64',
}

def validate_excel_file(file_path):
    print(f"Received file as {file_path}")
    # Determine the engine based on the file extension
    if file_path.endswith('.xlsx'):
        print("Selecting engine as openpyxl")
        engine = 'openpyxl'
    elif file_path.endswith('.xls'):
        print("Selecting engine as xlrd")
        engine = 'xlrd'
    else:
        print(f"Unsupported file format: {file_path}")
        return
    
    # Load the Excel file into a DataFrame
    try:
        # df = pd.read_excel(file_path)
        df = pd.read_excel(file_path, engine=engine)
        print(df.head())
        print(df.info())
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return

    # Validate columns
    columns = df.columns
    expected_columns_set = set(EXPECTED_COLUMNS.keys())
    actual_columns_set = set(columns)

    if expected_columns_set != actual_columns_set:
        print(f"Column names do not match. Expected columns: {expected_columns_set}, Found columns: {actual_columns_set}")
        return

    # Validate data types
    for column, expected_dtype in EXPECTED_COLUMNS.items():
        if column in df.columns:
            actual_dtype = str(df[column].dtype)
            if actual_dtype != expected_dtype:
                print(f"Data type for column '{column}' does not match. Expected: {expected_dtype}, Found: {actual_dtype}")
                return
        else:
            print(f"Column '{column}' is missing from the file.")
            return

    print("File validation passed successfully.")

# Example usage
file_path = 'Sample_Test.xlsx'
validate_excel_file(file_path)

print("------------------------ Calling Another File")
# Example usage
file_path = 'Sample_Test_1.xlsx'
validate_excel_file(file_path)