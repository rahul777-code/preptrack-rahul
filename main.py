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

# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

# --------------------------------------------------
# 3. PROCESS SEVEN PRACTICE DAYS
# --------------------------------------------------

for day in range(1, 8):

    while True:
        try:
            score = int(
                input(
                    f"Enter Day {day} score from 0 to 100, "
                    "or -1 for absent: "
                )
            )

            if score == -1 or (0 <= score <= 100):
                print("Score accepted.")
                break

            print("Invalid score. Enter -1 or a value between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter only numbers.")


    # TODO: Handle absence.
    # Increase absent_days and use continue.
    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
        continue


    # TODO: Increase attempted_days and total_score.

    attempted_days += 1
    total_score += score


    # TODO: Initialize or update:
    # highest_score, highest_score_day,
    # lowest_score and lowest_score_day.

    if not first_attempt_found:
        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True

    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day


    # TODO: Classify the score:
    # 75–100  -> Strong
    # 60–74   -> Satisfactory
    # 40–59   -> Needs Improvement
    # 0–39    -> Critical

    if score >= 75:
        strong_days += 1
        print(f"Day {day} Result: Strong")

    elif score >= 60:
        satisfactory_days += 1
        print(f"Day {day} Result: Satisfactory")

    elif score >= 40:
        improvement_days += 1
        print(f"Day {day} Result: Needs Improvement")

    else:
        critical_days += 1
        print(f"Day {day} Result: Critical")


    # TODO: Count passed and failed days.

    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1


    # TODO: Store only the first critical day and score.

    if score < 40:

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score

# --------------------------------------------------
# 4. CALCULATE THE AVERAGE
# --------------------------------------------------

# TODO: Prevent division by zero.
average_score = 0
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0

# --------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# --------------------------------------------------

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)

# --------------------------------------------------
# 6. DETERMINE FINAL STATUS
# --------------------------------------------------

# TODO: Check conditions in this priority:
# 1. No practice attempted
# 2. Critical score found
# 3. Fewer than six attempts
# 4. Fewer than four passed days
# 5. Average below 70
# 6. Attendance below 75
# 7. Graduation year not eligible
# 8. Project incomplete
# 9. Profile not verified
# 10. Ready for Mock Interview

final_status = ""
primary_blocker = ""
next_action = ""
if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice attempted"
    next_action = "Attempt the required coding practices"

elif critical_score_found:
    final_status = "Critical Support Required"
    primary_blocker = "Critical score found"
    next_action = "Revise the concepts from the first critical day"

elif attempted_days < 6:
    final_status = "Practice Incomplete"
    primary_blocker = "Fewer than six practices attempted"
    next_action = "Complete at least six practice days"

elif passed_days < 4:
    final_status = "Insufficient Passed Practices"
    primary_blocker = "Fewer than four passed practices"
    next_action = "Pass at least four coding practices"

elif average_score < 70:
    final_status = "Practice Improvement Required"
    primary_blocker = "Average score below 70"
    next_action = "Improve the average score to at least 70"

elif attendance < 75:
    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance below 75"
    next_action = "Improve attendance to at least 75 percent"

elif not graduation_eligible:
    final_status = "Graduation Criteria Not Met"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check the eligible graduation-year requirement"

elif not project_completed:
    final_status = "Application On Hold"
    primary_blocker = "Project incomplete"
    next_action = "Complete the required project"

elif not profile_verified:
    final_status = "Application On Hold"
    primary_blocker = "Profile not verified"
    next_action = "Complete profile verification"

else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to placement mock interviews"


# --------------------------------------------------
# 7. DISPLAY FINAL REPORT
# --------------------------------------------------

print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)

print(f"Student Name           : {student_name}")
print(f"Registration Number    : {registration_number}")
print(f"Graduation Year        : {graduation_year}")
print(f"Attendance             : {attendance}%")
print(f"Project Completed      : {'Yes' if project_completed else 'No'}")
print(f"Profile Verified       : {'Yes' if profile_verified else 'No'}")

print()
print(f"Attempted Days         : {attempted_days}")
print(f"Absent Days            : {absent_days}")
print(f"Passed Days            : {passed_days}")
print(f"Failed Days            : {failed_days}")

print()
print(f"Strong Days            : {strong_days}")
print(f"Satisfactory Days      : {satisfactory_days}")
print(f"Needs Improvement Days : {improvement_days}")
print(f"Critical Days          : {critical_days}")

print()
print(f"Total Score            : {total_score}")
print(f"Average Score          : {average_score:.2f}")
print()

# TODO: Display highest and lowest values only when
# at least one practice was attempted.
if attempted_days > 0:
    print(f"Highest Score          : {highest_score}")
    print(f"Highest Score Day      : Day {highest_score_day}")
    print(f"Lowest Score           : {lowest_score}")
    print(f"Lowest Score Day       : Day {lowest_score_day}")
else:
    print("Highest Score          : Not Available")
    print("Highest Score Day      : Not Available")
    print("Lowest Score           : Not Available")
    print("Lowest Score Day       : Not Available")
print()

# TODO: Display first critical details only when
# a critical score exists.
if critical_score_found:
    print("Critical Score Found   : Yes")
    print(f"First Critical Day     : Day {first_critical_day}")
    print(f"First Critical Score   : {first_critical_score}")
else:
    print("Critical Score Found   : No")
    print("First Critical Day     : Not Applicable")
    print("First Critical Score   : Not Applicable")
print()
print(f"Final Status           : {final_status}")
print(f"Primary Blocker        : {primary_blocker}")
print(f"Next Action            : {next_action}")

print("=" * 50)