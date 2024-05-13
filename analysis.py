import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


#read data from CSV
data = pd.read_csv('pivot_table.csv')

#Descriptives statistics table
while True:
    descriptives_prompt = input('Do you want to see a descriptives table?(yes/no)')
    if descriptives_prompt == 'yes':
        group_data = data[['GC_Cong_Avg', 'GC_Incong_Avg', 'CN_Cong_Avg', 'CN_Incong_Avg']]
        descriptive_table = pd.DataFrame({
            'Mean': group_data.mean(),
            'Median': group_data.median(),
            'StdDev':group_data.std(),
            'Min': group_data.min(),
            'Max': group_data.max(),
        }, index= ['GC_Cong_Avg', 'GC_Incong_Avg', 'CN_Cong_Avg', 'CN_Incong_Avg'])
        print(descriptive_table)
        break
    elif descriptives_prompt == 'no':
        print('Descripitves table not requested.')
        break
    else:
        print('Please enter a valid choice.')

#Repeated-Measures ANOVA
while True:
    anova_prompt = input('Do you want to perform a repeated-measures ANOVA? (yes/no)')
    if anova_prompt == 'yes':
        within_subjects= ['GC_Cong_Avg', 'GC_Incong_Avg', 'CN_Cong_Avg', 'CN_Incong_Avg']
        rm_data= data.melt(var_name= 'Condition', value_name= 'Response Time')
        rm_data['Participant']= range(1, len(rm_data)+1)
        print(rm_data)
        break
    elif anova_prompt == 'no':
        print('Repeated-measures ANOVA not requested.')
        break
    else:
        print('Please enter a valid choice.')

#One-way Anova
while True:
    oneWay_prompt= input('Do you want to perform one-way ANOVA? (yes/no)')
    if oneWay_prompt == 'yes':
        conditions= ['GC_Cong_Avg', 'GC_Incong_Avg', 'CN_Cong_Avg', 'CN_Incong_Avg']
        response_times = data[conditions]
        f_statistic, p_value= stats.f_oneway(*[data[col] for col in response_times.columns])
        print('F-statisitic:', f_statistic)
        print('p-value:', p_value)
        break
    elif oneWay_prompt == 'no':
        print('One-way ANOVA not requested.')
        break
    else:
        print('Please enter a valid choice.')
print ('ANOVA findings were non-significant.')
#Log-transformed Graph
while True:
    graph_prompt= input ('Do you want to produce a graph with average response time between conditions? (yes/no)')
    if graph_prompt== 'yes':
        condition= ['GC_Cong_Avg', 'GC_Incong_Avg', 'CN_Cong_Avg', 'CN_Incong_Avg']
        colors = ['b', 'r', 'g', 'm']
        linestyle = ['-','--', '-', '--']
        plt.figure()
        for i, condition in enumerate(conditions):
            plt.plot(data[condition], linestyle[i], label=condition, color=colors[i])
        plt.xlabel('Participant')
        plt.ylabel('Log-Transformed Response Time')
        plt.title('Log-Transformed Response Time for Congruent and Incongruent Conditions')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()
        break
    elif graph_prompt== 'no':
        print('Graph not requested.')
        break
    else:
        print('Invalid input. Please enter "yes" or "no".')

#Box plot
while True:
    boxplot_prompt= input('Do you want to see a box plot?(yes/no)')
    condition = ['GC_Cong_Avg', 'GC_Incong_Avg', 'CN_Cong_Avg', 'CN_Incong_Avg']
    if boxplot_prompt== 'yes':
        response_times= [data[condition] for condition in condition]
        plt.figure()
        plt.boxplot(response_times, labels = condition)
        plt.xlabel('Task and Condition')
        plt.ylabel('Response Time')
        plt.title('Box Plot of Response Times for Different Tasks and Condtions')
        plt.show()
        break
    elif boxplot_prompt == 'no':
        print('Box plot not requested.')
        break
    else:
        print('Please enter a valid choice.')


