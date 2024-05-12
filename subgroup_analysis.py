import pandas as pd
import matplotlib.pyplot as plt

# Subgroup analysis
# Looking at data by gender
data = pd.read_csv('raw_data.csv')
data['Gender'] = data['Gender'].str.lower()

# Conditions
conditions = ['CN', 'GC']
while True:
    condition_choice = input('Do you want to see average response times grouped by gender for Colornaming (CN) or Gender Categorization (GC)? ')
    if condition_choice.upper() in conditions:
        # Group by gender and calculate summary statistics
        gender_data = data.groupby('Gender')[f'{condition_choice}.rt'].describe()

        print("Summary statistics for response time grouped by gender: ")
        print(gender_data)

        plt.figure(figsize=(12, 6))
        plt.bar(range(len(gender_data)), gender_data['mean'], color='red')
        plt.xlabel('Gender')
        plt.ylabel('Mean Response Time')
        plt.xticks(range(len(gender_data)), gender_data.index)  # Set custom x-axis labels
        plt.title(f'Mean Response Time by Gender for {condition_choice} Condition')
        plt.show()

        other_condition = input('Do you want to see response time for another condition? ')
        if other_condition.lower() != 'yes':
            break
    else:
        print('Invalid condition choice. Please enter CN or GC.')



#
