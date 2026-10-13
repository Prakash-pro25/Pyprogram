# Identify whether a month has 30 days, 31 days, or is February
month = input("Enter the month name: ").strip().lower()

months_31 = ["january", "march", "may", "july",
             "august", "october", "december"]
months_30 = ["april", "june", "september", "november"]

if month in months_31:
    print("This month has 31 days")
elif month in months_30:
    print("This month has 30 days")
elif month == "february":
    print("February has 28 or 29 days")
else:
    print("Invalid month name")
