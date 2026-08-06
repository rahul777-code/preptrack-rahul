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

# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

# Total Score
total_score = 0

# Practice Counters
attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

# Performance Classification Counters
strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

# Highest Score Details
highest_score = 0
highest_score_day = 0

# Lowest Score Details
lowest_score = 0
lowest_score_day = 0

# Used to initialize highest and lowest score
first_attempt_found = False

# Critical Score Details
critical_score_found = False
first_critical_day = 0
first_critical_score = 0 

for day in range(1, 8):

    while True:
        score = int(
            input(
                f"Enter Day {day} score from 0 to 100, "
                "or -1 for absent: "
            )
        )

        if score == -1 or (0 <= score <= 100):
            break

        print("Invalid score. Enter -1 or a value between 0 and 100.")

# --------------------------------------------------
# 4. CALCULATE THE AVERAGE
# --------------------------------------------------

# TODO: Prevent division by zero.
average_score = 0

# --------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# --------------------------------------------------

# Graduation year should be between 2025 and 2027
graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

# Attendance should be at least 75%
attendance_eligible = attendance >= 75

# Student should attempt at least 6 practice days
practice_count_eligible = attempted_days >= 6

# Average score should be at least 70
average_eligible = average_score >= 70

# There should be no critical score
critical_score_clear = not critical_score_found

# Student should pass at least 4 practice days
passed_days_eligible = passed_days >= 4

# Final Placement Readiness
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

if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice attempted"
    next_action = "Attempt the required coding practices"

elif critical_score_found:
    # Final Status: Critical Support Required
    # Blocker: Critical score found
    # Next Action: Revise concepts from the first critical day
    pass

elif attempted_days < 6:
    # Final Status: Practice Incomplete
    # Next Action: Complete at least six practice days
    pass

elif passed_days < 4:
    # Final Status: Insufficient Passed Practices
    # Next Action: Pass at least four coding practices
    pass

elif average_score < 70:
    # Final Status: Practice Improvement Required
    # Next Action: Improve average score to at least 70
    pass

elif attendance < 75:
    # Final Status: Attendance Improvement Required
    # Next Action: Improve attendance to at least 75 percent
    pass

elif not graduation_eligible:
    # Final Status: Graduation Criteria Not Met
    pass

elif not project_completed:
    # Final Status: Application On Hold
    pass

elif not profile_verified:
    # Final Status: Application On Hold
    pass

else:
    # Final Status: Ready for Mock Interview
    # Next Action: Proceed to placement mock interviews
    pass


# --------------------------------------------------
# 7. DISPLAY FINAL REPORT
# --------------------------------------------------

print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)

print()
print("STUDENT PROFILE")
print()

print(f"Student Name             : {student_name}")
print(f"Registration Number      : {registration_number}")
print(f"Graduation Year          : {graduation_year}")
print(f"Attendance               : {attendance}%")
print(f"Project Completed        : {project_completed}")
print(f"Profile Verified         : {profile_verified}")

print()
print("PRACTICE SUMMARY")
print()

print("Total Practice Days      : 7")
print(f"Attempted Days           : {attempted_days}")
print(f"Absent Days              : {absent_days}")
print(f"Passed Days              : {passed_days}")
print(f"Failed Days              : {failed_days}")

print()
print(f"Strong Days              : {strong_days}")
print(f"Satisfactory Days        : {satisfactory_days}")
print(f"Needs Improvement Days   : {improvement_days}")
print(f"Critical Days            : {critical_days}")

print()
print("PERFORMANCE ANALYSIS")
print()

print(f"Total Score              : {total_score}")
print(f"Average Score            : {average_score:.2f}")

if attempted_days > 0:
    print(f"Highest Score            : {highest_score}")
    print(f"Highest Score Day        : Day {highest_score_day}")
    print(f"Lowest Score             : {lowest_score}")
    print(f"Lowest Score Day         : Day {lowest_score_day}")
else:
    print("Highest Score            : Not Available")
    print("Highest Score Day        : Not Available")
    print("Lowest Score             : Not Available")
    print("Lowest Score Day         : Not Available")

print()
print("CRITICAL SCORE INFORMATION")
print()

print(f"Critical Score Found     : {critical_score_found}")

if critical_score_found:
    print(f"First Critical Day       : Day {first_critical_day}")
    print(f"First Critical Score     : {first_critical_score}")
else:
    print("First Critical Day       : Not Applicable")
    print("First Critical Score     : Not Applicable")

print()
print("FINAL DECISION")
print()

print(f"Final Status             : {final_status}")
print(f"Primary Blocker          : {primary_blocker}")
print(f"Next Action              : {next_action}")

print()
print("=" * 50)