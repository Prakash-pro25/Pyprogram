p=input("enter you password:")

vowels=[]
alfL= ["a","e","i","o","u",'b','c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
alfU= ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',"A","E","I","O","U"]
special_chars = [
    "=","+","-","*","/","%","@","&","|","^","~","!","<",">","(",")","[","]","{","}",",",".",";",":","?","#","$","_",
]

number=["1","2","3","4","5","6","7","8","9","0"]


Cnum=0
Clen=0
Cupper=0
CLower=0
Cspcial=0

for i in p:
    Clen+=1
    if i in number:
        Cnum+=1
    if i in alfL:
        CLower+=1
    if i in alfU:
        Cupper+=1
    if i in special_chars:    
        Cspcial+=1

if Clen>=8 and Cnum>0 and CLower>0  and Cspcial>0:
    print ("the password is valid")            
else:
    print("the password is invalid")




