# The data is impoted

import pandas as pd
df = pd.read_excel("C:\\Users\\ayman\\Downloads\\TEST data 7 (1).xlsx")
print(df)
print(df.head())

## cleaning the data

df = df.drop_duplicates()
print(df.columns)

## Replacing  the space by _
df.columns= df.columns.str.strip().str.replace(' ','_')
print(df.columns)

## Removing the space by Strip

# ## Correcting the data type

df['SB date'] = pd.to_datetime(df['SB_date'], errors='coerce') 
# print(df['SB_date'])
df['GST'] = pd.to_numeric(df['GST'], errors='coerce')  

# # ## Handling missing values

df['_Not_Claimed_And_NULL_for_ROSLL'] = df['_Not_Claimed_And_NULL_for_ROSL'].fillna('NULL')
df['GST_Status_Check'] = df['GST_Status_Check'].fillna('Missing')

# # ## Filter only ROSL CLAIMED SHIPMENT

rosl_claimed = df[df['Claimed, _Not_Claimed_And_NULL_for_ROSL'] == 'ROSL CLAIMED']


# ## Group by PORT & Status

grouped = df.groupby(['PORT Code', 'Current status']).agg({
    'SB no': 'count',
    'GST': 'sum'
}).reset_index()

grouped.rename(columns={'SB_no': 'Shipment_Count', 'GST': 'Total_GST'}, inplace=True)


## Final Processed Dataset

# Save the cleaned dataset
df.to_excel('processed_dataset.xlsx', index=False)

# Save grouped summary separately (optional)
grouped.to_excel('grouped_summary.xlsx', index=False)
