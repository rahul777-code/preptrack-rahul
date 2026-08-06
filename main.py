# ==================================================
# PREPTRACK - BOILERPLACE CODE# Complete every section marked TODO
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# Student Name Validation
while True:
    student_name = input("Enter student name: ")

    if student_name != "":
        break
    else:
        print("Student name cannot be empty.")


# Registration Number
registration_number = input("Enter registration number: ")


# Graduation Year
graduation_year = int(input("Enter graduation year: "))


# Attendance Validation
while True:
    attendance = float(input("Enter attendance percentage: "))

    if attendance >= 0 and attendance <= 100:
        print("Attendance accepted.")
        break
    else:
        print("Invalid attendance. Enter a value between 0 and 100.")


# Project Completion Validation
while True:
    project_input = input(
        "Has the student completed the required project?\nEnter yes or no: "
    ).lower()

    if project_input == "yes":
        project_completed = True
        break

    elif project_input == "no":
        project_completed = False
        break

    else:
        print("Invalid input. Enter only yes or no.")


# Profile Verification Validation
while True:
    profile_input = input(
        "Is the student profile verified?\nEnter yes or no: "
    ).lower()

    if profile_input == "yes":
        profile_verified = True
        break

    elif profile_input == "no":
        profile_verified = False
        break

    else:
        print("Invalid input. Enter only yes or no.")