import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#read data from CSV
data = pd.read_csv('__.csv')

#Descriptives statistics table
while True:
    descriptives_prompt = 'Do you want to see a descriptives table?(yes/no)'
    if descriptives_prompt.lower()== 'yes':
        group_data= data[['']]
        descripitve_table = pd.DataFrame({
            'Mean': condition_data.mean(),
            'Median': condition_data.median(),
            'StdDev': condition_data.std(),
            'Min': condition_data.min(),
            'Max': condition_data.max(),
        }, index= [''])
        print(descriptives_table)
        break
    elif descripitives_prompt.lower() == 'no':
        print('Descripitves table not requested.')
        break
    else:
        print('Please enter a valid choice.')

#Repeated-Measures ANOVA
while True:
    anova_prompt = 'Do you want to perform a repeated-measures ANOVA? (yes/no)'
    choice = input(anova_prompt).lower()
    if choice == 'yes':
        within_subjects= []
        rm= statsmodels.stats.anova.AnovaRM(data, )
        print(rm.fit())
        break
    elif choice == 'no':
        print('Repeated-measures ANOVA not requested.')
        break
    else:
        print('Please enter a valid choice.')

#One-way Anova
while True:
    oneWay_prompt= 'Do you want to perform one-way ANOVA? (yes/no)'
    choice= input(oneWay_prompt).lower()
    if choice == 'yes':
        conditions= []
        response_times = data[conditions]
        f_statistic, p_value= stats.f_oneway(*[data[col] for col in response_times.columns])
        print('F-statisitic:', f_statistic)
        print('p-value:', p_value)
        break
    elif choice == 'no':
        print('One-way ANOVA not requested.')
        break
    else:
        print('Please enter a valid choice.')

#Log-transformed Graph
while True:
    graph_prompt= 'Do you want to produce a graph with average response time between conditions? (yes/no)'


