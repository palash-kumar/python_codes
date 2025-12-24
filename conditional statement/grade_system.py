"""
Grade system for open and fixed credit schemes without using collections.
The user selects a department, enters scores for each course, and the script
outputs the CGPA calculated from class test, mid-term, and final-term scores.
"""

def grade_letter(total_point):
    if (total_point >= 90):
        return "A+"
    if (total_point >= 85 and total_point < 90):
        return "A"
    if (total_point >= 80 and total_point < 85):
        return "B+"
    if (total_point >= 75 and total_point < 80):
        return "B"
    if (total_point >= 70 and total_point < 75):
        return "C+"
    if (total_point >= 65 and total_point < 70):
        return "C"
    if (total_point >= 60 and total_point < 65):
        return "D+"
    if (total_point >= 50 and total_point < 60):
        return "D"
    
    return "F"

def grade_letter_cgpa(total_point):
    print(f"total_point inside grade_letter: {total_point}")
    if (total_point == 4.0):
        return "A+"
    if (total_point >= 3.75 and total_point < 4.0):
        return "A"
    if (total_point >= 3.5 and total_point < 3.75):
        return "B+"
    if (total_point >= 3.25 and total_point < 3.5):
        return "B"
    if (total_point >= 3.0 and total_point < 3.25):
        return "C+"
    if (total_point >= 2.75 and total_point < 3.0):
        return "C"
    if (total_point >= 2.5 and total_point < 2.75):
        return "D+"
    if (total_point >= 2.25 and total_point < 2.5):
        return "D"
    
    return "F"
    

def grade_point(total_score):
    if total_score >= 90:
        return 4.0 # A+
    if total_score >= 85 and total_score < 90:
        return 3.75 # A
    if total_score >= 80 and total_score < 85:
        return 3.5 # B+
    if total_score >= 75 and total_score < 80:
        return 3.25 # B
    if total_score >= 70 and total_score < 75:
        return 3.0 # C+
    if total_score >= 65 and total_score < 70:
        return 2.75 # C
    if total_score >= 60 and total_score < 65:
        return 2.5 # D+
    if total_score >= 50 and total_score < 60:
        return 2.25 # D
    return 0.0 # F
    
def validate_score(msg, min_score=0, max_score=20):
    while True: 
        try: 
            score = float(input(msg)) 
            if min_score <= score <= max_score: 
                return score 
            else: print(f"X Please enter a score between {min_score} and {max_score}.") 
        except ValueError: print("X Invalid input. Please enter a number.")

def read_total(course_label):
    print("--- " + course_label + " ---")
    class_test = validate_score("Class test score out of 20: ", 0, 20)
    mid_term = validate_score("Mid term score out of 40: ", 0, 40)
    final_term = validate_score("Final term score out of 40: ", 0, 40)
    total = class_test + mid_term + final_term
    print(f"Total score for {course_label} : {total} \n GPA: {grade_point(total)} ({grade_letter(total)})\n")
    return total


def run_open_credit(department):
    dept = department.lower()
    if dept == "cse" or dept == "CSE":
        # Subjects ("Data Structures", "Algorithms", "Computer Metworks", "Object Oriented Programming", "Operating Systems", "CSE")
        print("CSE selected (open credit)")
        data_structures = read_total("Data Structures (4 credits)")
        algorithms = read_total("Algorithms (3 credits)")
        networking = read_total("Computer Networks (3 credits)")
        oop = read_total("Object Oriented Programming (4 credits)")
        os = read_total("Operating Systems (3 credits)")
        total_points = grade_point(data_structures) * 4.0
        total_points = total_points + grade_point(algorithms) * 3.0
        total_points = total_points + grade_point(networking) * 3.0
        total_points = total_points + grade_point(oop) * 4.0
        total_points = total_points + grade_point(os) * 3.0
        total_credits = 4.0 + 3.0 + 3.0+ 4.0 + 3.0
        cgpa = total_points / total_credits
        print(f"CGPA for open credit CSE: {round(cgpa, 2)} ({grade_letter_cgpa(round(cgpa, 2))})")

    elif dept == "eee" or dept == "EEE":
        # Subjects ("Circuit Analysis", "Digital Electronics","Signals and Systems", "Digital Logic", "Control Systems", "EEE")
        print("EEE selected (open credit)")
        circuits = read_total("Circuit Analysis (4 credits)")
        electronics = read_total("Digital Electronics (3 credits)")
        signals = read_total("Signals & Systems (3 credits)")
        logic = read_total("Digital Logic (4 credits)")
        control = read_total("Control Systems (3 credits)")
        total_points = grade_point(circuits) * 4.0
        total_points = total_points + grade_point(electronics) * 3.0
        total_points = total_points + grade_point(signals) * 3.0
        total_points = total_points + grade_point(logic) * 4.0
        total_points = total_points + grade_point(control) * 3.0
        total_credits = 4.0 + 3.0 + 3.0 + 4.0 + 3.0
        cgpa = total_points / total_credits
        print(f"CGPA for open credit CSE: {round(cgpa, 2)} ({grade_letter_cgpa(round(cgpa, 2))})")

    elif dept == "bba" or dept == "BBA":
        # Subjects ("Financial Accounting", "Principles of Management", "Microeconomics", "Business Law", "Marketing", "BBA")
        print("BBA selected (open credit)")
        accounting = read_total("Financial Accounting (3 credits)")
        management = read_total("Principles of Management (3 credits)")
        microeconomics = read_total("Microeconomics (3 credits)")
        business = read_total("Business Law (3 credits)")
        marketing = read_total("Marketing (2 credits)")
        total_points = grade_point(accounting) * 3.0
        total_points = total_points + grade_point(management) * 3.0
        total_points = total_points + grade_point(microeconomics) * 3.0
        total_points = total_points + grade_point(business) * 3.0
        total_points = total_points + grade_point(marketing) * 2.0
        total_credits = 3.0 + 3.0 + 3.0 + 3.0 + 2.0
        cgpa = total_points / total_credits
        print(f"CGPA for open credit CSE: {round(cgpa, 2)} ({grade_letter_cgpa(round(cgpa, 2))})")

    elif dept == "llb" or dept == "LLB":
        #Subjects ("Jurisprudence", "LEGAL SYSTEM OF BANGLADESH", "Critical Theory", "INTERMEDIATE ENGLISH", "LEGAL HISTORY")
        print("English selected (open credit)")
        jurisprudence = read_total("Jurisprudence (3 credits)")
        lsb = read_total("Legal System of Bangladesh (3 credits)")
        criticalTheory = read_total("Critical Theory (3 credits)")
        english = read_total("Intermediate English (3 credits)")
        history = read_total("Legal History (2 credits)")
        total_points = grade_point(jurisprudence) * 3.0
        total_points = total_points + grade_point(lsb) * 3.0
        total_points = total_points + grade_point(criticalTheory) * 3.0
        total_points = total_points + grade_point(english) * 3.0
        total_points = total_points + grade_point(history) * 2.0
        
        total_credits = 3.0 + 3.0 + 3.0 + 3.0 + 2.0
        cgpa = total_points / total_credits
        print(f"CGPA for open credit CSE: {round(cgpa, 2)} ({grade_letter_cgpa(round(cgpa, 2))})")

    elif dept == "economics":
        # Subjects ("Basics in Social Sciences", "Computer Fundamentals", "Introduction to MicroEconomics", "Probability and Statistics")
        print("Economics selected (open credit)")
        bss = read_total("Basics in Social Sciences (3 credits)")
        computer = read_total("Computer Fundamentals (4 credits)")
        microeconomics = read_total("Introduction to MicroEconomics (3 credits)")
        linear = read_total("Linear Algebra (3 credits)")
        statistics = read_total("Probability and Statistics (3 credits)")
        total_points = grade_point(bss) * 3.0
        total_points = total_points + grade_point(computer) * 4.0
        total_points = total_points + grade_point(microeconomics) * 3.0
        total_points = total_points + grade_point(linear) * 3.0
        total_points = total_points + grade_point(statistics) * 3.0
        total_credits = 3.0 + 4.0 + 3.0 + 3.0 + 3.0
        cgpa = total_points / total_credits
        print(f"CGPA for open credit CSE: {round(cgpa, 2)} ({grade_letter_cgpa(round(cgpa, 2))})")
    else:
        print("Open credit mode supports only CSE, EEE, BBA, LLB, or Economics.")


