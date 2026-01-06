# Task 1: The "Grade Scanner" (2D Lists & Functions)
# The Challenge: You have a 2D list where each inner list represents a student's scores in different subjects. Write a 
# function check_failing(grades_grid) that prints "Student [Index] failed a subject!" if any of their scores are below 50.

all_grades = [
[88, 92, 70], # Student 0 
 [45, 80, 77], # Student 1 (Has a 45!) 
 [99, 100, 95] # Student 2
]

def check_failing(grades_grid):
    for student, grades in enumerate(grades_grid):
        #for grade inrades_grid:
        #print(f'{student}')
        #for grade in student:
        if any(grade < 50 for grade in grades):
            print("Student : ", (student), "failed a subject!")

check_failing(all_grades)



# Task 2: The "Pixel Flasher" (Modifying 2D Lists)
# The Challenge: In computer graphics, a screen is a 2D grid of 0s (off) and 1s (on). Write a 
# function called activate_row(screen, row_index) that takes the grid and a row number, then uses a single loop to change every pixel in that specific row to 1.

monitor = [
[0, 0, 0], 
 [0, 0, 0], 
[0, 0, 0]
]

def activate_row(screen, row_index):
    for col in range(len(screen[row_index])):
        screen[row_index][col] = 1
    return screen

activate_row(monitor, 2)

print(monitor)