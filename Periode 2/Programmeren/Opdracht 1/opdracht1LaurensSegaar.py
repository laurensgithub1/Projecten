#Laurens Segaar
#versie 1
#15/11/2023

import random
#Hier komt een random getal voor de dobbelsteen
n = True
def main():
    score = 0
    input("klik op enter om te dobbelen...")
    getal1 = random.randint(1,6)
    if getal1 == 1:
        getal1 = 0
    elif getal1 == 6:
        getal1 = 12
    else:
        getal1 = getal1
    score = score + getal1

    getal2 = random.randint(1,6)
    if getal2 == 1:
        getal2 = 0
    elif getal2 == 6:
        getal2 = 12
    else:
        getal2 = getal2
    score = score + getal2

    getal3 = random.randint(1,6)
    if getal3 == 1:
        getal3 = 0
    elif getal3 == 6:
        getal3 = 12
    else:
        getal3 = getal3
    score = score + getal3

    print("Jij hebt",getal1,",",getal2,"en",getal3,"gegooid! Jouw score is:", score)

while n == True:
    main()