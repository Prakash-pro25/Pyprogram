# Check scholarship eligibility based on marks and attendance
# Requirements: marks >= 90 and attendance >= 85%
marks = float(input("Enter the student's marks (0-100): "))
attendance = float(input("Enter attendance percentage (0-100): "))

if not (0 <= marks <= 100 and 0 <= attendance <= 100):
    print("Invalid input. Marks and attendance must be between 0 and 100.")
elif marks >= 90 and attendance >= 85:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
