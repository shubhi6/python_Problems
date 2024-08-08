# --------------------------PRINT PRIME NUMBERS UPTO GIVEN INTERVAL-------------------------
s=int(input())
e=int(input())
for i in range(s,e+1):
    if i>1:
        for j in range(2,int(i ** 0.5) + 1):
            if(i%j==0):
                break
        else:
            print(i)