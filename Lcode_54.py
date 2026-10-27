class Solution(object):
    def lengthOfLastWord(self, s):
        
        
               
        i = len(s) - 1
        count = 0

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the last word's characters
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count  

c= Solution() 

print(c.lengthOfLastWord("   fly me   to   the moon  "))
print(c.lengthOfLastWord("Hello World"))
print(c.lengthOfLastWord("luffy is still joyboy"))
print(c.lengthOfLastWord("a "))
