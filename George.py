user = "Linus"
print("Hello, I am", user)
user = "George" # a new value
print("Hello, I'am", user)
name = "Martyna"
age = 26.0
height = 1.64
student_now = True
city = "Poznan"
print(name, "is", age, "years old")
print(type(name), type(age))
print(type(height), type(student_now))
slices_per_student = 3
students = 14

present_students =  students - 4
total_slices_needed =  present_students * slices_per_student
cost_per_student = 500 / present_students / boxes_to_order = total_slices_needed // 8
leftover_slices = (boxes_to_order*8) % present_students