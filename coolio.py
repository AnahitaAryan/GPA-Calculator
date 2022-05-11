subject = {
    "name": "",
    "level": "",
    "score": "",
    "gpa": 0.0
    
}

level1 = {
    100 = 5.0,
    99 = 4.9,
    98 = 4.8,
    97 = 4.7,
    96 = 4.6,
    95 = 4.5, 
    94 = 4.4,
    93 = 4.3,
    92 = 4.2,
    91 = 4.1,
    90 = 4.0,
    89 = 3.9,
    88 = 3.8,
    87 = 3.7,
    86 = 3.6,
    85 = 3.5,
    84 = 3.4,
    83 = 3.3,
    82 = 3.2,
    81 = 3.1,
    80 = 3.0,
    79 = 2.9,
    78 = 2.8,
    77 = 2.7,
    76 = 2.6,
    75 = 2.5,
    74 = 2.4,
    73 = 2.3,
    72 = 2.2,
    71 = 2.1,
    70 = 2.0
    
}

level2 = {
    100 = 5.5,
    99 = 5.4,
    98 = 5.3,
    97 = 5.2,
    96 = 5.1,
    95 = 5.0,
    94 = 4.9,
    93 = 4.8,
    92 = 4.7,
    91 = 4.6,
    90 = 4.5,
    89 = 4.4,
    87 = 4.3,
    86 = 4.2, 
    85 = 4.1,
    84 = 4.0,
    83 = 3.9,
    82 = 3.8,
    81 = 3.7,
    80 = 3.6,
    79 = 3.5,
    78 = 3.4,
    77 = 3.3, 
    76 = 3.2,
    75 = 3.1,
    74 = 3.0,
    73 = 2.9,
    72 = 2.8,
    71 = 2.7,
    70 = 2.6
}

level3 = {
    100 = 6.0,
    99 = 5.9,
    98 = 5.8, 
    97 = 5.7, 
    96 = 5.6,
    95 = 5.5,
    94 = 5.4,
    93 = 5.3,
    92 = 5.2, 
    91 = 5.1,
    90 = 5.0, 
    89 = 4.9,
    88 = 4.8,
    87 = 4.7,
    86 = 4.6,
    85 = 4.5,
    84 = 4.4,
    83 = 4.3,
    82 = 4.2,
    81 = 4.1,
    80 = 4.0,
    79 = 3.9,
    78 = 3.8,
    77 = 3.7,
    76 = 3.6,
    75 = 3.5,
    74 = 3.4,
    73 = 3.3, 
    72 = 3.2,
    71 = 3.1,
    70 = 3.0
}
def get_subjects():
    #make an empty list
    subjects = []
    #accept input from user until they are done
while True:
    subject["name"] = input("enter subject name: ")
    subject["grade"] = int("enter grade: "))
    subject["level"] = int(" if user is done
    answer = input("are you enter level: "))
    subjects.append(subject)
    #check done? [y/n]:")
    if answer.lower() == 'y':#if they are
        break# end the loop
    return subjects #give back the list of subjects

def calculate_weighted_gpa(subject):
    score = subject["score"]
    level = subject["level"]
def calculate_overall_average():
    #calculate overall average GPA by dividing individual class gpa and dividing by the number of subjects entered
    pass
def display_score():
    pass
def main():
    subjects = get_subjects()