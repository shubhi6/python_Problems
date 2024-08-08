a=int(input())
b=int(input())
# =map(int,input().split())
opp=input()
if opp=="ADD":
    print(a+b)
elif opp=="SUBB":
    print(abs(a-b))
elif opp=="MULTI":
    print(a*b)
else:
    print(a/b)


