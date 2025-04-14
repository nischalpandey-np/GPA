from tabulate import tabulate

# Define subjects with credit breakdowns and maximum marks
subjects = [
    {"name": "English", "total_credits": 4, "theory_credits": 3.00, "internal_credits": 1.00, "theory_max": 75, "internal_max": 25},
    {"name": "Nepali", "total_credits": 3, "theory_credits": 2.25, "internal_credits": 0.75, "theory_max": 75, "internal_max": 25},
    {"name": "Maths", "total_credits": 5, "theory_credits": 3.75, "internal_credits": 1.25, "theory_max": 75, "internal_max": 25},
    {"name": "Physics", "total_credits": 5, "theory_credits": 3.75, "internal_credits": 1.25, "theory_max": 75, "internal_max": 25},
    {"name": "Chemistry", "total_credits": 5, "theory_credits": 3.75, "internal_credits": 1.25, "theory_max": 75, "internal_max": 25},
    {"name": "Computer Science", "total_credits": 5, "theory_credits": 3.75, "internal_credits": 1.25, "theory_max": 50, "internal_max": 50},
]

# Total credits
total_credit_hours = sum(subject["total_credits"] for subject in subjects)

# GPA scale based on percentage
def percentage_to_grade_point(percentage):
    if 90 <= percentage <= 100:
        return 4.0
    elif 80 <= percentage < 90:
        return 3.6
    elif 70 <= percentage < 80:
        return 3.2
    elif 60 <= percentage < 70:
        return 2.8
    elif 50 <= percentage < 60:
        return 2.4
    elif 40 <= percentage < 50:
        return 2.0
    elif 35 <= percentage < 40:
        return 1.6
    else:
        return 0.0

# Helpers
def marks_to_percentage(marks, max_marks):
    return (marks / max_marks) * 100

def validate_gpa(gpa):
    return 0.0 <= gpa <= 4.0

def get_grade_point(input_type, value, max_marks=None):
    if input_type == "percentage":
        return percentage_to_grade_point(value)
    elif input_type == "gpa":
        return value
    elif input_type == "marks":
        percentage = marks_to_percentage(value, max_marks)
        return percentage_to_grade_point(percentage)
    else:
        raise ValueError("Invalid input type")

def calculate_subject_grade(theory_value, internal_value, theory_credits, internal_credits, total_credits, input_type, theory_max, internal_max, subject_name):
    theory_grade_point = get_grade_point(input_type, theory_value, theory_max)
    internal_grade_point = get_grade_point(input_type, internal_value, internal_max)
    weighted_grade = (theory_grade_point * theory_credits + internal_grade_point * internal_credits) / total_credits
    return weighted_grade, theory_grade_point, internal_grade_point

# Main GPA Calculator
def calculate_gpa():
    print("=== NEB GPA Calculator for Grade 12 (2082) ===")
    print("Choose how you want to input your marks:")
    print("1. GPA (Grade Point, e.g., 3.6 for A)")
    print("2. Raw Marks (e.g., 60 out of 75 for Theory)")

    while True:
        try:
            choice = int(input("Enter your choice (1 or 2): "))
            if choice in [1, 2]:
                break
            else:
                print("Invalid choice. Enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    input_type = {1: "gpa", 2: "marks"}[choice]
    print(f"\nYou chose to input as: {input_type.upper()}")

    total_grade_points = 0.0
    table_data = []

    for subject in subjects:
        subject_name = subject["name"]
        internal_label = "Practical" if subject_name == "Computer Science" else "Internal"

        # Get theory input
        while True:
            try:
                theory_input = float(input(f"Enter Theory ({subject_name}) ({'GPA' if input_type == 'gpa' else f'Marks out of {subject['theory_max']}' }): "))
                if input_type == "gpa" and not validate_gpa(theory_input):
                    raise ValueError
                if input_type == "marks" and not (0 <= theory_input <= subject["theory_max"]):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Try again.")

        # Get internal/practical input
        while True:
            try:
                internal_input = float(input(f"Enter {internal_label} ({subject_name}) ({'GPA' if input_type == 'gpa' else f'Marks out of {subject['internal_max']}' }): "))
                if input_type == "gpa" and not validate_gpa(internal_input):
                    raise ValueError
                if input_type == "marks" and not (0 <= internal_input <= subject["internal_max"]):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Try again.")

        # Calculate
        subject_gpa, theory_gpa, internal_gpa = calculate_subject_grade(
            theory_input,
            internal_input,
            subject["theory_credits"],
            subject["internal_credits"],
            subject["total_credits"],
            input_type,
            subject["theory_max"],
            subject["internal_max"],
            subject_name
        )

        credit_grade_point = subject_gpa * subject["total_credits"]
        total_grade_points += credit_grade_point

        table_data.append([
            subject_name,
            f"{internal_gpa:.2f}",
            f"{theory_gpa:.2f}",
            f"{subject_gpa:.2f}"
        ])

    # Final GPA
    final_gpa = total_grade_points / total_credit_hours

    # Table display
    headers = ["Subject", "Internal/Practical GPA", "Theory GPA", "Overall GPA"]
    print("\n=== GPA Summary Table ===")
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    # Final result
    print("\n=== Final Result ===")
    print(f"Total Credit Hours: {total_credit_hours}")
    print(f"Total (Credit × Grade Point): {total_grade_points:.2f}")
    print(f"🎓 Your Final GPA: {final_gpa:.2f}")

# Run the program
if __name__ == "__main__":
    calculate_gpa()
