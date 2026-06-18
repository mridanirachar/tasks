# Student Management System

name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

skills = input("Enter skills separated by space: ").split()

marks = int(input("Enter marks: "))

student = {
    "Name": name,
    "Age": age,
    "Course": course,
    "Skills": skills,
    "Marks": marks
}

print("\nStudent Profile")
print(student)

new_skill = input("\nEnter one more skill to add: ")
skills.append(new_skill)

print("Updated Skills:", skills)

records = set()

record = (name, age, course)
records.add(record)

print("Unique Student Records:")
print(records)