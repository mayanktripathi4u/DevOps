import pandas as pd

# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com']
}

df = pd.DataFrame(data)

# Get columns and their data types
column_types = df.dtypes

# Display columns and their data types
print("Columns and their data types:")
for column, dtype in column_types.items():
    print(f"Column '{column}': Data type '{dtype}'")
