def vraagleeftijd():
    #hier word een code geschreven om leeftijd te vragen
    invoerOk=False
    while not invoerOk:
        leeftijd = int(input("Wat is uw leeftijd"))
        if leeftijd<7 or leeftijd>120:
            print("FOUT, de leeftijd moet tussen 7 en 120 liggen!")
            invoerOk=False
        else:
            invoerOk=True
    
    
    
    #print(leeftijd)
    return leeftijd



print("Uw leeftijd is: ", vraagleeftijd())