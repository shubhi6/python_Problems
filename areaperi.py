# ---------------------------PROGRAM TO FIND AREA AND PERIMETER OF CIRCLE------------------------
def area(r):
    pi=3.14
    print(f"AREA OF CIRCLE IS :  {pi*r*r}")

def peri(r):
    pi=3.14
    print(f"PERIMETER OF CIRCLE IS :  {pi*2*r}")

r=int(input("RADIUS OF CIRCLE IS : "))
area(r)
peri(r)