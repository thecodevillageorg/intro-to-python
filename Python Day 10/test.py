 # for each student, ask for the number of subjects they'd like to enter
number_of_subjects = int(input("Enter the number of subjects: "))
    # list to hold subjects
subjects = []
    
for subject in range(number_of_subjects):
        # for each subject, record the name
    subject_name =  input("Enter the subject name: ")
    subjects.append(subject_name)


for subject in subjects:
    print(subject)
    