s=input("enter the string: ")



for i in s:
    recon=0
    for j in s:
      if j == i:
        recon+=1
    if recon == 1:
       print(f"the first non repetitive is {i}")
       break   