def fixed_credit_block(course_one, course_two, course_three, course_four, course_five, department_label):
    print(department_label + " selected (fixed credit)")
    course_one_total = read_total(course_one + " (3 credits)")
    course_two_total = read_total(course_two + " (3 credits)")
    course_three_total = read_total(course_three + " (3 credits)")
    course_four_total = read_total(course_four + " (3 credits)")
    course_five_total = read_total(course_five + " (3 credits)")
    total_points = grade_point(course_one_total) * 3.0
    total_points = total_points + grade_point(course_two_total) * 3.0
    total_points = total_points + grade_point(course_three_total) * 3.0
    total_points = total_points + grade_point(course_four_total) * 3.0
    total_points = total_points + grade_point(course_five_total) * 3.0
    total_credits = 3.0 + 3.0 + 3.0 + 3.0 + 3.0
    cgpa = total_points / total_credits
    print(f"CGPA for fixed credit {department_label} : {round(cgpa, 2)} ({grade_letter_cgpa(cgpa)})\n" )


def run_fixed_credit(department):
    dept = department.lower()
    if dept == "cse":
        fixed_credit_block("Data Structures", "Algorithms", "Computer Metworks", "Object Oriented Programming", "Operating Systems", "CSE")
    elif dept == "eee":
        fixed_credit_block("Circuit Analysis", "Digital Electronics","Signals and Systems", "Digital Logic", "Control Systems", "EEE")
    elif dept == "bba":
        fixed_credit_block("Financial Accounting", "Principles of Management", "Microeconomics", "Business Law", "Marketing", "BBA")
    elif dept == "llb":
        fixed_credit_block("JURISPRUDENCE", "LEGAL SYSTEM OF BANGLADESH", "Critical Theory", "INTERMEDIATE ENGLISH", "LEGAL HISTORY", "LLB")
    elif dept == "economics":
        fixed_credit_block("Basics in Social Sciences", "Computer Fundamentals", "Introduction to MicroEconomics", "Mathematics", "Probability and Statistics", "Economics")
    else:
        print("Fixed credit mode supports only CSE, EEE, BBA, LLB, or Economics.")


def main():
    while True:
        print("Grade calculator")
        system_choice = input("\nSelect credit system (open/fixed): \n1: fixed\n2: open\n \nOr Press 'q' to quit \n- ").strip().lower()

        if system_choice == 'q' or system_choice == 'exit': 
            print("Goodbye!!!") 
            break

        system_choice = system_choice if system_choice in ["open", "fixed"] else int(system_choice)
        print("system_choice: ", system_choice)
        department = input("Enter department (CSE/EEE/BBA/LLB/Economics): ").strip()
        print("department: ", department)

        
    
        if system_choice == "open" or system_choice == 2:
            run_open_credit(department)
        elif system_choice == "fixed" or system_choice == 1:
            run_fixed_credit(department)
        else:
            print("Invalid credit system. Please choose 'open' or 'fixed'.")


if __name__ == "__main__":
     
    main() 
