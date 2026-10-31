# created a student progress report text file and store student's performance

student = {
    "name": "Jacob",
    "marks": [85, 72, 91, 64, 78]
}

total_marks = 0

for mark in student["marks"]:
    total_marks += mark

average = total_marks / len(student["marks"])
highest_marks = max(student["marks"])
lowest_marks = min(student["marks"])

if total_marks >= 250:
    result = "pass"
else:
    result = "fail"

with open("progress_report.txt", "w") as file:  # we don't have to manually close the file, using "with" python automatically close the file
    file.write(f"Name: {student['name']}\n")
    file.write(f"Total Marks: {total_marks}\n")
    file.write(f"Average: {average}\n")
    file.write(f"Highest Marks: {highest_marks}\n")
    file.write(f"Lowest Marks: {lowest_marks}\n")
    file.write(f"Overall Result: {result}")

try:
    with open("progress_report.txt", "r") as file:   # "r" denotes reading text file after creating it
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found.")

# we can also add other details to above text file by employing "append".
# not only this, we can use .readlines() to read all into a list.