import numpy as np
from pathlib import Path

csv_path = Path(__file__).with_name("students_scores.csv")

scores = np.loadtxt(
    csv_path,
    delimiter=",",
    skiprows=1
)



students = np.array([
   "Ali", "Sara", "John", "Emma", "David",
    "Aisha", "Rahul", "Priya", "Omar", "Neha"
])

subjects = np.array([
    "Math", "Science", "English", "Computer"
])
print(scores.shape)
print(scores.ndim)
print(scores.dtype)
student_ids = np.arange(1,11) # Creating an array of student IDs
zeroes = np.zeros(10)
ones = np.ones(10)
scores_int = scores.astype(int) # Converting the marks to an integer data type from float
print(scores_int.dtype)

print(f"Name: {students[0]}, Marks : {scores[0]}") # printing name and marks of first student

maths_marks = np.sum(scores[:,0])         # calculating Math marks of all ten students
print(f"Total Math marks of all 10 students : {maths_marks}")

# Show the marks of students 3 through 6.

marks_middle_students = scores[3:6]
print(f"Marks of Emma, David and Aisha are {marks_middle_students} respectively")

# Display the English and Computer marks of the first five students.

eng_comp_m = scores[0:5, 2:]  # english and computer marks of first five students
print(eng_comp_m)

# Display the complete rows for Ali, John and Priya using integer-array indexing.

ajp = f"Marks of {students[0]} : {scores[0]}\nMarks of {students[2]} : {scores[2]}\nMarks of {students[7]} : {scores[7]}"
print(ajp)       # printing marks of above students separately

# Calculate the total marks for each student and their average marks

total_marks_each = np.sum(scores, axis= 1)
print(total_marks_each)
avg_s = (total_marks_each/400)*100 #average of each student
print(avg_s)



# calculate the average, maximum, minimum, median and standard deviation for each subject.
avg = (np.average(scores, axis = 0)) 
print(avg)
print(np.min(scores, axis = 0))
print(np.max(scores, axis = 0))
print(np.median(scores, axis= 0 ))
print(np.std(scores, axis = 0))


higher_avg = avg_s   
higher_avg >75       
print(students[higher_avg>75])   # Students whose average marks are above 75% using Boolean Masking

low_score = np.any(scores<40, axis= 1)
print(students[low_score])             # students who score less than 40

grade = np.where(
    avg_s > 80, "A",
    np.where(                             # create a grade for each student based on their average:    
        avg_s > 60, "B",
        np.where(avg_s > 45, "C", "Fail")
    )
)


#print(grade)
 
un_grade = np.unique(grade, return_counts= True)
print(un_grade)                                          # determine how many students received each grade.

top_students = np.sort(avg_s)[::-1]   # average marks from top to low. we can also find their indices using argsort
print(top_students)




