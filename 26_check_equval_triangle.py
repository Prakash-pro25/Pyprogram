def check_triangle_type(a, b, c):
   
    if (a + b > c) and (a + c > b) and (b + c > a):
        
        if a == b == c:
            return "Equilateral Triangle"
        
      
        elif a == b or b == c or a == c:
            return "Isosceles Triangle"
        

        else:
            return "Scalene Triangle"
            
    else:
        return "Not a valid triangle"


side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

result = check_triangle_type(side1, side2, side3)
print(f"Result: {result}")
