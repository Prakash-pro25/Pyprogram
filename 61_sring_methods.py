s=" prAkAsh iS a GoOd boY "
s1="*prakash*"

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.swapcase())
print(s.title())

print("\n")


print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s1.strip("*"))

print("\n")


print(s.count("a"))
print(s.find("good"))
print(s.find("GoOd"))
print(s.find("ka"))


print("\n")

print(s.index("prA")) # index and find like same but that is not in string it return the error but find is return -1

a="apple apple apple"

print(a.replace("apple","mango"))
print(a.replace("apple","mango",1))
print(a.replace("apple","mango",2))
print(a.replace("apple","mango",-1))
print(a.replace("apple","mango",-2))


print("\n")

p="Hellow123(&$()) "

print(p.isalpha())
print(p.isalnum())
print(p.isdigit())
print(p.islower())
print(p.isupper())
print(p.istitle())
print(p.isspace())






