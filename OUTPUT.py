
#  Import Libraries
import pandas as pd
from datetime import datetime

# Load Dataset
file_path = r"C:\Users\ayman\Downloads\TEST data 7 (1).xlsx"  # Use raw string to avoid path errors
df = pd.read_excel(file_path, engine='openpyxl')

# Clean Column Names
df.columns = df.columns.str.strip().str.replace(' ', '_')
print(df.columns)

# Data Cleaning
df = df.drop_duplicates()  # Remove duplicate rows

# Trim string columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Correct data types
df['SB_date'] = pd.to_datetime(df['SB_date'], errors='coerce')
df['GST'] = pd.to_numeric(df['GST'], errors='coerce')
df['ROSL_Status_Flag'] = pd.to_numeric(df['ROSL_Status_Flag'], errors='coerce')

# Fill missing values
df['Clainmed,_Not_Claimed_And_NULL_for_ROSL'] = df['Clainmed,_Not_Claimed_And_NULL_for_ROSL'].fillna('NULL')

df['GST_Status_Check'] = df['GST_Status_Check'].fillna('Missing')

#  Computed Fields

df['Days_Since_SB_Date'] = (datetime.today() - df['SB_date']).dt.days

# PORT & Status concatenation
df['PORT_Status_Concatenation'] = df['PORT_Code'] + " - " + df['Current_status']

# Version 1: Sort by PORT_Code and Current_status
sorted_port_status = df.sort_values(by=['PORT_Code', 'Current_status'])

# Version 2: Sort by GST descending, then Days_Since_SB_Date descending
sorted_gst_days = df.sort_values(by=['GST', 'Days_Since_SB_Date'], ascending=[False, False])


#  Save Processed Datasets
sorted_port_status.to_excel(r"C:\Users\ayman\Downloads\Sorted_By_PORT_Status.xlsx", index=False)
sorted_gst_days.to_excel(r"C:\Users\ayman\Downloads\Sorted_By_GST_Days.xlsx", index=False)

# Verification
print("Cleaning, computed fields, and sorting complete!")
print("Columns:", df.columns)
print("First 5 rows:")
print(df.head())
