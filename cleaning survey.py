import pandas as pd

# Read the CSV file
data = pd.read_csv('survey_data.csv')

# Display the original data
print("Original Data:")
print(data)

# Identify the word to search for in the first column
word_to_delete = 'Participant ID'

# Identify rows where 'participant id' is found in the first column
rows_to_delete = data.iloc[:, 0] == word_to_delete

# Display the rows to delete
print("\nRows to Delete:")
print(rows_to_delete)

# Delete the rows where 'participant' is found in the first column
data_filtered = data[~rows_to_delete]

# Display the filtered data
print("\nFiltered Data:")
print(data_filtered)

# Save the filtered data to a new CSV file
new_file = 'filtered_survey.csv'
data_filtered.to_csv(new_file, index=False)

print('\nRows containing the word in the first column deleted, and the filtered data saved to "{}".'.format(new_file))