# -------------------------PROGRAM TO SWAP TWO NUMBERS WITH THIRD VARIABLE--------------------
n=int(input("ENTER FIRST NUMBER : "))
m=int(input("ENTER SECOND NUMBER : "))
temp=n
n=m
m=temp
print(f"AFTER SWAPPING FIRST NUMBER = {n} AND SECOND NUMBER = {m}")




# -------------------------PROGRAM TO SWAP TWO NUMBERS WITHOUT THIRD VARIABLE-----------------
n=int(input("ENTER FIRST NUMBER : "))
m=int(input("ENTER SECOND NUMBER : "))
n=n+m
m=n-m
n=n-m
print(f"AFTER SWAPPING FIRST NUMBER = {n} AND SECOND NUMBER = {m}")
