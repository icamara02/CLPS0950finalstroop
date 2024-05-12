import os
import pandas as pd

folder_path = '/Users/sofiagerlein/Desktop/CLPS0950finalstroop/raw_data.csv'
raw_df = pd.read_csv(folder_path)

#all the unique participant names
participant_ids = pd.unique(raw_df.iloc[:,0])
#put those names into a column in a dataframe
pivot_table_df = pd.DataFrame({'participant id': participant_ids})

## finding the average response time for GC_cong
gc_cong_means = []

for index, row in pivot_table_df.iterrows():
    id = row['participant id']
    #index for GC_Cong and that indiv id
    idx1 = ((raw_df['participant'] == id) & (raw_df['congruent'] == 1) &
            (raw_df['GC']==1))
    #table with only participant id and rows
    GC_cong_table = raw_df[idx1]
    #find the mean
    GC_cong_mean = GC_cong_table['GC.rt'].mean()
    #put mean into list
    gc_cong_means.append(GC_cong_mean)

#put the list into the dataframe here at the end
pivot_table_df.insert(1,'GC_Cong_Avg',gc_cong_means)

## finding the average response time for GC_incong
gc_incong_means = []

for index, row in pivot_table_df.iterrows():
    id = row['participant id']
    #index for GC_incong and that indiv id
    idx2 = ((raw_df['participant'] == id) & (raw_df['incongruent'] == 1) &
            (raw_df['GC']==1))
    #table with only participant id and rows
    GC_incong_table = raw_df[idx2]
    #find the mean
    GC_incong_mean = GC_incong_table['GC.rt'].mean()
    #put mean into list
    gc_incong_means.append(GC_incong_mean)

#put the list into the dataframe here at the end
pivot_table_df.insert(2,'GC_Incong_Avg',gc_incong_means)

## finding the average response time for CN_cong
cn_cong_means = []

for index, row in pivot_table_df.iterrows():
    id = row['participant id']
    #index for CN_Cong and that indiv id
    idx3 = (raw_df['participant'] == id) & (raw_df['congruent'] == 1) & (raw_df['CN']==1)
    #table with only participant id and rows
    CN_cong_table = raw_df[idx3]
    #find the mean
    CN_cong_mean = CN_cong_table['CN.rt'].mean()
    #put mean into list
    cn_cong_means.append(CN_cong_mean)

#put the list into the dataframe here at the end
pivot_table_df.insert(3,'CN_Cong_Avg',cn_cong_means)

## finding the average response time for CN_incong
cn_incong_means = []

for index, row in pivot_table_df.iterrows():
    id = row['participant id']
    #index for CN_incong and that indiv id
    idx4 = (raw_df['participant'] == id) & (raw_df['incongruent'] == 1) & (raw_df['CN']==1)
    #table with only participant id and rows
    CN_incong_table = raw_df[idx4]
    #find the mean
    CN_incong_mean = CN_incong_table['CN.rt'].mean()
    #put mean into list
    cn_incong_means.append(CN_incong_mean)

#put the list into the dataframe here at the end
pivot_table_df.insert(4,'CN_Incong_Avg',cn_incong_means)

# if you use this code, put in your own folder path
pivot_table_folder_path = '/Users/sofiagerlein/Desktop/CLPS0950finalstroop'

pivot_table_file_path = os.path.join(pivot_table_folder_path, 'pivot_table.csv')

# Write the raw DataFrame to an Excel file in the specified output folder
pivot_table_df.to_csv(pivot_table_file_path, index=False)

