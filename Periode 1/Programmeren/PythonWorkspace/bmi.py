# enge comment wajow
def bodymassindex(hoogte, gewicht):
    return round((gewicht / hoogte**2),2)
g = float(input("Uw gewicht in KG: "))
h = float(input("Uw lengte in meter: "))
bmi = bodymassindex(h, g)
print("Uw bmi is: ", bmi)
if bmi <= 18.5:
    print("je hebt ondergewicht")
elif bmi < 18.5 <= 25:
    print("je hebt gezondgewicht")
elif bmi < 25 <= 30:
    print("je hebt overgewicht")
else:
    print("je hebt obesitas")
