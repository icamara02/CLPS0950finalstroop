
# Subgroup analysis
#Looking at data by gender
data= pd.read_csv('__.csv')
data['Gender']= data['Gender'].str.lower()

if 'Gender' in data.columns:
    #group by gender and calculate summary statistics
    gender_data= data.groupby('Gender')['Response Time'].describe()
    plt.subplot (1,2,1)
    plt.table(cellText=gender_data.values,
              colLabels= gender_data.colummns,
              rowLabels= gender_data.index,
              loc='center')
    plt.axis('off')

    print("Summary statistics for response time grouped by gender: ")
    print(gender_data)
    #display bargraph to visualize stats
    plt.figure(figsize= (12,6))
    plt.subplot(1,2,2)
    plt.bar(gender_data.index, gender_data['mean'], color='red')
    plt.xlabel('Gender')
    plt.ylabel('Mean Response Time')
    plt.title('Mean Response Time by Gender')

    plt.show()
else:
    print("Error: 'Gender' column not found.")
