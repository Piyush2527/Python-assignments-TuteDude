# normal dictionary to store student marks
student={
    'Piyush': 85.5,
    'Ankit': 90.0,
    'Riya': 78.0,
    'Sneha': 88.5,
    'Aman': 92.0,
    'Divya': 80.0,
    'Karan': 75.5,
    'Neha': 89.0,
    'Vikram': 95.0,
    'Sonal': 82.5,
    'lokesh': 87.0 
}
fStudent=input("Enter the student's name: ")
c=0
for name, marks in student.items():
    if name.lower() == fStudent.lower():
        print(f"{fStudent}'s marks: {marks}")

    elif name.lower() != fStudent.lower():
        c+=1
if c==len(student):
    print("Student not found.")


# # fetch from file and display
# with open('Assignment-5/student_marks.txt','rt') as f:
#     content=f.readlines()
#     for l in content:
#         name, marks = l.split(' and ')
#         print(f'{name.strip()}: {marks.strip()}')

# with open('Assignment-5/student_marks.txt','at') as f:
#     n=int(input("Enter number of students to add: "))
#     for i in range(n):
#         name=input(f"Enter name of {i+1} student: ")
#         marks=input(f"Enter marks of {i+1} student: ")
#         f.write(f'\n{name} and {marks}')
#         print(f'Added: {name} and {marks}\n')

