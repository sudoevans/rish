#! python3
#Rishabh Assignment
number_of_students=int(input("Enter the Number of students: "))
marks_of_students=[]
for i in range(number_of_students):
    i+1
    marks=int(input(f"Enter marks of the student {i}:"))
    marks_of_students.append(marks)
# print(marks_of_students)
# Finding maximum mark:
print("Highest Mark is :",max(marks_of_students))
marks_of_students.sort(reverse=True)# We use reverse =True to return list in descending order
sorted_marks_of_students=sorted(marks_of_students)# The sorted method returns our sorted list

# The second highest mark is the second item in the sorted list
print("The second Highest mark is",sorted_marks_of_students[-2])

#Its that simple, Happy Codding!

