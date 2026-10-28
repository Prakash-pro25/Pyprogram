s=input().lower()

vol="aeiou"
sp=""

for i in s:
    if i in vol:
        sp+="*"
    else:
        sp+=i    

print(sp)