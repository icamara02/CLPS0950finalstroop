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











