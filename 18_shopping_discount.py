# Apply a 10% discount if the bill exceeds 2000
bill = float(input("Enter the shopping bill amount: "))

if bill < 0:
    print("Invalid bill amount")
elif bill > 2000:
    discount = bill * 0.10
    final_amount = bill - discount
    print(f"Discount: {discount:.2f}")
    print(f"Final amount: {final_amount:.2f}")
else:
    print("No discount")
    print(f"Final amount: {bill:.2f}")
