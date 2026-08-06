# ==================================================
# PREPTRACK — BOILERPLATE CODE
# Complete every section marked TODO.
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# TODO: Validate that the student name is not empty.
while True:
    student_name = input("Enter student name: ")

    if student_name != "":
        break

    print("Student name cannot be empty.")

registration_number = input("Enter registration number: ")
graduation_year = int(input("Enter graduation year: "))
if graduation_year >= 2025 and graduation_year <= 2027:
    print("eligible")
else:
    print("Not Eligible")


# TODO: Validate attendance between 0 and 100.
while True:
    attendance = int(input("Enter attendance percentage: "))

    if 0 <= attendance <= 100:
        print("Attendance accepted.")
        break

    print("Invalid attendance. Enter a value between 0 and 100.")
# TODO: Accept only yes or no.
while True:
    project_input = input(
        "Has the student completed the required project?\nEnter yes or no: "
    )

    if project_input == "yes" or project_input == "no":
        break
    else:
        print("Invalid input. Enter only yes or no.")
# TODO: Convert project_input into True or False.
if project_input == "yes":
    project_completed = True
else:
    project_completed = False
# TODO: Accept only yes or no.
while True:
    profile_input = input("Is the student profile verified? Enter yes or no: ")
    if profile_input == "yes" or profile_input == "no":
        break
    else:
        print("Invalid input. Enter only yes or no.")

# TODO: Convert profile_input into True or False.
if profile_input == "yes":
    profile_verified = True
else:
    profile_verified = False