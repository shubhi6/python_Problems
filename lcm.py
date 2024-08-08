# -------------------------PROGRAM TO FIND LCM---------------------------------------------------
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    
    return lcm

x = int(input("ENTER FIRST NUMBER: "))
y = int(input("ENTER SECOND NUMBER: "))

print(f"LCM OF {x} AND {y} IS: {compute_lcm(x, y)}")