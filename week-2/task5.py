n = int(input().strip())
allowed = "ABCEHKMOPTXY"

for i in range(n):
    s = input().strip()
    
    if len(s) != 6:
        print("No")
        continue
        
    if (s[0] in allowed and s[4] in allowed and s[5] in allowed and 
        s[1].isdigit() and s[2].isdigit() and s[3].isdigit()):
        print("Yes")
    else:
        print("No")