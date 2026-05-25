student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for x in student_scores:
    score =  student_scores[x]
    if score >= 91:
        student_grades[x] = "Outstanding"
    elif score >= 81:
        student_grades[x] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[x] = "Acceptable"
    else:
        student_grades[x] = "Fail"
        
print(student_grades)
    
    
