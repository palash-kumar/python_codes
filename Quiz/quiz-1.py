'''Problem 1:
Make a program that reads a seller's name, his/her fixed salary, and the sale's total
sales made by himself/herself in the month (in money). Considering that this seller
receives 15% over all products sold, write the final salary (total) of this seller at the
end of the month, with two decimal places.
Input
The input file contains a text (employee's first name), and two double precision
values, which are the seller's salary and the total value sold by him/her.
Output
Print the seller's total salary, according to the given example.
'''
print("Problem 1 Solution: ")
name = input("Name : ").strip()
fixed_salary = float(input("Fixed Salary : "))
total_sales = float(input("Total Sales : "))
total_salary = fixed_salary + (total_sales * 0.15)
print(f"TOTAL = R${total_salary:.2f}")

print("\n")
'''Problem 2:
Read three values (variables A, B and C), which are the three student's grades.
Then, calculate the average, considering that grade A has weight 2, grade B has
weight 3 and the grade C has weight 5. Consider that each grade can go from 0 to
10.0, always with one decimal place.
Input
The input file contains 3 values of floating points (double) with one digit after the
decimal point.
Output
Print the message "MEDIAN" and the student's average according to the following
example, with a blank space before and after the equal signal.
'''
print("Problem 2 Solution: ")
A = float(input("A : "))
B = float(input("B : "))
C = float(input("C : "))
average = (A * 2 + B * 3 + C * 5) / 10
print(f"MEDIAN = {average:.1f}")