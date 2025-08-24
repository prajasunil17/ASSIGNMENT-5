students = {
    "Alice" : "91",
    "John" : "45",
    "Smith" : "71",
    "Sunil" : "99.99", 
}

studentName = input("Enter the student's name: ")

if studentName in students:
    print(f"{studentName}'s marks: {students[studentName]}")
else:
    print("Student not found.")
