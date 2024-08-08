# ---------------------------PROGRAM TO FIND SUM OF ARRAY----------------------------------------
def sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return sum
arr=[]
arr=list(map(int,input("ENTER ELEMENTS OF ARRAY : ").split()))
n=len(arr)
ans=sum(arr)
print(f"SUM OF ARRAY IS : {ans}")

# -------------OR------------
arr=list(map(int,input("ENTER ELEMENTS OF ARRAY : ").split()))
n=len(arr)
print(f"SUM OF ARRAY IS : {sum(arr)}")