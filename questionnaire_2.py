# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
def demographic_survey(): #collect demographic information
    participant_id= input("Before we begin, please enter your participant ID number: ")
    while True:
        print("\nFirst, we will be collecting basic demographic information.")
        print("What is your gender?")
        print("1. Male")
        print("2. Female")
        print("3. Non-binary")
        print("4. Prefer not to say")
        print("5. Other")
        gender_category = input("Enter the number corresponding to your gender identity.")

        if gender_category == '1':
            gender="Male"
            break
        elif gender_category == '2':
            gender = "Female"
            break
        elif gender_category == '3':
            gender = "Non-binary"
            break
        elif gender_category == '4':
            gender = "Prefer not to say"
            break
        elif gender_category == '5':
            gender = input("Please specify your gender: ")
            break
        else:
            print("\nInvalid selection. Please enter a number between 1 and 5.")


    age = input("How old are you?")

    while True:
        print("What is your ethnicity?")
        print("1. White")
        print("2. Black")
        print("3. Asian")
        print("4. Hispanic or Latino")
        print("5. Native American or Alaska Native")
        print("6. Native Hawaiian or Pacific Islander")
        print("7. Other")
        ethnicity_selection = input("Enter the number corresponding to your ethnicity choice: ")

        if ethnicity_selection == '1':
            ethnicity = "White"
            break
        elif ethnicity_selection == '2':
            ethnicity = "Black"
            break
        elif ethnicity_selection == '3':
            ethnicity = "Asian"
            break
        elif ethnicity_selection == '4':
            ethnicity = "Hispanic or Latino"
            break
        elif ethnicity_selection == '5':
            ethnicity = "Native American or Alaska Native"
            break
        elif ethnicity_selection == '6':
            ethnicity = "Native Hawaiian or Pacific Islander"
            break
        elif ethnicity_selection == '7':
            ethnicity = input("Please specify your ethnicity: ")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")

    print("You have completed the demographic section of the survey. Now you will answer more general questions.")
    while True:
        print("Have you ever played with dolls as a child?")
        print("1. Yes")
        print("2. No")
        question_dolls= input("Enter the number corresponding to your answer choice: ")
        if question_dolls == '1':
            dolls= "Yes"
            break
        elif question_dolls == '2':
            dolls= "No"
            break
        else:
             print("Invalid selection. Please enter either  1 or 2.")

    while True:
        print("Have you ever considered pursuing/are pursuing a career in STEM?")
        print("1. Yes")
        print("2. No")
        question_STEM= input ("Enter the number corresponding to your answer choice: ")
        if question_STEM == '1':
            STEM= "Yes"
            break
        elif question_STEM == '2':
            STEM= "No"
            break
        else:
            print("Invalid selection. Please enter either  1 or 2.")

    while True:
        print("Have you watched the Barbie movie?")
        print("1. Yes")
        print("2. No")
        question_barbie= input("Enter the number corresponding to your answer choice: ")
        if question_barbie== '1':
            barbie= "Yes"
            break
        elif question_barbie== '2':
            barbie= "No"
            break
        else:
            print("Invalid selection. Please enter either  1 or 2.")

    while True:
        print("When considering leadership roles, do you instinctively picture a man or woman in the position?")
        print("1. Man")
        print ("2. Woman")
        question_leader= input ("Enter the number corresponding to your answer choice: ")
        if question_leader =='1':
            leader= "Man"
            break
        if question_leader =='2':
            leader= "Woman"
            break
        else:
            print("Invalid selection. Please enter either  1 or 2.")
    while True:
        print("Do you notice differences in the way you perceive assertiveness or competence based on gender?")
        print("1. Yes")
        print("2. No")
        question_assertiveness= input ("Enter the number corresponding to your answer choice: ")
        if question_assertiveness=='1':
            assertiveness= "Yes"
            break
        elif question_assertiveness=='2':
            assertiveness= "No"
            break
        else:
            print("Invalid selection. Please enter either  1 or 2.")

    while True:
        print("Do you find yourself using gendered language (e.g., 'bossy' for women, 'assertive' for men) to describe behavior?")
        print("1. Yes")
        print("2. No")
        question_language= input("Enter the number corresponding to your answer choice: ")
        if question_language=='1':
            language= "Yes"
            break
        elif question_language=='2':
            language= "No"
            break
        else:
            print("Invalid selection. Please enter either  1 or 2.")


#display responses for participants
    print("\nThank you for completing the survey! Here are your responses: ")
    print("Gender:", gender)
    print("Age:", age)
    print("Ethnicity:", ethnicity)
    print("Dolls:", dolls)
    print("STEM:", STEM)
    print("Barbie:", barbie)
    print("Leader:", leader)
    print("Assertiveness:", assertiveness)
    print("Language:", language)

#save data into a new csv file
    headers= ["Participant ID", "Gender", "Age", "Ethnicity", "Dolls", "STEM", "Barbie", "Leader", "Assertiveness", "Language"]
    with open ('survey_responses.csv', 'a', newline= '') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow ([participant_id, gender, age, ethnicity, dolls, STEM, barbie, leader, assertiveness, language])



if __name__ == '__main__':

    demographic_survey()


