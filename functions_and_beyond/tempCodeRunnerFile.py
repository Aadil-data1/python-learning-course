marks = {
    "Math": 85,
    "History": 92,
    "English": 76,
    "Physics": 88
}

higher_marks = {subject : mark
                for subject, mark in marks.items() # Creating a new dictionary containing only subjects where the mark is 80 or above.
                if mark > 80}

print(higher_marks)

result = {subject: "A" if mark >90 else "B"
          for subject, mark in marks.items()
          }

print(result)
