
# Python and Data Science Fundamentals

# 1. Variables
name = "Anjali"
marks = [75, 80, 90, 65, 85]

print("Name:", name)
print("Marks:", marks)

# 2. Calculate Total and Average Marks
total = sum(marks)
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)

# 3. Loop
print("Student Marks:")
for mark in marks:
    print(mark)

# 4. Function
def show_course():
    print("I am learning Python and Data Science")

show_course()

# 5. Dictionary
student = {
    "name": name,
    "course": "BCA",
    "subject": "Data Science"
}

print("Student Details:", student)

# 6. File Handling
file = open("student.txt", "w")
file.write("Learning Python and Data Science")
file.close()

file = open("student.txt", "r")
print(file.read())
file.close()
