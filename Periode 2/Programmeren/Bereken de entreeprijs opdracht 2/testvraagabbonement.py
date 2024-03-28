def vraagabonnement():
    #hier word de code geschreven om abonnement te vragen    
    heeftAbo=False
    antw="Q"
    while antw not in ["J","N"]:
        antw = input("heb je een abonnement  (j/n)? "   ).upper()
    if antw=="J":
        heeftAbo=True
    else:
        heeftAbo=False

    #print(vraagabonnement)
    return heeftAbo



print("Uw abonnement: ", vraagabonnement())