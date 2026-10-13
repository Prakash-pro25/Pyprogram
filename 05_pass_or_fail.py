# Check whether a student passes or fails
# Assumption: 35 marks is the pass mark
mark = float(input("Enter the mark: "))

if 0 <= mark <= 100:
    if mark >= 35:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid mark. Enter a mark from 0 to 100.")
