import pandas as pd
from pathlib import Path

students_csv = Path(__file__).with_name("students.csv")

df = pd.read_csv(students_csv)
print(df.info())
print(df.describe())

df.columns = df.columns.str.title()       # to captilize first alphabet of a column name 

gender_map = {
    "M": "Male",
    "F": "Female"
}
df["Gender"] = df["Gender"].replace(gender_map)  # "Replace the gender with "M" and "F". We can also use "MAP", if we have to map each value    


#print(df.describe)

df["Total"] = df["Math"] + df["Science"]+ df["English"]   # calculating total marks achieved by a student

def grade(total):
    if total >= 250:
        return "A"
    elif total >= 200:            # calculating grade of each student after calculating total
        return "B"
    elif total >= 150:
        return "C"
    else:
        return "D"

df["Grade"] = df["Total"].apply(grade)    # we can use apply to run our own function on a column
print(df)