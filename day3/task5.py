# Day 3 - Student Management System

name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
marks = int(input("Enter marks: "))

# list
skills = []
n = int(input("How many skills do you have? "))

for i in range(n):
    skill = input("Enter skill: ")
    skills.append(skill)

# dictionary
student = {
    "Name": name,
    "Age": age,
    "Course": course,
    "Marks": marks,
    "Skills": skills
}

print("\nStudent Profile")
print(student)

# update list
new_skill = input("Enter one more skill: ")
student["Skills"].append(new_skill)

print("Updated Skills:", student["Skills"])

# tuple
record = (name, age, course)

# set
records = set()
records.add(record)

print("Unique Student Records:", records)

# string methods
print("Name in uppercase:", name.upper())
print("Course in lowercase:", course.lower())