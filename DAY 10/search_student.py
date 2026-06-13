students = [
    {"Name": "John", "Marks": 85},
    {"Name": "Alice", "Marks": 92},
    {"Name": "Bob", "Marks": 78}
]

search_name = input("Enter student name to search: ")
found = False

for student in students:
  
    if student["Name"].lower() == search_name.lower():
        print("Student Found")
        print(f"Marks: {student['Marks']}")
        found = True
        break 

if not found:
    print("Student Not Found")