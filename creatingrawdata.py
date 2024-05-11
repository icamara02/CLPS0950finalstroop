import os
import pandas as pd


#folder path - if others use this, insert their folder path
folder_path = '/Users/sofiagerlein/Desktop/CLPS0950finalstroop/stroop/copyofdatatouse'

#storing all data
short_dfs = []
#go through every CSV in the folder
for csv in os.listdir(folder_path):
    if csv.endswith(".csv"):
        #read the file
        file_path = os.path.join(folder_path, csv)
        df = pd.read_csv(file_path)
        #keep only when practice == 0
        no_practice_or_empty = df[df['practice'] == 0]

        short_df = no_practice_or_empty.loc[:,['word', 'color','congruent',
                                            'incongruent','CN','GC','corrAns',
                                            'response.rt','key_resp_5.rt',
                                            'participant',]]
        #put the participant column first
        first_column = short_df.pop('participant')
        short_df.insert(0,'participant',first_column)

        #put all shorts together
        short_dfs.append(short_df)

raw_df = pd.concat(short_dfs, ignore_index=True)
# if you use this code, put in your own folder path
raw_data_folder_path = '/Users/sofiagerlein/Desktop/CLPS0950finalstroop'

raw_data_file_path = os.path.join(raw_data_folder_path, 'raw_data.csv')

# Write the raw DataFrame to an Excel file in the specified output folder
raw_df.to_csv(raw_data_file_path, index=False)

## MERGE data from questionnaire and match responses to participant ID numbers in raw data

# Folder path for raw data files
raw_data_folder_path = '/Users/icamara/Desktop/CLPS0950finalstroop'

# Read the existing raw data CSV file
raw_data_file_path = os.path.join(raw_data_folder_path, 'raw_data.csv')
raw_df = pd.read_csv(raw_data_file_path)

# Read the additional CSV file containing the new data
survey_data_file_path = os.path.join(raw_data_folder_path, 'survey_data.csv')
survey_df = pd.read_csv(survey_data_file_path)

# Check if 'Participant ID' column contains non-numeric values
non_numeric_ids = survey_df[~survey_df['Participant ID'].str.isdigit()]['Participant ID']
if not non_numeric_ids.empty:
    print("Warning: Non-numeric values found in 'Participant ID' column:", non_numeric_ids)

# Convert the 'Participant ID' column to numeric type
survey_df['Participant ID'] = pd.to_numeric(survey_df['Participant ID'], errors='coerce')

# Merge data based on participant ID numbers
merged_data = pd.merge(raw_df, survey_df, left_on='participant', right_on='Participant ID', how='left')

# Save merged data back to the raw data CSV file
merged_data.to_csv(raw_data_file_path, index=False)

print("Merged data saved back to 'raw_data.csv'")









