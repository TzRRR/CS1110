import fines
print("$", fines.fine(50,20))
print("$", fines.fine(50,75))
print("$", fines.fine(25,30,"work"))
print("$", fines.fine(25,35,"residential"))
print()
print(fines.demerits(75,50), "demerit points")
print(fines.demerits(50,65), "demerit points")
print(fines.demerits(50,75), "demerit points")