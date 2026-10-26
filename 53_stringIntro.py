s=input("enter any word:")

vol=["a","e","i","o","u","A","E","I","O","U"]
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
]
special_chars = [
    "=","+","-","*","/","%","@","&","|","^","~","!","<",">","(",")","[","]","{","}",",",".",";",":","?","#","$","_",
]

number=["1","2","3","4","5","6","7","8","9","0"]


con=0
consonantsCount=0
Cvol=0
Cstr=0
Cspec=0
Cnum=0

for i in s:
    """ print(i,end=",") """
    con+=1
    if i in vol:
        Cvol+=1
    if i in consonants:
        consonantsCount+=1 
    if i in vol or i in consonants:
        Cstr+=1
    if i in number:
        Cnum+=1    
    if i in special_chars:
        Cspec+=1     


print("\n length:",con)
print("number of vowels:",Cvol)
print("number of consonants",consonantsCount)
print("number of letters:",Cstr)
print("number of digits:",Cnum)
print("number of special characters:",Cspec)

