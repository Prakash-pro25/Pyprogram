# Check eligibility for a student discount based on age
# Assumption: anyone under 18 qualifies
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 18:
    print("Eligible for the student discount")
else:
    print("Not eligible for this age-based discount")
