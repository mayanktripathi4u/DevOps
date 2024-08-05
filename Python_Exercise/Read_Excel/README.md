# Read Excel File and Validate
To perform file and data validation on an Excel file in Python, you can use the pandas library to read the Excel file and validate its structure. Below is a step-by-step guide along with the code to:

1. Read the Excel file.
2. Validate the number of columns and column names.
3. Validate the data types of each column.
4. Stop processing if any validation fails.

Here’s a detailed Python script to accomplish these tasks:

# Python Code for Validation
[main.py](/DevOps/Python_Exercise/Read_Excel/main.py)

# Explanation:
1. Define Expected Columns and Data Types:
* EXPECTED_COLUMNS is a dictionary where keys are the expected column names and values are the expected data types ('string' for object type and 'int64' for integer).
2. Load the Excel File:
* Use pd.read_excel(file_path) to load the Excel file into a DataFrame. Handle any exceptions that occur during file reading.
3. Validate Column Names:
* Check if the actual column names in the DataFrame match the expected column names. Print a message if there is a mismatch and stop further processing.
4. Validate Data Types:
* Check if the data types of the columns match the expected data types. Print a message if there is a mismatch and stop further processing.
5. Run Validation:
* Call the validate_excel_file function with the path to your Excel file.

## Notes:
* Column Data Types in Pandas:
    * Pandas column types might not exactly match the expected data types due to automatic type inference. For example, you might need to check for 'object' type for strings and 'int64' for integers.
    * Adjust the EXPECTED_COLUMNS dictionary if your actual column types differ.
* Error Handling:
  * Add more sophisticated error handling if needed, especially if dealing with large or complex files.

This script will ensure that the Excel file matches the expected structure and data types before proceeding with any further processing.

# Run the Script.


# If Scripts fail
If you ran into issue, and the error message "Excel file format cannot be determined, you must specify an engine manually" typically occurs when Pandas is unable to automatically determine the correct engine to use for reading the Excel file. This can happen with certain file formats or extensions.

To resolve this issue, you can explicitly specify the engine to use when reading the Excel file. Pandas supports two engines for reading Excel files:

1. openpyxl: For .xlsx files.
2. xlrd: For .xls files.

## Steps to Fix the Issue
1. Install the Required Libraries:

Make sure you have the required libraries installed. You can install them using pip:
```
pip install openpyxl xlrd
```
2. Specify the Engine in pd.read_excel:
Depending on the file extension, specify the appropriate engine. Here’s how to modify the code to include engine specifications:

Add the below code in "main.py".
```
# Determine the engine based on the file extension
    if file_path.endswith('.xlsx'):
        engine = 'openpyxl'
    elif file_path.endswith('.xls'):
        engine = 'xlrd'
    else:
        print(f"Unsupported file format: {file_path}")
        return
    
    # Load the Excel file into a DataFrame
    try:
        df = pd.read_excel(file_path, engine=engine)
    except Exception as e:
```

## Explanation:
1. Determine Engine Based on File Extension:
The code snippet checks the file extension to determine whether to use openpyxl (for .xlsx files) or xlrd (for .xls files).
2. Specify the Engine in pd.read_excel:
Pass the determined engine to the engine parameter in pd.read_excel.
3. Handle Unsupported File Formats:
The script prints an error message if the file format is unsupported.
## Additional Tips:
* For .xlsx Files: Use openpyxl as it is the default engine for this file type in recent versions of Pandas.
* For .xls Files: Use xlrd, but be aware that recent versions of xlrd may not support .xls files anymore. In such cases, you might need to use openpyxl or pyxlsb for different types of Excel files.

By specifying the engine explicitly, you should be able to resolve the issue and successfully read the Excel file.


# Get the Column and its Data Type from DataFrame
To get the columns and their data types from a Pandas DataFrame, you can use the DataFrame.dtypes attribute. This attribute returns a Series where the index represents the column names, and the values represent the data types of those columns.

Here's a step-by-step guide on how to retrieve and display the columns and their data types from a DataFrame:

[Sample Code](/DevOps/Python_Exercise/Read_Excel/get_df_column_type.py)

## Explanation
* Create a DataFrame:
  * In this example, a DataFrame df is created from a dictionary data.
* Get Columns and Data Types:   
  * Use df.dtypes to retrieve a Series where the index is the column names and the values are the data types.
* Display the Results:
  * Iterate over the items of the Series and print each column's name and its data type.
## Example Output
For the example DataFrame provided, the output will be:
```
Columns and their data types:
Column 'Name': Data type 'object'
Column 'Age': Data type 'int64'
Column 'Email': Data type 'object'
```
**Notes**

* Data Types: In Pandas, common data types include:
    * int64 for integers
    * float64 for floating-point numbers
    * object for string (text) data
    * datetime64 for date and time data
* Data Type Mapping: If you need to map Pandas data types to more generic or specific types (like mapping object to string), you can customize the output formatting.

This approach can be applied to any DataFrame to quickly inspect the schema of your data, which is useful for data validation and cleaning processes.