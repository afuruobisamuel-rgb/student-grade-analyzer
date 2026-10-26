students = []
subjects = 3

checking = "yes"
while checking =="yes":
    student_name = input("Student name: ")
    scores = []
    for attendance in range (1, subjects + 1):
        
        grade = int(input("Student's score: "))
       
       
        scores.append(grade)
    record = {
        "name": student_name,
        "score": scores
    }
    
    students.append(record)
    average_score = sum(scores)/ len(scores)
    print(f'''Student name: {student_name}
    Average score: {average_score}''')
    if average_score >= 70:
        print("Grade: A")
        grade_output = "A"
    elif average_score >= 60:
        print("Grade: B")
        grade_output = "B"
    elif average_score >=50:
        print("Grade: C")
        grade_output = "C"
    elif average_score >=45:
        print("Grade: D")
        grade_output = "D"
    elif average_score >= 40:
        print("Grade: E")
        grade_output = "E"
    else:
        print("Grade: F")
        grade_output = "F"
    
    
    record ["Average"] = average_score
    record["grade"] = grade_output
    checking = input("do you want to continue recording student? ").strip().lower()

for student in students:
    
    print(f'Student name: {student["name"]}')
    print(f'score: {student["score"]}')
    print(f'Average: {student["Average"]}')
    print(f'Grade: {student["grade"]}')

 

