n = input("Enter a number: ")

if n.isdigit() and n[0] != "0" and "0" in n:
    print("Duck number")
else:
    print("Not a Duck number")