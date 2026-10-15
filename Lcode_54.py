class Solution(object):
    def lengthOfLastWord(self, s):
        
        count=0
        
        if ' '==s[-1]:
            for i in range(1:len(s):-1):
                if ' '==s[i]:
                    lastB=i    
            for i in range(len(s[lastB:])-1):
                count+=1
            
        else:
            for i in range(len(s)):
                if ' '==s[i]:
                    lastB=i    
            for i in range(len(s[lastB:])-1):
                count+=1

        return count        

c= Solution() 

print(c.lengthOfLastWord("   fly me   to   the moon  "))