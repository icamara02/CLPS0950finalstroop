import pandas as pd
import matplotlib.pyplot as plt

# Read the data
data = pd.read_csv('subgroup_merged.csv')

print ('First, we will look at average response times across conditions, grouped by gender. ')
# check that gender column in consistent
data['Gender'] = data['Gender'].str.lower()

# Define the conditions
conditions = ['CN_Cong_Avg', 'CN_Incong_Avg', 'GC_Cong_Avg', 'GC_Incong_Avg']

# response time grouped by gender across the conditions
for condition in conditions:
    # Group by gender and calculate summary statistics for the current condition
    gender_data = data.groupby('Gender')[condition].describe()

    print(f"Summary statistics for response time grouped by gender for {condition}:")
    print(gender_data)

    # Visualize response times by gender for the current condition
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(gender_data)), gender_data['mean'], color='blue')
    plt.xlabel('Gender')
    plt.ylabel('Mean Response Time')
    plt.title(f'Mean Response Time by Gender for {condition} Condition')

    plt.xticks(range(len(gender_data)), ['female', 'male', 'Non-binary', 'Prefer not to say'])
    plt.show()


# Analysis: Have you ever played with dolls as a child?
print ('Next, we will look at average response times across conditions based on responses to: Have you ever played with dolls as a child? See plot. ')
dolls_question = 'Dolls'
dolls_responses = data[dolls_question].unique()

for response in dolls_responses:
    grouped_dolls = data[data[dolls_question] == response].groupby(dolls_question)[['CN_Cong_Avg', 'GC_Cong_Avg']].mean()

    # Plot the results
    plt.figure(figsize=(10, 6))
    grouped_dolls.plot(kind='bar')
    plt.xlabel(f'Response to "{dolls_question}"')
    plt.ylabel('Mean Response Time')
    plt.title(f'Mean Response Time Across Two Conditions for Response: {response}')
    plt.xticks(rotation=0)
    plt.legend(title='Condition')
    plt.tight_layout()
    plt.show()


#Analysis: "When considering leadership roles, do you instinctively picture a man or woman in the position?"
print ('Now, we will look at responses to the leader question based on gender.')
leader_column = 'Leader'
gender_column = 'Gender'

# Group the data by gender and count the responses
gender_response = data.groupby(gender_column)[leader_column].value_counts().unstack()

# Plot the bar graph
gender_response.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.title('Responses by Gender')
plt.xticks(range(len(gender_response.index)), gender_response.index, rotation=0)  # Set custom x-axis labels
plt.legend(title=leader_column)
plt.tight_layout()
plt.show()

print ('See plot.')

language_question = 'Language'
language_responses = data[language_question].unique()

# go over each response value
for response in language_responses:
    # Filter data for the current response value
    filtered_data = data[data[language_question] == response]

    # Group by the language question and calculate mean response times for each condition
    grouped_language = filtered_data.groupby(language_question)[['CN_Cong_Avg', 'GC_Cong_Avg']].mean()

    # Plot the results
    plt.figure(figsize=(10, 6))
    grouped_language.plot(kind='bar')
    plt.xlabel(f'Response to "{language_question}"')
    plt.ylabel('Mean Response Time')
    plt.title(f'Mean Response Time Across Two Conditions for Response: {response}')
    plt.xticks(rotation=0)
    plt.legend(title='Condition')
    plt.tight_layout()
    plt.show()