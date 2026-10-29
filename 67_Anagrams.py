from collections import Counter

def is_anagram(str1, str2):
   
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()
    
    # Anagrams must have the exact same character frequencies
    return Counter(clean_str1) == Counter(clean_str2)

# Test cases
print(is_anagram("Listen", "Silent"))  # Output: True
print(is_anagram("Hello", "World"))    # Output: False
