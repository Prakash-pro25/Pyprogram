import importlib

gcd_module = importlib.import_module("44_GCD")


number1,number2,result=gcd_module.GCD()

LCM=(number1*number2)/result

print(f"The LCM of the num1({number1}) and num2({number2}) is {LCM}")
