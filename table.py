# ---------------------------PRINT A TABLE FOR A GIVEN NUMBER--------------------------------
n=int(input("ENTER A NUMBER : "))
print(f"TABLE FOR GIVEN NUMBER {n} IS :")
for i in range(1,11):
    print(f"{n}X{i}={i*n}")