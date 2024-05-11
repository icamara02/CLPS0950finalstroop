import pandas as pd

folder_path = '/Users/sofiagerlein/Desktop/CLPS0950finalstroop/raw_data.csv'
df = pd.read_csv(folder_path)

#all the unique participant names
pivot_table = pd.unique(df.iloc[:,0])

#creating a dataframe to store response times
pivot_table_df = pd.DataFrame(columns=['participant ID','mean_rt_GC_cong',
                                       'mean_rt_GC_incong','mean_rt_CN_cong',
                              'mean_rt_CN_incong'])
print(pivot_table_df)
