ch = input("Enter a character: ")

# Convert to lowercase to check both cases easily
if ch.isalpha() and len(ch) == 1:
  if ch.lower() in "aeiou":
    print(f"'{ch}' is a vowel.")
  else:
    print(f"'{ch}' is a consonant.")
else:
  print("Please enter a single valid alphabet letter.")