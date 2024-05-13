import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('pivot_table.csv')

# Read the second CSV file
df2 = pd.read_csv('filtered_survey.csv')

# Merge the two DataFrames based on a common identifier
merged_df = pd.merge(df1, df2, left_on='participant id', right_on='Participant ID')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('subgroup_merged.csv', index=False)