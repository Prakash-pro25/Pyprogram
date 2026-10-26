


def GCD():
    num1 =int(input())
    num2 =int(input())

    GCD=0

    for i in range(1,num2+1 if num1 < num2 else num1+1):
            if num2%i==0 and num1%i==0:
                GCD =i
    return num1,num2,GCD


     
